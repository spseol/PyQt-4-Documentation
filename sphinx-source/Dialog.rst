Dialog
======

Nyní si ukážeme jak vytvářet dialogy mezi uživatelem a progrramem. Dialogy se vyplatí použivat na místech, kde potřebujeme upoutat pozornost uživatele na nějakou důležitou událost, například uzavření aplikace bez uložení vytvořeného obsahu. V PyQt jsou již předchystány standardní dialogy, ale mi si ukážeme jak vytvořit univerzální dialog pomocí QDialog. ::

 from PyQt4 import QtGui
 import sys
 class Ui(QtGui.QWidget):
    def __init__(self):
        super(Ui,self).__init__()
        self.setup()
    def setup(self):
        self.btn = QtGui.QPushButton("Exit",parent=self)
        self.btn.move(20,30)
        self.btn.resize(self.btn.sizeHint())
        self.btn.clicked.connect(self.exit_)
        self.setGeometry(200,300,400,500)
        self.show() 

Na začátku si vytvoříme jednoduché okno, které bude obsahovat tlačítko, které bude pří kliknutí otevírat dialog, o tom jestli si je uživatel jistý, že chce vypnout aplikaci. Poté již nastavíme oknu rozměr a zobrazíme toto okno. ::

 def exit_(self):
    self.create_dialog()
    if self.dialog.exec_():
        self.close()
    else:
        self.dialog.close()

Při zavolání metody exit_ se vytvoří metodou create_dialog() dialogové okno s názvem dialog. Z dialogu získáme návratovou hodnotu funkcí exec_ tato funkce může navracet hodnoty Accepted, což je logická jednička, nebo Rejected, což je logická nuda, nebo nějakou jinou hodnotu, například číslo zadané v dialogu uživatelem. V našem případě navrací tato metoda hodnotu Accepted, pokud si uživatel přeje okno vypnout, nebo Rejected, kdy se rozhodl okno nevypínat. Pří návratu Accepted, okno zavíráme pomocí metody close(). Při návratu hodnoty Rejected zavíráme tou samou metodou dialog. ::

 def create_dialog(self):
        self.dialog=QtGui.QDialog(parent=self)
        self.dialog.setModal(True)
        self.dialog.lbl = QtGui.QLabel("Jste si jsit ze chcete ukoncit aplikaci",parent= self.dialog)
        self.dialog.lbl.resize(self.dialog.lbl.sizeHint()) 
        self.dialog.btn = QtGui.QPushButton("Ano",parent=self.dialog)
        self.dialog.btn.resize(self.dialog.btn.sizeHint())
        self.dialog.btn.clicked.connect(self.dialog.accept)
        self.dialog.btn1= QtGui.QPushButton("Ne",parent=self.dialog)
        self.dialog.btn1.resize(self.dialog.btn1.sizeHint())
        self.dialog.btn1.clicked.connect(self.dialog.reject)
        grid=QtGui.QGridLayout()
        grid.addWidget(self.dialog.lbl,0,0,1,0)
        grid.addWidget(self.dialog.btn,1,0)
        grid.addWidget(self.dialog.btn1,1,1)
        self.dialog.setLayout(grid)

V metodě create_dialog si vytvoříme dialog pomocí konstruktoru QtGui.QDialog(parent), pokud nastavíme rodiče jako naše hlavní okno zobrazí se dialog nad naším hlavním okno. Pokud bychom toto neučinili museli bychom nastavi, kde chceme dialog zobrazi. Dialog funguje jako jakékoliv jiné okno, proto do něj můžeme přidávat ostatní widgety. Proto si vytvroříme label se zpravou pro uživatele a dvě tlačítka, která budou mít text „Ano“/„Ne“. Pokud stiskne uživatel tlačítko „Ano“, zavolá se slot dialog.accept, který nastaví návratovou hodnotu na hodnotu Accepted. Podobně navážeme tlačítko „Ne“ na slot dialog.reject, který nastaví návratovou hodnotu na Rejected. Poté vytvoříme rozvržení a metodou setLayout toto rozvržení nastavíme jako rozvžení dialogu. A tímto máme celou aplikaci funkční. Nyní si ukážeme ostatní důležité metody související s QDialog.

*	**dialog.reject()**

	*	schová dialogové okno a nastaví návratovou hodnotu na Rejected

*	**dialog.accept()**
	
	*	schová dialogové ono a nastaví návratovou hodnotu na Accepted

*	**dialog.done(int r)**
	
	*	zavře dialog a nastaví návratovou hodnotu na r, tato hodnota je navrácena metodou exec_

*	**dialog.exec_()**

	*	zobrazí dialog a posléze navrátí návratovou hodnotu.

*	**dialog.setResult(int result)**
	
	*	nastaví návratovou hodnotu na result, tato metoda se hodí pokud potřebujeme navracet z dialogu více hodnot. 
