Celý zdorojový kód: :download:`hello_world.py <src/hello_world.py>`.

.. _window:

===============
Vytvoření okna
===============

V prvním příkladu si ukážeme jak vytvořit základní okno, nastavení titulku a
ikony okna a přidám i pár tipů k přehlednosti kódu.	::

	import sys
	from PyQt4 import QtGui

Importování všech nezbytných modulů pro naše okno. Neimportujeme všechny třídy
PyQt4, neboť bychom se ztratili v množství tříd a náš kód by byl úplně
nepřehledný.	::	


	class main_window(QtGui.QWidget):
		def __init__(self):
			super(main_window,self).__init__()
			self.setupUi()

			
Jako první vytváříme třídu ``main_window``, která dědí metody z třídy
``QWidget``. V této třídě jsou umístěny metody pro práci s velikostí widgetů,
posouvání widgetů a mnoho dalších věcí. Dále vytvoříme metodu ``__init__()``,
která se vždy spustí při inicializaci objektu. Funkce ``super()`` nám umožňuje
inicializovat všechny třídy, ze kterých jsme dědily. To je dobré v tom, že
nemusíme zdlouhavě vypisovat všechny rodiče a inicializovat je. Poté se spouští
metoda ``setupUi()``, která nám vytvoří samotné okno.	::
	

	def setupUi(self):
		self.move(300,200)
		self.resize(300,150)
		self.setWindowTitle("Hello world")
		self.setWindowIcon(QtGui.QIcon("world.jpg"))
		self.show()

		
Funkce ``move(pozice x, pozice y)`` nám přesune okno na dané souřadnice. Ty se
počítají od pravého horního rohu obrazovky. 

Funkce ``resize(pozice x, pozice y)``
nám umožnuje nastavovat velikost okna. Jak vidíte move a resize jsou si velmi
podobné. Z toho nám může být jasné, že zvětšení okna se bere od pravého horního
rohu okna. Funkce ``resize`` i ``move`` se dají využít u všech ostatních widgetů a
provádějí stejnou věc. 

``SetWindowTitle(string)`` nastavuje titulek okna.

``SetWindowIcon(QIcon)`` vytváří ikonu okna podle objektu ``QIcon``. Tento objekt
vytovoříme pomocí funkce ``QIcon(cesta k obrazku)`` umístěné v modulu ``QtGui``. 

Jako poslední funkci použijeme ``show()``, která nám zobrazí celé okno na
obrazovku. Je důležité, abyste funkci show použily až po vytvoření osatních
widgetů, jinak se vám widgety nezobrazí. ::

    app = QtGui.QApplication(sys.argv)
    okno = main_window()
    sys.exit(app.exec_())
	
A nyní se dostáváme k části, kdy inicializujeme celou naši třídu, která vytváří
okno. Jako první si vytvoříme objekt ``QApplication(seznam_parametru)``, který
vytváří hlavní smyčku programu, v níž se sbírají informace o tom, jestli bylo
stisknuto tlačítko atd. ``Exit()`` nám zajistí to, že se okno korektně vypne při
opuštění hlavní smyčky. Argumentem je stav jestli je aplikace stalé funkční.
Ten získáme funkcí ``exec_()``.

.. image:: img/okna.png

-------------------------------------------

Celý zdorojový kód: :download:`hello_world.py <src/hello_world.py>`.
