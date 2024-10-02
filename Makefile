VENV = venv
PYTHON = $(VENV)/bin/python3
PIP = $(VENV)/bin/pip
EXTRACTED_DIR = extracted_files

.PHONY: data clean

all: data

data: $(VENV)/bin/activate
	$(PYTHON) scripts/process.py

$(VENV)/bin/activate: scripts/requirements.txt
	python3 -m venv $(VENV)
	$(PIP) install -r scripts/requirements.txt

clean:
	rm -rf __pycache__
	rm -rf $(VENV)
	find . -maxdepth 1 -name "*.zip" -exec rm -f {} +
	if [ -d $(EXTRACTED_DIR) ]; then rm -rf $(EXTRACTED_DIR); fi