
hackytest-init:
	printf 'hackytestproject\n\n\n\n\n\n\n\n\n\n\n\n\n\n' | cookiecutter .
	(cd hackytestproject && make install)

TMPDIR := $(shell mktemp -d)
hackytest-reset:
	mv hackytestproject ${TMPDIR}


.PHONY: hackytest
TMPDIR := $(shell mktemp -d)
hackytest:
	printf 'testproject\n\n\n\n\n\n\n\n\n\n\n\n\n\n' | cookiecutter . --output-dir ${TMPDIR}
	echo # newline for the users shell shell
	cp -r ./hackytestproject/venv ${TMPDIR}/testproject/venv
	cp -r ./hackytestproject/node_modules ${TMPDIR}/testproject/node_modules
	(cd ${TMPDIR}/testproject/ \
	&& venv/bin/python manage.py migrate \
	&& make watch)
