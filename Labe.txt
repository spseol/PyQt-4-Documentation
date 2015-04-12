Label
=====

Label patří k důležitým widgetům. Umožňuje zobrazení textu, 
který je needitovatelný uživatelem. Jeho výhodou je velká možnost formátování textu. V následujícím příkladu si 
ukážeme pouze pár možností a také si představíme možnost nastavení tlačítka na dva stavy.	::

	import sys 
	from PyQt4 import QtGui,QtCore
	class Main_Window(QtGui.QWidget):
		def __init__(self):
			super(Main_Window,self).__init__()
			self.setup_ui()
		def setup(self):	
			self.lbl = QtGui.QLabel("hezky text",parent = self)
			self.lbl.resize(self.lbl.sizeHint())
			self.lbl.setAlignment(QtCore.Qt.AlignCenter)

První částí kódu se nebudeme moc zabývat a vrhneme se na metodu setup. Jako první si vytvoříme objekt lbl za pomoci konstuktoru QLabel(“text“,rodič). 
Stejně jako v minulém příkladu si musíme nastavit velikost lbl pomocí metody resize. A nastavíme jí zarovnání na střed jako v prvním příkladu.	::
	
		self.re_button = QtGui.QPushButton("red",parent=self)
      	self.re_button.setCheckable(True)
		self.re_button.resize(self.re_button.sizeHint())
       	self.re_button.clicked.connect(self.zmena)
		
		self.it_button = QtGui.QPushButton("kurziva",parent=self)
       	self.it_button.setCheckable(True)
		self.it_button.resize(self.it_button.sizeHint())
       	self.it_button.clicked.connect(self.zmena)
		
		self.tu_button = QtGui.QPushButton("tucne",parent=self)
       	self.tu_button.setCheckable(True)
       	self.tu_button.resize(self.tu_button.sizeHint())
       	self.tu_button.clicked.connect(self.zmena)
		
		self.po_button = QtGui.QPushButton("podtrhnute",parent=self)
       	self.po_button.setCheckable(True)
       	self.po_button.resize(self.po_button.sizeHint())
        self.po_button.clicked.connect(self.zmena)

V tomto kódu vytváříme několik tlačítek. Dále jim nastavujeme velikost a vytváříme u každého z nich vazbu na metodu změna. Tento postup je známý z předchozích příkladů. 
Každé tlačítko je nastavené metodou setCheckable(True/False) na to, aby bylo schopno přepínání mezi dvěmi stavy.	::
		
		grid=QtGui.QGridLayout()
       	grid.addWidget(self.lbl,0,0,1,0)
       	grid.addWidget(self.re_button,1,0,)
       	grid.addWidget(self.it_button,1,1,)
       	grid.addWidget(self.tu_button,2,0)
       	grid.addWidget(self.po_button,2,1)      
        self.setLayout(grid)
       	self.setWindowTitle("stisknute tlacitko")
       	self.show()

V poslední části metody setup jako obvykle nastavíme rozvržení našeho hlavního okna a okno zobrazíme.	::

	def zmena(self):
       	font= QtGui.QFont()
		if self.it_button.isChecked():
            font.setItalic(True)            
            self.lbl.setFont(font)
		else:
            font.setItalic(False)
            self.lbl.setFont(font)
		if self.tu_button.isChecked():
            font.setBold(True)            
            self.lbl.setFont(font)
     	else:
            font.setBold(False)
            self.lbl.setFont(font)   
		if self.po_button.isChecked():
            font.setUnderline(True)            
            self.lbl.setFont(font)
     	else:
            font.setUnderline(False)
            self.lbl.setFont(font)      
       	if self.re_button.isChecked():
            self.lbl.setStyleSheet("color:red")
		else:
            self.lbl.setStyleSheet("color:black")

V této metodě si jako první vytvoříme objekt font pomocí konstruktoru QFont. Tímto objektem budeme ovlivňovat vzhled textu našeho objektu lbl. V každé z podmínek se zeptáme, v jakém stavu je dané tlačítko. Toho dosáhneme pomocí metody isChecked. Podle toho nastavíme náš objekt lbl. Nyní si řekneme něco o metodách, kterými nastavujeme vzhled. 
SetItalic nastavuje, jestli bude text napsán kurzívou. SetBold nastavuje tučný text. SetUnderline nastavuje podtržení textu. V případě těchto metod nastavujeme tyto hodnoty objektu font, který poté použijeme jako parametr pro setFont(QFont) metody, kterou nastavíme vzhled fontu v objektu lbl. SetStyleSheet nastavuje mnoho věcí, neboť je založený na CSS, který můžete znát z kódování stránek a proto podporuje velmi podobnou syntaxi. V našem případě jim nastavujeme barvu. 
