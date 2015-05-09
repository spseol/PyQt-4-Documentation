Signály a sloty
================

V této kapitole se budeme zabývat velmi důležitou mechanikou knihovny PyQt4 a
to signály a sloty. Tato mechanika slouží pro zachicení událostí a na základě
nich provedení požadovaných operací. 

Oproti jiným knihovnám pro grafické rozhraní je PyQt výjmečné použitím signálu
a slotů. Rozdíl oproti callback funkcím v jiných knihovnách musí mít signál i
slot stejnou návratovou hodnotu. Toto je důležité v Qt, jehož je PyQt
nástavbou, ale v PyQt se tím prakticky nemusíme zabývat, neboť Python nemá jako
jiné jazyky pevně stanovenou navratovou hodnotu funkce.

Signály
-------

Signál je vyvolán při každé událostí, způsobené uživatelem nebo nějakým pro nás
zajímavým jevem. Například výpadek připojení k internetu nebo stisknutí
tlačítka.  Po vyvovolání  signálu jsou vykonány sloty, pokud je k jednomu
signálu připojeno více slotů jsou sloty prováděny postupně v pořadí v jakém
byli připojeny k signálu.

V Pyqt je nám k dispozici velké mmožství přednastavených signálu, s těmito
signály si ve většině případů vystačíme, ale máme možnost si vytvořit vlasní
signal. Užitečné signály obsažené v Pyqt4 jsou.

**widget.clicked**
    pokud bylo kliknuto na widget, spustí se přiřazený slot, použití zejména
    pro QButton, ale lze použít i na ostatní widgety.
**widget.released**
    pokud bylo po kliknutí na widget uvolněno tlačítko, spustí se přířazený
    slot, použití zejména pro QButton, ale lze použít i na ostatní widgety.
**widget.pressed**
    pokud bylo kliknuto na widget, spustí se přířazený slot, použití zejména
    pro QButton, ale lze použít i na ostatní widgety.
**widget.valueChanged**
    použití pro QSpinBox nebo QSlider, pokud se změní hodnota widgetu,
    spustí se přiřazený slot.
**widget.stateChanged**
    použití pro QCheckBox, pokud se změní stav, spustí se přiřazený slot.
    Změna stavu znamená přepnutí QCheckBoxu.
**widget.textChanged**
	použití pro QLineEdit, pokud se změní text, spustí se přiřazený slot.

Neboť by bylo zdlouhavé vypisovat všechny signály v knihovně PyQt, existuje
způsob jak zjistit všechny signály pro jednotlivé widgety a to pomocí skriptu,
který vypíše všechny signály do textového souboru s názvem widgetu, který k
danému slotu náleží. Poté je již snadné si daný signál prostudovat v oficiální
dokumentaci PyQt.	::


	from PyQt4 import QtGui, QtCore
	import inspect
	file = open("kwan.txt","w")
	for name in dir(QtGui):
		obj = getattr(QtGui, name)
		if inspect.isclass(obj) and issubclass(obj, QtCore.QObject):
			for name2 in dir(obj):
				obj2 = getattr(obj, name2)
				if isinstance(obj2, QtCore.pyqtSignal):
					file.write(str(name)+" "+str(name2)+"\n")


	
	
Vázání signálů
^^^^^^^^^^^^^^

Poté co jsme si řekli, co to jsou signály, je důležité se naučit jak tyto
signály napojit na widgety a tím vytvořit vazby, které umožní uživateli
komunikovat s naší aplikací. V PyQt4 jsou dvě možností jak tyto vazby vytvářet
a to „nový“ a „starý“ styl. Jediný rozdíl mezi těmito styly je v tom, že nový
styl je více pythonovější  a také je kratší na zápis. A nyní si ukážeme jak
tyto vazby vytvořit.

Starý styl	
^^^^^^^^^^

.. code-block:: python

    slider = QtGui.QSlider()
    QtCore.QObject.connect(slider, QtCore.SIGNAL("valueChanged()"), change)
    def change(num):
        print "slider ma hodnotu ", num

V tom to příkladu na vytvoření vazby si vytvoříme slider, které napojíme pomocí
metody ``connect``, která se nachází ve třídě ``QtCore.QObject``. Tato metoda
přijímá jako argumenty widget, který má vytvořit vazbu, signál, který ma danou
vazbu vytvořit. Signál musí být specifikován metodou ``SIGNAL``,tato metoda
přijímá řetězec s názvem signálu. Posledním parametrem metody connect je
funkce, která se zavolá po provedení daného signálu. Je dobré si všimnout,
že signál posílá při změně hodnoty tuto změněnou hodnotu našemu slotu.
	
Metoda connect má několik možných signatur, které se pouze drobně liší. Tyto signatury si nyní blíže představíme.

 
**connect(sender,SIGNAL(),receiver,SLOT())** 
    Vytvoří vazbu mezi widgetem ``sender`` a widgetem ``receiver``. Důležité
    je, že SLOT musí náležet widgetu ``receiver``. Tato signatůra se hodí
    například pro vytvoření ``Slideru``, jehož hodnota se bude zobrazovat v
    ``Label``.
**connect(sender,SIGNAL(),callable)**
    Podobně jako předchozí signatura vytvoří vazbu z widgetu ``sender``
    signálem na slot se jménem ``callable``. Callable je jakákoliv funkce nebo
    metoda v Pythonu.

**connect(sender,SIGNAL(),SLOT())**
    Zkrácený zápis pro ``connect(sender,SIGNAL(),self,SLOT())``. To znamená,
    že vytvoří vazbu na naše okno a ne na nějaký blíže specifikovaný widget.

Nový styl	
^^^^^^^^^
::

	slider = QtGui.QSlider()
	slider.valueChanged.connect(change)
	
	def change(num):
	 print "hodnota slideru je ", num

Podobně jako v minulém příkladu si vytvoříme slider, z kterého vedeme vazbu na
slot change. Jak je jistě patrné tento způsob je přehlednější, lépe čitelný a
také se více podobá syntaxi Pythonu. Celá vazba vzniká zavoláním signálu
``valueChanged`` na slider a připojení pomocí metody ``connect``, která přijímá
pythonovkskou funkci.
 

Vytváření signálů
^^^^^^^^^^^^^^^^^

Přesto, že PyQt obsahuje obsáhlou sbírku již vytvořených signálu, tak se někdy
hodí si vytvořit vlastní signál se specifickými parametry, které přesně splňují
naše požadavky. Vlastní signály jsou zejména užitečné pro námi vytvořené
widgety.	::

	class Ui(QtGui.QWidget,QtCore.QObject,):
		right=QtCore.pyqtSignal(str)
		left=QtCore.pyqtSignal(str)
		def __init__(self):
			super(Ui,self).__init__()
			self.setup()

Jako první si vytvoříme třídu reprezentující naše grafické rozhraní. V proměnné
``right`` si vytvoříme signál, který bude odesílat textovou hodnotu. Stejným
způsobem vytvoříme i druhý signál ``left``. Je důležité si všimnout, že **signály
definujeme v těle třídy a ne v metodě**. A také toho, že signály by měly být
vytvářeny pouze ve třídách dědících z ``QtCore.QObject``.	::

	def setup(self):
	   self.setGeometry(100,100,100,100)
	   self.rect=QtGui.QLabel(parent=self)
	   self.rect.resize(50,50)
	   self.right.connect(self.text)
	   self.left.connect(self.text)
	   self.show()

V této části si nastavíme velikost okna a vytvoříme Label do, kterého posléze
budeme zapisovat, zda byl proveden náš signál. Poté si vytvoříme dvě vazby na
slot ``self.text``, a to za pomoci naších signálů. Na tom to je také dobře
vidět, že slot může obsluhovat více signálů. ::

    def text(self,e):
        self.rect.setText(e)

    def keyPressEvent(self,e):
        if e.key()== 65:
            self.right.emit("right")
        if e.key()== 67:
            self.left.emit("left")
			
Nyní se dostáváme, k nejdůležitější častí kódu, a to z toho důvodu, že nám
umožní spustit náš signál. V metodě text změníme text naší Label. Nejdůlžitější
metodou celého kódu je keyPressEvent a to z důvodu, že se spustí při každém
zmáčknutí tlačítka. Toto tlačítko můžeme zjistit pomocí parametru e na který
zavoláme metodu key, která nám vrátí číslo tlačítka, které spustilo tuto
metodu. Díky tomuto si můžeme určit při jakém stisknutí tlačítka se spustí náš
signál. Spuštění signálu způsobíme zavoláním metody emit na náš signál, do
metody může odeslat parametry odpovídající signatůře našeho signálu, v našem
případě to je string. Signály jde spouštět mnoha různými eventy, nebo i jinými
způsoby. Stačí pouze kreativně vytvořit spojení.
 
Sloty
-------

Slotem může být jakákoliv funkce nebo metoda v Pythonu. Slot je proveden v
případě, když je signál vázaný na tento slot emitován. Na rozdíl od Qt knihovny
nemusíme v PyQt sloty přímo deklarovat, přesto tuto možnost máme. Přestože
knihovna Qt musí mít definován návratový datový typ, v PyQt toto není potřeba a
to z toho důvodu, že Python nemá stanovený návratový datový typ. Přesto je i v
PyQt možnost jak nastavit návratový datový typ slot a to si nyní si ukážeme.


PyqtSlot dekorátor 
^^^^^^^^^^^^^^^^^^^^

K definování návratového datového typu slotu se používá dekorátoru
``pyqtSlot``. Přestože, PyQt knihovna umožňuje použít jako slot všechny funkce
nebo metody, hodí se v případech, kdy se potýkáme s nedostatkem paměti v
systému. Neboť sloty dekorované ``pyqtSlot`` dekorátorem potřebují méně paměti
a také se rychleji spouští. Toto je způsobeno tím, že dekorátor poskytuje slotu
C++ signaturu. ::

 from PyQt4.QtCore import QObject, pyqtSlot
 class Foo(QObject):
    @pyqtSlot()
    def foo(self):
        """ C++: void foo() """
    @pyqtSlot(int, str)
    def foo(self, arg1, arg2):
        """ C++: void foo(int, QString) """
    @pyqtSlot(int, name='bar')
    def foo(self, arg1):
        """ C++: void bar(int) """
    @pyqtSlot(int, result=int)
    def foo(self, arg1):
        """ C++: int foo(int) """
    @pyqtSlot(int, QObject)
    def foo(self, arg1):
        """ C++: int foo(int, QObject *) """

Tímto dekorátorem můžeme také nastavit, která ze signatur signálu má být k
danému slotu přípojena. Toto se hodí například pro zaškrtávací tlačítko, které
má signál clicked s dvěma signaturami, jedna, která po kliknutí vrátí hodnotu
zaškrtnutí tlačíka a druhá, která nic nenavrací, pokud by nás zajímala pouze
druhá signatura, můžeme použít tuto konstrukci. ::

	@pyqtSlot(bool)
	def on_spinbox_valueChanged(self, i):
		# i bude bool hodnota
		pass
