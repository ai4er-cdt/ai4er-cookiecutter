# {{cookiecutter.project_name}}

{{cookiecutter.description}}
{% if cookiecutter.open_source_license == "MIT" %} [![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
{% elif cookiecutter.open_source_license == "BSD" %} [![License](https://img.shields.io/badge/License-BSD%203--Clause-blue.svg)](https://opensource.org/licenses/BSD-3-Clause)
{% elif cookiecutter.open_source_license == "GPLv3" %} [![License: GPL v3](https://img.shields.io/badge/License-GPL%20v3-blue.svg)](http://www.gnu.org/licenses/gpl-3.0)
{% elif cookiecutter.open_source_license == "Apache Software License 2.0" %} [![License](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](https://opensource.org/licenses/Apache-2.0)
{% endif %}

## Project Organization
```
├── LICENSE
├── Makefile           <- Makefile with commands like `make init` or `make lint-requirements`
├── README.md          <- The top-level README for developers using this project.
|
├── notebooks          <- Jupyter notebooks. Naming convention is a number (for ordering),
│                         the creator's initials, and a short `-` delimited description, e.g.
│                         `1.0-jqp-initial-data-exploration`.
│
├── report             <- Generated analysis as HTML, PDF, LaTeX, etc.
│   ├── figures        <- Generated graphics and figures to be used in reporting
│   └── sections       <- LaTeX sections. The report folder can be linked to your overleaf
|                         report with github submodules.
│
├── requirements.txt   <- The requirements file for reproducing the analysis environment, e.g.
│                         generated with `pip freeze > requirements.txt`
│
├── setup.py           <- makes project pip installable (pip install -e .) so src can be imported
├── src                <- Source code for use in this project.
│   ├── __init__.py    <- Makes src a Python module
│   │
│   ├── data           <- Scripts to download or generate data
│   │
│   ├── preprocessing  <- Scripts to turn raw data into clean data and features for modeling
|   |
│   ├── models         <- Scripts to train models and then use trained models to make
│   │                     predictions
│   │
│   └── tests          <- Scripts for unit tests of your functions
│
└── setup.cfg          <- setup configuration file for linting
```

---

Project template created by the [Cambridge AI4ER Cookiecutter](https://github.com/ai4er-cdt/ai4er-cookiecutter).