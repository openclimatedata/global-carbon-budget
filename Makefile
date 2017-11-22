CSV_FILES = \
  data/global-carbon-budget.csv \
  data/fossil-fuel-cement.csv \
  data/fossil-fuel-cement-per-capita.csv \
  data/land-use-change.csv \
  data/ocean-sink.csv \
  data/terrestrial-sink.csv \
  data/historical-budget.csv \
  data/territorial-emissions-cdiac.csv \
  data/territorial-emissions-gcb.csv \
  data/consumption-emissions.csv \
  data/emissions-transfers.csv \
  data/country-definitions.csv

all: $(CSV_FILES)

data/%.csv: scripts/%.py scripts/util.py venv
	@echo $@
	@./venv/bin/python $<

validate:
	@./venv/bin/python scripts/check.py
	@./venv/bin/python scripts/validate.py

venv: scripts/requirements.txt
	[ -d ./venv ] || python3 -m venv venv
	./venv/bin/pip install --upgrade pip
	./venv/bin/pip install -Ur scripts/requirements.txt
	touch venv

clean:
	rm -rf data/*.csv

clean-venv:
	rm -rf venv

.PHONY: clean validate
