# Makefile to set up Python notebook environment

.PHONY: install venv clean

# Set up virtual environment and install dependencies
install: venv
	. venv/bin/activate && pip install -r requirements.txt && python -m ipykernel install --user --name=venv --display-name "Python (venv)"

# Create virtual environment if not exists
venv:
	python -m venv venv

# Clean up virtual environment
clean:
	rm -rf venv
