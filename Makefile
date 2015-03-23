VIRTUALENV=~/mock-all-things/env

nosetests:
	$(VIRTUALENV)/bin/nosetests --cover-package=mockly --with-coverage --cover-erase --cover-tests --stop