LineEdit
=============

V následující kapitole si ukážeme jak pracovat s LineEdit. LineEdit je velmi důležitým widgetem, neboť umožňuje uživateli vkládat textové řetězce do naší aplikace, jako takové se proto hodí pro nejrůznější účely, jako zadávání hesla a podobně. ::

    from PyQt4 import QtGui, QtCore
    import sys
    class Ui(QtGui.QWidget,):
      def __init__(self):
        super(Ui,self).__init__()
        self.dict={}        
        self.setup()
        
      def setup(self):
        self.font = QtGui.QFont()
        self.font.setItalic(True)
        self.form_name = QtGui.QLineEdit("Jmeno",parent=self,)        
        self.form_name.setFont(self.font)
        self.form_name.resize(100,20)

V první části kódu si jako obvykle implementujeme nezbytné moduly. V metodě setup si vytvoříme QFont, což je objekt písma z PyQt knihovny. Tento objekt má mnoho druhů nastavení a používáme ho pro nastavení písma v ostatních widgetech. My budeme chtít text psaný kurzívou, a proto nám stačí písmo nastavit metodou setItalic(bool). Poté si vytvoříme lineEdit pomocí konstruktoru QtGui.QLineEdit(text,rodič) a takto vytvořenému lineEditu nastavíme písmo pomocí metody setFont(QFont) a nastavíme pevnou velikost lineEditu. ::

        self.form_pass = QtGui.QLineEdit("Heslo",parent=self,)
        self.form_pass.setEchoMode(2)
        self.form_pass.resize(100,20)
        self.btn_prihlas = QtGui.QPushButton("potvrdit",parent=self,)
        self.btn_prihlas.resize(self.btn_prihlas.sizeHint())
        self.btn_prihlas.clicked.connect(self.prihlas)
        self.btn= QtGui.QPushButton("nemate registraci",parent=self,)
        self.btn.resize(self.btn.sizeHint())
        self.btn.clicked.connect(self.registrace)

Poté si vytvoříme další lineEdit, do kterého bude uživatel zadávat heslo, protože heslo musí zůstat tajné musíme nastavit změnu znaků při zadávání hesla. Toho docílíme metodou setEchoMode(EchoMode). Typ překrití můžeme nastavit číselnou hodnotou. Číselná hodnota 2 nám zobrazí klasické heslo. Ostatní druhy nastavení najdete na konci kapitoly. Poté vytvoříme tlačítko pro přihlášení, které bude pří kliknutí spouštět slot self.prihlas a další tlačítko pro zaregistrování uživatele. Toto tlačítko bude po kliknutí spouštět slot s názvem self.registrace. ::

        self.lbl = QtGui.QLabel(parent=self)
        self.lbl.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl.setMinimumSize(220, 13)
        grid=QtGui.QGridLayout()
        grid.addWidget(self.form_name,0,0,1,0)
        grid.addWidget(self.form_pass,1,0,1,0)
        grid.addWidget(self.btn_prihlas,2,0)
        grid.addWidget(self.btn,2,1)      
        grid.addWidget(self.lbl,3,0,1,0)         
        self.setLayout(grid)
        self.show()

V poslední části metody setup si vytvoříme label, do kterého budeme vypisovat informace o úspěšnosti přihlášení. A všechny widgety umístíme do rozvržení. A zobrazíme celé okno. ::

 def prihlas(self):
   if self.form_name.text() in self.dict.keys() and self.form_pass.text()==self.dict[self.form_name.text()]:
       self.lbl.setText("Byli jste uspesne prihlaseni")
       self.lbl.resize(self.lbl.sizeHint())
   else:
       self.lbl.setText("Prihlaseni se nezdarilo heslo nebo jmeno se lisi")
       self.lbl.resize(self.lbl.sizeHint())

V této metodě zjišťujeme, jestli text z lineEditu se jménem máme ve slovníku hesel a zároveň jestli odpovídá heslo heslu uloženém pro dané jméno. Jak si můžete, všimnou text z lineEditu získáváme jednoduchou metodou text, která nám vrátí text obsažený v lineEditu. Pokud je přihlášení úspěšné, informujeme uživatele o úspěchu. Jinak zobrazíme chybovou hlášku s nezdařeným přihlášením. ::

   def registrace(self):
        okenko=popup()
        self.dict[okenko.line_name.text()]= okenko.line_pass.text()

V této metodě si inicializujeme třídu s naším dialogem, ze kterého získáme heslo pro nového uživatele. Heslo a jméno získáme metodou text z lineEditů, které se nacházejí v dialogovém okně. :: 

 class popup(QtGui.QDialog,):
    def __init__(self):
        super(popup,self).__init__()
        self.setup()
    def setup(self,):
        self.line_name = QtGui.QLineEdit("Jmeno",parent=self)
        self.line_name.resize(100,20
        self.line_pass = QtGui.QLineEdit("Heslo",parent=self)
        self.line_pass.resize(100,20)
        self.line_pass.setEchoMode(2)
        self.btn_potvrdit = QtGui.QPushButton("potvrdit",parent=self)
        self.btn_potvrdit.resize(self.btn_potvrdit.sizeHint())
        self.btn_potvrdit.clicked.connect(self.close)
        grid=QtGui.QGridLayout()
        grid.addWidget(self.line_name,0,0,1,0)
        grid.addWidget(self.line_pass,1,0,1,0)
        grid.addWidget(self.btn_potvrdit,2,0)
        self.setLayout(grid)
        self.exec_()

Tato třída, která reprezentuje dialogové okno, dědí z QDialog a to proto, abychom mohli používat metody spojené s dialogem a proto, aby se vůbec námi vytvořené okno chovalo jako dialog. Tento dialog je velmi podobný oknu naší hlavní aplikace a proto obsahuje dva lineEdity. Jeden lineEdit má změněné znaky zadávání pomocí metody setEchomMode. Po kliknutí na tlačítko se náš dialog uzavře.

* **lineEdit.clear()**

	* Vymaže obsah lineEditu. Je možné použít místo lineEdit(““)

* **lineEdit.setPlaceholderText(self,string)**

	* Nastaví šedý text, který je po kliknutí automaticky vymazán.

* **lineEdit.setText(string)**

	* nastaví text do lineEditu

* **lineEdit.text()**

	* Vrátí text napsaný v lineEditu

.. image:: img/13.png