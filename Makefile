build:
	pyinstaller --onefile src/main.py --name sidparser --specpath build

clean:
	rm -rf build dist *.spec

.PHONY: build clean