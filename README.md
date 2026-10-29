# Pytest + GitHub Actions Demo

A small Python project demonstrating unit tests with `pytest` and automatic test execution with GitHub Actions.

## Project structure

```text
pytest_github_actions_project/
├── src/
│   ├── __init__.py
│   └── calculator.py
├── tests/
│   └── test_calculator.py
├── .github/
│   └── workflows/
│       └── tests.yml
├── requirements.txt
├── pytest.ini
├── .gitignore
└── README.md
```

## Run locally (Windows PowerShell)

```powershell
py -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
python -m pytest
```

If PowerShell blocks activation, you can use the environment's Python directly:

```powershell
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
.\.venv\Scripts\python.exe -m pytest
```

## What is tested?

- Addition of positive and negative numbers
- Subtraction
- Multiplication
- Division
- Division by zero raises the expected exception

## Enable GitHub Actions

1. Create a new GitHub repository.
2. Extract this project and open a terminal in its folder.
3. Run:

   ```bash
   git init
   git add .
   git commit -m "Add pytest unit tests and GitHub Actions"
   git branch -M main
   git remote add origin https://github.com/YOUR_USERNAME/YOUR_REPOSITORY.git
   git push -u origin main
   ```

4. Replace the remote URL with your repository's actual URL.
5. Open the repository on GitHub and select **Actions**. The `Python Unit Tests` workflow should run after the push.
6. Every later push and pull request will trigger the tests automatically.

## Workflow behavior

The workflow checks out the code, configures Python 3.12, installs dependencies from `requirements.txt`, and runs `python -m pytest`. A failing test causes the GitHub Actions job to fail.
