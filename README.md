# Student Information System

A small CLI-based Student Information System demonstrating:
- CRUD operations (JSON persistence)
- Modular design and configuration
- Logging and error handling
- Unit tests and CI (GitHub Actions)

## Features
- Add, view, update, delete students
- Data stored in `data/students.json`
- Configurable via `config/config.json`
- Logging to `logs/app.log`
- Tests with `pytest` and CI via GitHub Actions

## Project structure
(briefly show tree)

## Setup (local)
```bash
git clone <your-repo-url>
cd student-info-system
python -m venv .venv
source .venv/bin/activate  # or .venv\Scripts\activate on Windows
pip install -r requirements.txt
python src/main.py
