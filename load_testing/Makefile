URL=https://us-east1-taller3-ofernandez.cloudfunctions.net

.PHONY: install
install:
	pip3 install -r requirements.txt;

.PHONY: run
run:
	locust -f main.py --host=$(URL);
