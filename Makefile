slidescript/Slidescript.tokens: slidescript/Slidescript.g
	(cd slidescript ; java -cp ../lib/antlrworks-1.3.1.jar org.antlr.Tool Slidescript.g)

test: slidescript/Slidescript.tokens
	(cd test ; make)

examples:
	./pythonenv/bin/python slidec examples/party.slide --resolved examples/party.vars
	./pythonenv/bin/python slidec examples/party.slide --js examples/party.js
	./pythonenv/bin/python slidec examples/party.slide --html examples/party.html
	./pythonenv/bin/python slidec examples/party.slide --xls examples/party.xls
	./pythonenv/bin/python slidec examples/party.slide --tex examples/party.tex
	(cd examples ; pdflatex party.tex party.pdf)
	./pythonenv/bin/python slidec examples/party.slide --dot examples/party.dot
	dot -Tpng -v -o examples/party.png examples/party.dot

dependencies:
	virtualenv --no-site-packages --distribute pythonenv 
	pip -E pythonenv -q install -r requirements.txt

clean:
	rm -Rf slidescript/Slidescript.tokens slidescript/SlidescriptLexer.* \
	slidescript/SlidescriptParser.* build dist *.egg-info

install:
	python setup.py install


.PHONY: examples test
