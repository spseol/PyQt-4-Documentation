Zdorojové kódy: 
:download:`Gryd.py <src/Grid.py>`,
:download:`BoxLayout.py <src/BoxLayout.py>`,
:download:`Grid_Presah.py <src/Grid_Presah.py>`.

Rozvržení
=========

Rozvržení je velmi užitečná věc. Ta nám umožňuje vytvořit dobře vypadající
grafické rozhraní bez velké práce. V PyQt4 existují dva manažery rozvržení, což
jsou **Grid** a **BoxLayout**. Nyní se podíváme jak je vytvořit.

Grid
----

Grid je jeden z nejvíce užívaných rozvržení a to díky své jednoduchosti.
Pracuje na základě sloupců a řádků do kterých umísťuje widgety. Díky této
vlastnosti je pro programátora velmi snadné si představit jak bude výsledný
program vypadat.    ::

    from PyQt4 import QtGui
    import sys
    class Ui(QtGui.QWidget):
        def __init__(self):
            super(Ui,self).__init__()
            self.setup()

První část kódu je stejná jako v prvním příkladu (:ref:`window`). Tlačítko se
vytvoří pomocí metody ``QPushButton()`` Je důležité, aby byl řetězec, neboť jak
si později ukážeme (:ref:`PushButton`), tlačítka nejsou schopna přijmout čísla
do svého názvu. Poté vytvoříme objekt ``grid`` za pomocí konstruktoru
``QGridLayout()``.  :: 
        
    def setup(self):
        grid = QtGui.QGridLayout()
        j = 1
        tlacitka = []
        for radek in range(4):
            for sloupec in range(5):
                tlacitka.append(QtGui.QPushButton(str(j)))
                grid.addWidget(tlacitka[-1], radek, sloupec)
                j += 1
        self.move(200, 300)
        self.setLayout(grid)
        self.show()
            
V zanořených cyklech ``for`` vytvoříme seznam tlačítek, která umístíme pomocí
metody ``addWidget(objekt, řádek, sloupec)`` do našeho rozvržení ``grid``. Poté
inkrementujeme j o jedna. Tato proměnná nám určuje počet již vytvořených
tlačítek. Vytvoření tlačítek tímto způsobem je velmi výhodné, protože
zpřehledňuje kód. Dále nastavíme našemu hlavnímu oknu rozvržení metodou
setLayout(rozvržení) a potom jako obvykle okno zobrazíme.

.. image:: img/Grid.png
 
BoxLayout
---------------

Toto rozvržení je velmi užitečné, neboť graficky rozdělí widgety do logických
skupin. Tato vlastnost je zejména využitelná pro widgety jako :ref:`CheckBox`
nebo :ref:`RadioButton`. Existují dva typy ``BoxLayout`` a to vertikální a
horizontální. Oba si nyní představíme.

Horizontální
^^^^^^^^^^^^^^^

::

    from PyQt4 import QtGui
    import sys
    class Ui(QtGui.QWidget):
        def __init__(self):
            super(Ui,self).__init__()
            self.setup()
        def setup(self):
            btn_ok_hor = QtGui.QPushButton("ok",)
            btn_cancel_hor = QtGui.QPushButton("cancel",)
            hbox = QtGui.QHBoxLayout()
            hbox.addWidget(btn_ok_hor)
            hbox.addWidget(btn_cancel_hor)

První část kódu je stejná jako v předchozích příkladech a proto se jí nebudeme
zabývat. Jako první si vytvoříme ``btn_ok_hor`` a ``btn_cancel_hor`` za pomocí
kostruktoru ``QPushButton(text)``. Blíže si povíme o tlačítkách v příštím
příkladu (:ref:`PushButton`). Poté vytváříme za pomoci kostruktoru
``QHBoxLayout`` objekt ``hbox``. Do tohoto rozvržení nasledně umístíme naše
tlačítka pomocí metody addWidget(objekt).

Vertikální
^^^^^^^^^^^^^^^

::
            
            btn_ok_ver = QtGui.QPushButton("ok",)
            btn_cancel_ver = QtGui.QPushButton("cancel",)
            vbox = QtGui.QVBoxLayout()
            vbox.addWidget(btn_ok_ver)
            vbox.addWidget(btn_cancel_ver)


Stejně jako pro ``HBoxLayout`` vytvoříme dvě tlačítka, která poté přidáme za
pomocí metody ``addWidget`` do našeho rozvržení. Zde jde krásně vidět, jak si
jsou ``VBoxLayout`` a ``HBoxLayout`` podobné, neboť podporují podobné metody.

Grid
^^^^^^^

::
        
            grid=QtGui.QGridLayout()
            grid.addLayout(vbox,0,0)
            grid.addLayout(hbox,3,3)
            self.setLayout(grid)
            self.move(200,300)
            self.show()   

V poslední části kódu si vytvoříme objekt grid, který je vytvořen konstruktorem
``QGridLayout``. Do tohoto rozvržení potom umístíme ``hbox`` a ``vbox`` pomocí
metody ``addLayout(rozvržení)``. Toto je nutné, neboť bychom nebyli schopni
nastavit rozvržení pro hlavní okno, jelikož okno může mít pouze jedno
rozvržení. Jako obvykle musíme okno zobrazit.

.. image:: img/BoxLayout.png

Zdorojové kódy
================

* :download:`Gryd.py <src/Grid.py>`.
* :download:`BoxLayout.py <src/BoxLayout.py>`.
* :download:`Grid_Presah.py <src/Grid_Presah.py>`.
