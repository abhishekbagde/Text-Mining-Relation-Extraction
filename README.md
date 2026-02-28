# Text Mining: Relation Extraction

This repository contains the code and resources for the **Text Mining** project, which explores different techniques for **Relation Extraction (RE)**. The project evaluates and compares various methods ranging from traditional rule-based and bootstrapping algorithms to modern deep learning architectures.

## Project Structure

The repository is organized into the following main directories:

- **`BREDS/`**: Implementation of Bootstrapping Relationship Extraction.
- **`DocRED/`**: Document-level Relation Extraction tools and experiments.
- **`SemEval/`**: Models and data related to the SemEval 2010 Task 8 benchmark.
- **`Symbolic/`**: A Symbolic Bootstrapping approach for extracting relations.
- **`Notebooks/`**: Jupyter notebooks containing exploratory data analysis, visualizations, and demonstrations of the models (`training_demo.ipynb`, `RE_ruleBase.ipynb`).
- **`Reports_and_Literature/`**: Contains the final project report (`PROJECT_REPORT.pdf`) and relevant literature papers studied during the project.

## Highlights and Results

The core of the project involves training and evaluating different relation extraction models. Key insights and results can be observed in the demonstration notebooks. 

Below are some visualized results from our training runs:

![Result 1](assets/images/result_1.png)
*(Note: Images extracted from `training_demo.ipynb` notebook)*

## Getting Started

### Prerequisites

Ensure you have Python 3.7+ installed. We recommend setting up a virtual environment.

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt # Make sure to install the respective requirements in each subfolder
```

### Running the Notebooks

To interact with the exploratory analysis and training demonstrations:

```bash
cd Notebooks
jupyter notebook
```

Open `training_demo.ipynb` or `RE_ruleBase.ipynb` to view the details of the rule-based approaches vs. machine learning models.

## License

This project is created for academic purposes. Refer to individual subdirectories for specific code licenses if applicable.
