Slidescript
===========

Slidescript ist eine Tabellenkalkulation ohne die Tabellen, oder - technischer
ausgedrückt - eine [deklarative][1] [Domain Specific Language (DSL)][2].

[1]: http://en.wikipedia.org/wiki/Declarative_programming
[2]: http://en.wikipedia.org/wiki/Domain-specific_language


Einführung
----------

Man beschreibt in Slidescript einfache mathematische Zusammenhänge. In der
Programmdatei können Beschreibende Texte und Formeln gemischt werden.
Im folgenden eine Beispiel-Formel:

    AnzahlBesucher = 500
    VerzehrProBesucher = 20
    VerzehrKosten = AnzahlBesucher * VerzehrProBesucher

Mit dem Slidescript-Compiler kann man nun ein solches Programm verschiedene
formate umwandeln. Im einfachsten Fall können die Variablen aufgelößt und
ausgegeben werden.

    $ ./slidescript.py examples/simple.slide --resolved
        VerzehrKosten = 10000.0
        VerzehrProBesucher = 20.0
        AnzahlBesucher = 500.0

Wenn nicht alle Varialben komplett aufgelösst werden können, wird bis zu dem
Punkt aufgelößt, bei dem Informationen Fehlen und dieser Stand ausgegeben.
Formeln werden dabei in Stack Notation ausgegeben.

    VerzehrProBesucher = 20
    VerzehrKosten = AnzahlBesucher * VerzehrProBesucher

Die obige Datei führt zu folgender Ausgabe:

    $ ./slidescript.py examples/incomplete.slide --resolved
        VerzehrKosten = ('*', u'AnzahlBesucher', 20.0)
        VerzehrProBesucher = 20.0
        AnzahlBesucher = ?Unknown

Der Slidescript Compiler kann die Programme in zahlreiche andere Formate
umwandeln (oder er wird es bald können). Folgende Formate kommen in Frage:

* Graphviz DOT
* XLS (Excel) Kalkulationsblatt
* Javascript und HTML (mit jQuery)
* Python Klasse
* LaTeX (TBD)


Ausgabeformate
--------------

### Graphviz DOT

Der Slidescript Compiler kann eine Datei erstellen, die mit
[Graphviz][graphviz] die Abhaengigkeiten der verschiedenen Variablen
visualisieren kann. Das Ergebnis von [party.slide][party.slide] sieht dann etwas so aus:

![Dependency graph](http://static.23.nu/md/Pictures/ZZ74E8162F.png)

[graphviz]: http://www.graphviz.org/
[party.slide]: http://github.com/mdornseif/Slidescript/blob/master/examples/party.slide
