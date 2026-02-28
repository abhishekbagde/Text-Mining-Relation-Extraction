import base64
import json
import os
import re


def _as_text(value):
    if isinstance(value, list):
        return "".join(value)
    return value


png_count = 0
svg_count = 0

try:
    with open("Notebooks/training_demo.ipynb", "r", encoding="utf-8") as f:
        nb = json.load(f)

    os.makedirs("assets/images", exist_ok=True)

    for cell in nb.get("cells", []):
        if cell.get("cell_type") != "code":
            continue

        for output in cell.get("outputs", []):
            data = output.get("data", {})
            if not data:
                continue

            # Standard image outputs from matplotlib and similar libraries.
            if "image/png" in data:
                img_data = _as_text(data["image/png"])
                img_bytes = base64.b64decode(img_data)
                png_count += 1
                with open(f"assets/images/result_{png_count}.png", "wb") as img_f:
                    img_f.write(img_bytes)

            # Some notebook renderers (e.g., displaCy) emit SVG inside text/html.
            if "text/html" in data:
                html = _as_text(data["text/html"])
                match = re.search(r"(<svg[\s\S]*?</svg>)", html)
                if match:
                    svg_count += 1
                    with open(f"assets/images/result_{svg_count}.svg", "w", encoding="utf-8") as svg_f:
                        svg_f.write(match.group(1))

    print(
        f"Extracted {png_count} PNG image(s) and {svg_count} SVG image(s) from notebook."
    )
except Exception as e:
    print(f"Error extracting images: {e}")
