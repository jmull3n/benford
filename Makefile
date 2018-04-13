FILE_PATH ?= ./census_2009

init:
	@pip install -r requirements.txt

test:
	@python3 -m unittest discover -v

run:
	@python3 lab7_benford_calculator/main.py -f census_2009 -nc 7_2009

lint:
	pylint --rcfile=.pylintrc \lab7_benford_calculator -f parseable -r n && \
	mypy --silent-imports \lab7_benford_calculator && \
	pycodestyle \lab7_benford_calculator --max-line-length=120 && \
	pydocstyle \lab7_benford_calculator

clean:
	@find . | grep -E "(__pycache__|\.pyc|\.pyo)" | xargs rm -rf