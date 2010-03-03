default:
	java -cp ./antlrworks-1.3.1.jar org.antlr.Tool Slidescript.g

examples:
	./pythonenv/bin/python slidescript.py examples/party.slide --dot examples/party.dot
	dot -Tpng -v -o examples/party.png examples/party.dot

dependencies:
	virtualenv pythonenv
	pip -E pythonenv -q install -r requirements.txt

clean:
	rm Slidescript.tokens SlidescriptLexer.* SlidescriptParser.*

.PHONY: examples