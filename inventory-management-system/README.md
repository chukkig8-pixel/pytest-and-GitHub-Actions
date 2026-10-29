# Inventory Management System

A simple Python inventory management application with unit tests written using `pytest` and automated test execution using GitHub Actions.

## Project structure

```text
inventory-management-system/
├── inventory.py
├── tests/
│   └── test_inventory.py
├── requirements.txt
├── .github/
│   └── workflows/
│       └── tests.yml
├── .gitignore
└── README.md
```

## Features

- Add products and reject duplicate IDs
- Validate product names, prices, and quantities
- Retrieve products
- Increase stock
- Sell products while checking available stock
- Remove products
- Calculate total inventory value

## Run locally on Windows PowerShell

```powershell
py -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
python -m pytest -v
```

## Run with GitHub Actions

The workflow at `.github/workflows/tests.yml` runs on every push and on pull requests targeting `main`. It sets up Python 3.12, installs requirements, and runs `python -m pytest -v`.

## Push to GitHub

Create an empty GitHub repository, then run these commands from this folder:

```bash
git init
git add .
git commit -m "Add inventory management system and tests"
git branch -M main
git remote add origin https://github.com/YOUR_USERNAME/YOUR_REPOSITORY.git
git push -u origin main
```

Replace the URL with your repository's actual URL. If the folder is already a Git repository, do not run `git init` again; check `git remote -v` and update `origin` if needed.
