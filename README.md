# Playwright Python Test Automation Framework

A robust test automation framework built with Playwright Python for web testing, featuring BDD support, parallel execution, API testing capabilities, and Allure reporting.

## 🚀 Features

- Page Object Model design pattern
- Parallel test execution with pytest-xdist
- Data-driven testing using CSV and JSON
- API testing and mocking capabilities
- BDD support with pytest-bdd (commented out but ready to use)
- Allure reporting integration
- Docker support for CI/CD
- GitHub Actions integration

## 🛠 Tech Stack

- Python with Playwright
- pytest as the test runner
- pytest-xdist for parallel execution
- Allure for reporting
- Docker for containerization
- GitHub Actions for CI/CD

## 🔧 Setup

1. Clone the repository
```bash
git clone <repository-url>
cd py-playwright
```

2. Create and activate virtual environment
```bash
python -m venv venv
source venv/bin/activate  # On Windows: .\venv\Scripts\activate
```

3. Install dependencies
```bash
pip install -r requirements.txt
```

4. Install Playwright browsers
```bash
playwright install
```

## 🏃 Running Tests

### Local Execution

Run all tests:
```bash
pytest
```

Run tests in parallel:
```bash
pytest -n auto
```

Run with Playwright debug mode:
```bash
PWDEBUG=1 pytest -s
```

### Docker Execution

Build and run using Docker:
```bash
docker build -t py-playwright:test .
docker run --rm --shm-size=2g py-playwright:test
```

## 📊 Test Reports

Generate Allure report:
```bash
pytest --alluredir=build/allure-results
allure serve build/allure-results
```

## 📁 Project Structure

```
py-playwright/
├── pages/                 # Page Object Models
├── tests/
│   ├── features/         # BDD feature files
│   ├── step_definitions/ # BDD step definitions
│   └── conftest.py      # pytest fixtures and configuration
├── data/                 # Test data files
├── utils/                # Helper utilities
└── Dockerfile           # Docker configuration
```

## 🔄 CI/CD Integration

The framework includes two GitHub Actions workflows:
- `playwright-gh.yaml`: Runs tests directly on GitHub runner
- `playwright-docker.yaml`: Runs tests in Docker container

## 🌟 Best Practices

- Page Object Model for better maintainability
- Data-driven approach using external test data
- API mocking capabilities for reliable testing
- Parallel execution support
- Comprehensive reporting with Allure
- Docker support for consistent execution environment

## 📝 Configuration

Environment variables:
- `BASE_URL`: Base URL for tests (default: https://www.automationexercise.com/)
- `PWDEBUG`: Enable Playwright debug mode