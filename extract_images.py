import json
import base64
import os

try:
    with open('Notebooks/training_demo.ipynb', 'r', encoding='utf-8') as f:
        nb = json.load(f)

    os.makedirs('assets/images', exist_ok=True)
    img_count = 0
    for cell in nb.get('cells', []):
        if cell.get('cell_type') == 'code':
            for output in cell.get('outputs', []):
                if 'data' in output and 'image/png' in output['data']:
                    img_data = output['data']['image/png']
                    img_bytes = base64.b64decode(img_data)
                    with open(f'assets/images/result_{img_count + 1}.png', 'wb') as img_f:
                        img_f.write(img_bytes)
                    img_count += 1
    print(f"Extracted {img_count} images from notebook.")
except Exception as e:
    print(f"Error extracting images: {e}")
