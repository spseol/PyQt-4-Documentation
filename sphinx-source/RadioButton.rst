RadioButton
===========

RadioButton je widget velmi podobný widgetu CheckBox. Rozdíl je v tom, že ze skupiny několika těchto widgetů můžete vybrat 
pouze jednu možnost. Proto se tento widget hodí pro zjišťování informací, které nemohou proběhnout zároveň (např. volba národnosti, pohlaví atd.).	::

	from PyQt4 import QtGui,QtCore
	import sys
	class Ui(QtGui.QWidget):
		def __init__(self):
			super(Ui,self).__init__()
			self.setup()
		def setup(self):     
			self.lbl = QtGui.QLabel("Hezky text", parent=self)
			self.lbl.resize(self.lbl.sizeHint())
			self.lbl.setAlignment(QtCore.Qt.AlignCenter)
			self.radio = QtGui.QRadioButton("cervena",parent=self)        
			self.radio.resize(self.radio.sizeHint())
			self.radio.setChecked(True)
			self.radio2 = QtGui.QRadioButton("modra",parent=self)        
			self.radio2.resize(self.radio2.sizeHint())       

Jak je možné vidět v první části kódu zůstává vše stejné a proto se zaměříme na metodu setup. V ní si vytvoříme objekt lbl, který se bude měnit v 
závislosti na zvoleném radioButtonu. Objekt radio a radio2 vytvoříme pomocí konstruktoru QRadioButton(“Text“, rodič). Jak si můžete všimnout, tak jsme použily metodu setChecked(True/False) na objekt radio. 
Tato metoda způsobí to, že tento widget zaškrtne. To je dobré v případě, že je nutné mít alespoň jednu z možností žaskrtnutou.	::
		
			self.color = QtGui.QButtonGroup(parent=self)
			self.color.addButton(self.radio)
			self.color.addButton(self.radio2)
			self.color.buttonClicked.connect(self.change)

Nedílnou součástí vytváření radioButton sestav je widget ButtonGroup, který zajistí aby byl v jedné skupině zaškrtnut pouze 
jeden radioButton. ButtonGroup vytvoříme pomocí konstruktoru QButtonGroup(rodič), následně přidáme vytvořené radioButtony pomocí metody addButton(název). 
Jako poslední vytvoříme vazbu po kliknutí na tlačítko, která zavolá funkci change.	::
			
			self.radio3 = QtGui.QRadioButton("kurziva",parent=self)        
			self.radio3.resize(self.radio3.sizeHint())
			self.radio3.setChecked(True)                  
			self.radio4 = QtGui.QRadioButton("tucne",parent=self)        
			self.radio4.resize(self.radio4.sizeHint())
			self.font = QtGui.QButtonGroup(parent=self)
			self.font.addButton(self.radio3)
			self.font.addButton(self.radio4)
			self.font.buttonClicked.connect(self.change)       
			grid=QtGui.QGridLayout()
			grid.addWidget(self.lbl,0,0,1,0)
			grid.addWidget(self.radio,1,0)
			grid.addWidget(self.radio2,1,1)        
			grid.addWidget(self.radio3,2,0)
			grid.addWidget(self.radio4,2,1)
			self.setLayout(grid)
			self.show()

V poslední části metody setup vytvoříme dva radioButtony. Toto provedeme stejným způsobem, jaký jsme si již ukazovali. Dále musíme všechny widgety umístit do rozvržení grid a toto rozvržení nastavíme oknu a okno zobrazíme.	::
		
		def change(self):
			font= QtGui.QFont()
			if self.color.checkedId()==self.color.id(self.radio):
				self.lbl.setStyleSheet("color:red")
			else:
				self.lbl.setStyleSheet("color:blue") 
			if self.font.checkedId()==self.font.id(self.radio3):
				font.setItalic(True)   
				self.lbl.setFont(font)
			else:
				font.setBold(True)
				self.lbl.setFont(font)

Metoda change obstarává změnu textu v objektu lbl podle zaškrtnutého radioButtonu. Z tohoto důvodu si vytvoříme objekt font, kterým budeme ovlivňovat text v objektu lbl. V podmínkách se ptáme metodou checkedID, která nám řekne id tlačítka v buttonGroup jež je zaškrtnuto. Tuto informaci porovnáme následně s id radioButtonu, které získáme metodou id(jméno objektu). A dále pak nastavíme upravení textu.

.. image:: img/Radio.png
.. image:: img/radio2.png