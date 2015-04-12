Slider
======

V této kapitole si ukážeme, velmi užitečný  grafický prvek zvaný slider. Tento prvek se hodí k zadávání hodnot z souvislého intervalu a také tam, kde potřebujeme okamžitou odezvu. Toho předurčuje jako vhodný widget pro práci s barvami nebo pro nastavovaní rychlosti myšy. Mimo jiné si v této kapitole ukážeme jak jde efektivně detekovat místo na kterém chceme vykreslit určitý objekt. ::

 from PyQt4 import QtGui,QtCore
 import sys
 class changer(QtGui.QWidget):
    def __init__(self):
        super(changer,self).__init__()
        self.painter=QtGui.QPainter()
        self.setup()
    
    def setup(self):
        self.grid=QtGui.QGridLayout()
        self.rect=QtGui.QSpacerItem(100,50,)
       	
	self.red=QtGui.QLabel(self)
        self.red.setNum(0)
        self.grid.addWidget(self.red,2,0)
        
        self.blue=QtGui.QLabel(self)
        self.blue.setNum(0)
        self.grid.addWidget(self.blue,2,2)
        
        self.green=QtGui.QLabel(self)
        self.green.setNum(0)
        self.grid.addWidget(self.green,2,1)   

První část kódu je klasické importování knihoven a nastavení potřebných nezbytností. První důležitou věcí, které je dobré si všimnout, je vytvoření spaceru. Spacer je neviditelná widget, který nám umožnuje vytvořit rozestup o požadované velikosti mezi widgety. V našem případě ho používáme proto, abychom byli schopni kreslit na předem určené místo. Poté si vytvoříme tři label widgety, které nám budou ukazovat aktualní hodnoty slideru. Toto je důležité, neboť samotná slider nemá žádnou grafickou indikaci hodnoty. ::

        self.slider=QtGui.QSlider(parent=self)
        self.slider.setMaximum(255)
        self.slider.setMinimum(0)
        self.slider.valueChanged.connect(self.paintEvent)
        self.slider.valueChanged.connect(self.red.setNum)
        self.slider2=QtGui.QSlider(parent=self)
        self.slider2.setMaximum(255)
        self.slider2.setMinimum(0)
        self.slider2.valueChanged.connect(self.paintEvent)
        self.slider2.valueChanged.connect(self.green.setNum)
        self.slider3=QtGui.QSlider(parent=self)
        self.slider3.setMaximum(255)
        self.slider3.setMinimum(0)
        self.slider3.valueChanged.connect(self.paintEvent)
        self.slider3.valueChanged.connect(self.blue.setNum)
                
Nyní si vytvoříme naše tři slidery a to pomocí třídy QSlider, poté pomocí metody setMaximum nastavíme horní mez intervalu. Podbně nastavíme i hodnotu dolní meze a to metodou setMinimum. Obě tyto metody příjmaji celo číselné hodnoty. Pomocí signálu valueChanged, který se provede při zmněně hodnoty slideru, napojíme dva sloty a to self.paintEvent, který nám zajistí přebarvení obdelníku na danou rgb hodnotu, a self.label.setNum, který nám zajistí zmněnu hodnoty label dané barvy na aktuální hodnotu slideru. Tímto způsobem vytvoříme všechny tři slidery. ::
     
        self.grid.addWidget(self.slider,0,0)
        self.grid.addWidget(self.slider2,0,1)
        self.grid.addWidget(self.slider3,0,2)
        self.grid.addItem(QtGui.QSpacerItem(0,10),1,1)
        self.grid.addItem(QtGui.QSpacerItem(0,10),4,1)
        self.grid.addItem(self.rect,5,0,1,3)
        self.setLayout(self.grid)
        self.show()

Zde si všechny widgety dáme do rozvžení, které jsme si na žačátku vytvoříly a toto rozvržení nastvíme jako hlavní rozvržení okna. ::

 def paintEvent(self,e):
        self.painter.begin(self)
        pen=QtGui.QPen()
        pen.setStyle(QtCore.Qt.NoPen)
        self.painter.setPen(pen)
        self.painter.setBrush(QtGui.QColor(self.slider.value(),self.slider2.value(),self.slider3.value()))
        self.painter.drawRect(self.rect.geometry())
        self.painter.end()        
        self.update()

Podobně jako v minulé kapitole si reimplementujeme metodu paintEvent v ní začneme kreslení metodou self.painter.begin. Poté si vytvoříme pero, které bude neviditelné a předáme ho painteru. To nám zajistí, že vytvořený obdelník nebude mít rámeček. Poté si nastavíme štětec s barvou. Barvu nastavíme třídou QtGui.QColor. Parametry této metody jsou hodnoty ze slideru v pořadí červená, zelená a modrá. Díky použití metody paintEvent se nám obdelník vytvoří již s oknem a nemusíme čekat na to, až užívatel potáhne sliderem. Nyní si ukážeme, přehled užitečných metod a signálů pro práci se sliderem. 

*	**setMinimum(int min)**

	*	Nastaví nejmenší možnou hodnotu slideru.

*	**setMaximum(int min)**
	
	*	Nastaví největší možnou hodnotu slideru.

*	**setValue(int value)**

	*	Nastaví slider na hodnotu v rozsahu od minima po maximum. Hodí se pro první nastavení hodnoty, třeba na často vybíranou hodnotu.

*	**setSingleStep(int value)**

	*	nastaví hodnotu o kterou se při jednom kroku změní hodnota slideru.

*	**setRange(int min,int max)**

	*	Nastaví rozsah pro slider, funguje stejně jako setMinimum a setMaximum.

.. image:: 16.png