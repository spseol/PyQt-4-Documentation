Rozvržení
=========

Rozvržení je velmi užitečná věc. Ta nám umožňuje vytvořit dobře vypadající grafické rozhraní bez velké práce. V PyQt4 existují dva manažery rozvržení, což jsou Grid a BoxLayout. Nyní se podíváme jak je vytvořit.

Grid
----

Grid je jeden z nejvíce užívaných rozvržení a to díky své jednoduchosti. 
Pracuje na základě sloupců a řádků do kterých umísťuje widgety. Díky této vlastnosti 
je pro programátora velmi snadné si představit jak bude výsledný program vypadat.	::

	from PyQt4 import QtGui
	import sys
	class Ui(QtGui.QWidget):
		def __init__(self):
			super(Ui,self).__init__()
			self.setup()
		def setup(self):
			cisla= (str(x) for x in range(1,17))
			pozice = [(x,y) for y in range(4) for x in range(4)]
			grid= QtGui.QGridLayout()
			j=0

První část kódu je stejná jako v prvním příkladu. Zajímavé věci se dějí až při vytváření pole čísla, které obsahuje po sobě jdoucí čísla v podobě řetězce. 
Je důležité, aby tyto čísla byla v řetězci, neboť jak si později ukážeme, tlačítka nejsou schopna přijmout čísla do svého názvu. Poté vytvoříme objekt grid za pomocí konstruktoru QGridLayout().	:: 
		
		
			for x in cisla:
				button= QtGui.QPushButton(x)
				grid.addWidget(button, pozice[j][1],pozice[j][0])
				j+=1
			self.move(200,300)
			self.setLayout(grid)
			self.show()

			
V cyklu for vytvoříme tlačítka, která umístíme pomocí metody addWidget (objekt, řádek, sloupec) do našeho rozvržení grid. 
Poté inkrementujeme j o jedna. Tato proměnná nám určuje počet již vytvořených tlačítek. Vytvoření tlačítek tímto způsobem je 
velmi výhodné, protože zpřehledňuje kód. Dále nastavíme našemu hlavnímu oknu rozvržení metodou setLayout(rozvržení) a potom jako obvykle okno zobrazíme.

.. image:: Grid.png
 
BoxLayout
---------------


Toto rozvržení je velmi užitečné, neboť graficky rozdělí widgety do logických skupin. Tato vlastnost je zejména využitelná pro widgety jako checkBox nebo RadioButton. Existují dva typy boyLayout a to vertikální a 
horizontální. Oba si nyní představíme.	::

	from PyQt4 import QtGui
	import sys
	class Ui(QtGui.QWidget):
		def __init__(self):
			super(Ui,self).__init__()
			self.setup()
		def setup(self):
			btn_ok_hor = QtGui.QPushButton("ok",)
			btn_ok_hor = QtGui.QPushButton("cancel",)
			hbox = QtGui.QHBoxLayout()
			hbox.addWidget(btn_ok_hor)
			hbox.addWidget(btn_cancel_hor)

První část kódu je stejná jako v předchozích příkladech a proto se jí nebudeme zabývat. Jako první si vytvoříme btn_ok_hor a btn_ok_hor za pomocí 
kostruktoru QPushButton(text). Blíže si povíme o tlačítkách v příštím příkladu. Poté vytváříme za pomoci kostruktoru QHBoxLayout objekt hbox. Do tohoto rozvržení nasledně 
umístíme naše tlačítka pomocí metody addWidget(objekt).	::
			
			btn_ok_ver = QtGui.QPushButton("ok",)
			btn_cancel_ver = QtGui.QPushButton("cancel",)
			vbox = QtGui.QVBoxLayout()
			vbox.addWidget(btn_ok_ver)
			vbox.addWidget(btn_cancel_ver)


Stejně jako pro HBoxLayout vytvoříme dvě tlačítka, která poté přidáme za pomocí metody addWidget do našeho rozvržení. 
Zde jde krásně vidět, jak si jsou VBoxLayout a HBoxLayout podobné, neboť podporují podobné metody.	::
		
			grid=QtGui.QGridLayout()
			grid.addLayout(vbox,0,0)
			grid.addLayout(hbox,3,3)
			self.setLayout(grid)
			self.move(200,300)
			self.show()   

V poslední části kódu si vytvoříme objekt grid, který je vytvořen konstruktorem QGridLayout. Do tohoto rozvržení potom umístíme hbox a vbox pomocí metody addLayout(rozvržení). Toto je nutné, neboť bychom nebyli schopni nastavit rozvržení pro hlavní okno, jelikož okno může mít pouze jedno rozvržení. Jako obvykle musíme okno zobrazit.

.. image:: BoxLayout.png