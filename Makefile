VIRTUALENV=~/mock-all-things/env

nosetests:
	$(VIRTUALENV)/bin/nosetests test/ --cover-package=mockly --with-coverage --cover-erase --cover-tests --stop