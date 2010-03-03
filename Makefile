default:
	java -cp ./lib/antlrworks-1.3.1.jar org.antlr.Tool Slidescript.g

examples:
	./pythonenv/bin/python slidescript.py examples/party.slide --js examples/party.js
	./pythonenv/bin/python slidescript.py examples/party.slide --html examples/party.html
	./pythonenv/bin/python slidescript.py examples/party.slide --xls examples/party.xls
	./pythonenv/bin/python slidescript.py examples/party.slide --dot examples/party.dot
	dot -Tpng -v -o examples/party.png examples/party.dot

dependencies:
	virtualenv pythonenv
	pip -E pythonenv -q install -r requirements.txt

clean:
	rm Slidescript.tokens SlidescriptLexer.* SlidescriptParser.*

.PHONY: examples