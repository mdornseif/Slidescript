default:
	java -cp ./antlrworks-1.2.2.jar org.antlr.Tool Slidescript.g 

dependencies:
	virtualenv pythonenv
	pip -E pythonenv -q install -r requirements.txt

clean:
	rm Slidescript.tokens SlidescriptLexer.* SlidescriptParser.*
