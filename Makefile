venv:
    python -m venv venv

setup: venv
    source venv/bin/activate && pip install -r requirements.txt

test:
    python -m unittest discover tests

run:
    python my_calculator/calculator.py
