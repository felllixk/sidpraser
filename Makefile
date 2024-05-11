build:
	pyinstaller sidparser.spec

clean:
	rm -rf build dist *.spec

.PHONY: build clean