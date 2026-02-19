# API_Backend_Automation_Sample

Backend Automation for [JSONPlaceholder](https://jsonplaceholder.typicode.com/) using BDD Framework (Behave/Cucumber) and Python requests package.

## Prerequisites

- Git
- Python 3.9+ (recommended)

## Project Workflow

### 1. Clone the Repository

```bash
git clone https://github.com/ashishnaik-star/API_Backend_Automation_Sample.git
cd API_Backend_Automation_Sample
```

### 2. Create Virtual Environment

```powershell
python -m venv .venv
```

### 3. Activate Virtual Environment

**Windows (PowerShell):**
```powershell
.\.venv\Scripts\Activate.ps1
```

**Windows (CMD):**
```cmd
.venv\Scripts\activate.bat
```

**Linux/macOS:**
```bash
source .venv/bin/activate
```

### 4. Install Dependencies

```bash
pip install --upgrade pip
pip install -r requirements.txt
```

### 5. Run Test Suite

**Run all features:**
```bash
behave features
```

**Run with Allure reporting:**
```bash
behave --no-capture -f allure_behave.formatter:AllureFormatter -o %allure_result_folder% features
```

**Run a specific feature:**
```bash
behave features/Api_check_set_one.feature
```

## Test Coverage

- **Set 1**: GET requests - Posts, Comments, Albums, Photos validation
- **Set 2**: Single resource retrieval and comment filtering
- **Set 3**: POST, PUT, PATCH, DELETE operations

## Recent Fixes (v2.0)

- Fixed PYTHONPATH issues for module imports
- Updated step implementations for robustness
- Pinned dependency versions for reproducibility
- All 11 scenarios passing (21 steps)
