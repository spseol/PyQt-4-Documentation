PushButton
===========
Tento widget je pravděpodobně nejvíce využívaný, protože se jím provádí mnoho ukonů, a to od posílání dat uživateli, 
po přesouvání se mezi formuláři a mnoho jiného. Je tedy důležité tento widget pochopit. Dále si ukážeme jak vytvořit tooltip 
pro zobrazení hodnotných informací pro uživatele.	::
	
	import sys
	from PyQt4 import QtGui,QtCore
	class Main_Window(QtGui.QWidget,):
		def __init__(self,):
			super(Main_Window,self).__init__()
			self.Setup_Ui()
		def Setup_Ui(self):
			QtGui.QToolTip.setFont(QtGui.QFont("Arial", 10))
			self.lbl= QtGui.QLabel(parent=self)

Jako obvykle si importujete potřebné moduly. Můžete si všimnout, že kromě obvyklého QtGui importujeme i modul QtCore, který obsahuje metody pro vytvoření vazeb jež reagují na akce uživatele.
Dále si v metodě Setup_Ui nastavíme font našeho tooltipu pomocí metody setToolTip(QFont). Objekt QFont se vytváří pomoci metody QFont(„jméno fontu, velikost fontu“). 
Potom vytvoříme objekt lbl pomocí konstruktoru QLabel(rodič). O tomto widgetu si řekneme něco více v příštích kapitolách. Pro nynější příklad tento widget použijeme pouze na zobrazení textu.	::

		btn= QtGui.QPushButton("klikni",self)
		btn.resize(btn.sizeHint())
		btn.setToolTip("tlacitko slouzici na zobrazeni textu")
		btn.clicked.connect(self.text)

Pomocí konstruktoru QPushButton(“text”,rodič) vytvoříme naše tlačítko, které 
nastavíme metodou setTooltip(“text”). Dále vytvoříme vazbu, která bude reagovat na kliknutí a vyvolá 
metodu text. Toto je podle mne nejdůležitější část kódu, proto aby se naše aplikace staly živějšími.	::

			grid=QtGui.QGridLayout()
			grid.addWidget(self.lbl,0,0)
			grid.addWidget(btn,1,0)
			self.setLayout(grid)
			self.setWindowTitle("Tlacitko")
			self.show()

V poslední části metody setup vytvoříme rozvržení a nastavíme je jako hlavní rozvržení pro naše okno. Nyní se podíváme na důležitější metodu, kterou je Text. Tato metoda zajišťuje zobrazení textu po kliknutí na tlačítko.	::
	
	def text(self):
		self.lbl.setText('klikl jste')
		self.lbl.resize(self.lbl.sizeHint())

Po kliknutí na tlačítko se provede vazba. Ta vyvolá funkci, která jako první provede nastavení textu do dříve vytvořené lbl pomocí metody setText(„text“). Dále je nutné nastavit velikost lbl widgetu, neboť bychom neviděli žádný text. Widgety totiž nemají žádnou velikost při jeho vytvoření. Toto provedeme pomocí metody resize, kterou jsme si již představili. 

.. image:: img/Tlacitko.png
.. image:: img/Tlacitko_klik.png



