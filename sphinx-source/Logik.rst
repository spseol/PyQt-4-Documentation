Logik
=====

Nyní, když již umíme základy PyQt, si ukážeme, jak naprogramovat jednoduchou hru Logik. K vytvoření této aplikace budete potřebovat základní znalosti práce s tlačítky a popisky. 

Logik je logická hra , jejímž cílem je uhádnutí hádanky složené z pěti různých barev. Hra musí umožňovat zobrazení předchozích tahů hráče a také musí zobrazovat počet uhádnutých barev a pozic. Hráč má na uhádnutí pouze 10 pokusů . Celá hra bude vytvořena pouze PyQt4. Nyní si ukážeme jak nato. ::

 class Ui(QtGui.QWidget):
    
   def __init__(self):
        super(Ui,self).__init__()
        self.barvy=["70,192,255","252,87,52","238,224,66",
                     "31,133,70","119,73,17","255,49,196","245,189,101")
        self.setup()

V první části kódu si vytvoříme třídu Ui, ve které si budeme vytvářet hrací okno a budeme také provádět logiku hry. Pravděpodobně by bylo lepší si rozdělit hru a gui do dvou oddělených tříd, ale pro náš tutoriál bude stačit jedna třída. V metodě __init__ si, kromě zavolání metody self.setup(), vytvoříme pole barev, které jsou textové řetězce ve formátu RGB. Tyto barvy budeme používat pro barvení tlačítek pomoci metody setStyleSheet. ::

  def new(self):
        self.pokusy=0
        self.hadanka=random.sample(self.barvy,5)

Tato krátká metoda nám vytvoří promněné pokusy a vytvoří novou hádanku náhodnou hadanku. Hádanku generujeme funkcí random.sample(pole,počet výběrů). Výledkem této funkce je pole obsahující pět unikátních kódů barev. ::

 def setup(self):
        self.widgets=[[],[],[],[],[],[],[],[],[],[],[],[]]
        self.new()
        grid=QtGui.QGridLayout()
        self.lbl_logik=QtGui.QLabel(self)
        self.lbl_logik.setText("Logik")
        self.lbl_logik.resize(self.lbl_logik.sizeHint())

V první části metody setup si vytvoříme dvojrozmněrné pole widgets. Do tohoto pole budeme posléze umisťovat reference na prvky rozhraní, které budeme při každé nové hře vyresetovávat. Poté vytvoříme popisky pro hru a nastavíme jim velikost způsobem jakým jsme si ukazovali v příkladu pro label. ::
        
         spacer=QtGui.QSpacerItem(10,0)
         grid.addItem(spacer,0,5,13,1)
         self.lbl_barvy=QtGui.QLabel(self)
         self.lbl_barvy.setText("Barvy/Pozice")
         self.lbl_barvy.resize(self.lbl_barvy.sizeHint())
         grid.addWidget(self.lbl_barvy,0,6,1,1)

Aby měla naše aplikace hezký vzhled a nic se nikde nelepilo použijeme widget zvaný QSpacerItem, tetnto widget vytvoříme pomocí QtGui.QSpacerItem(šířka,délka). Díky tomu, že umístíme QSpacerItem do rozložení grid a roztáhneme buňku, ve které je umístěn na počet řadků, ve kterých chceme mezeru, dosáhnme mezery o velikosti šířky QSpacerItemu. Poté vytvoříme label s textem "Barvy/Pozice", který bude usnaďnovat uživately orientaci v aplikaci. ::
       
         for radek in range(0,12):
            for sloupec in range(5):
                if radek==0:
                    button=QtGui.QPushButton(self)
                    button.setDisabled(True)
                    button.setStyleSheet("* { background-color: rgb(0,0,0) }")
                    button.resize(10,5)
                    self.widgets[radek].append(button)
                    grid.addWidget(button,radek+1,sloupec)
                    continue

V první části hromadného vytváření widgetů si vytvoříme vrchních pět tlačítek, které budou obsahovat hádanku. Proto si nastavíme barvu těchto tlačítek na černou, také je musíme učinit nemačkatelýmí, toho dosáhneme metodou button.setDiasabled(bool). Poté nám stačí vytvořené tlačítko přidat do pole widgets a umísťit ho do roložení, je důležité si všimnou, že počet řadku je o jedna vetší a to z toho důvodu, že již máme na tomto řádku obsažené popisky. ::

	if radek==11:
        button=QtGui.QPushButton(self)
        button.setStyleSheet("* { background-color: rgb(70,192,255) }")
        button.resize(10,5)
        button.clicked.connect(self.change)
        self.widgets[radek].append(button)
        grid.addWidget(button,radek+1,sloupec)
        continue

Poslední řadu tlačítek vytváříme stejným způsobem jako první řadu, s tím rozdílem, že těmto tlačítkům nastavíme signál clicked, který připojíme na metodu self.change. Dalším rozdílem je barva těchto tlačítek. První barvou tlačitek je první barva z pole barev. I tyto tlačíka umístíme do pole widgets. ::
 	
                button=QtGui.QPushButton(self)
                button.setDisabled(True)
                button.setStyleSheet("* { background-color: rgb(160,160,160) }")
                button.resize(10,5)
                self.widgets[radek].append(button)
                grid.addWidget(button,radek+1,sloupec)

Pro zobrazování předchozích tahů použijeme znovu tlačítka, a to z důvodu, aby naše aplikace vypadala konzistentně. Jako u prvního řádku tato tlačítka nastavíme metodou setDisabled na nestisknutelná. A jejich barvu nastavíme na šedou, proto aby uživatel viděl kolik mu zbývá tahů. Poté tato tlačítka umístíme do pole widgets. ::

             if radek==11:
                button=QtGui.QPushButton(self)
                button.setText("odeslat")
                button.resize(10,5)
                button.clicked.connect(self.odeslat)
                grid.addWidget(button,radek+1,6)
            else:            
                lbl=QtGui.QLabel(self)
                lbl.setText("0/0")
                grid.addWidget(lbl,radek+1,6)
                self.widgets[radek].append(lbl)
        self.setLayout(grid)
        self.show()

Každý řádek, na kterém jsou zobrazeny pokusy nebo hádanka by měl obsahovat popisek s počtem uhodnutých barev a pozic. Toho dosáhneme tím, že po vytvoření řádku tlačítek vytvoříme label s potřebnými parametry. Pokud vytváříme tlačítka na řádku jedenáct, čož je řádek, který slouží pro zadávání pokusů, tak místo vytvoření popisku vytvoříme odesílací tlačítko s signálem na metodu self.odeslat, tato metoda slouží pro odeslání pokusu a vyhodnocení stavu hry. ::

 def odeslat(self):
    hadani=[]
    pozice=0
    barvy=0
    self.pokusy+=1
    for i in range(5):
        red=self.widgets[11][i].palette().color(1).red()        
        blue=self.widgets[11][i].palette().color(1).blue()
        green=self.widgets[11][i].palette().color(1).green()
        hadani.append("%s,%s,%s"%(red,green,blue))

V první části metody odeslat si vytvoříme potřebné promněné a zvýšíme počet pokusů. Pokus užívatele musíme získat z každého tlačítka na jedenáctém řádku. Proto jsi projdeme jedenáctý řádek v poli widgets a pro každé tlačítko získáme jeho barvu. Barvu získáme z tlačítka pomocí button.pallete().color(1).red(), což nám zjistí  hodnotu červené části stejným způsobem zjistíme i modrou a zelenou složku. Tyto hodnoty poté uložíme do řetězce a ten vložíme do pole hádání, které reprezentuje uživatelův pokus. ::
        
         if hadani==self.hadanka:
            for x in range(5):
                self.widgets[0][x].setStyleSheet("* { background-color: rgb(%s) }"%self.hadanka[x])
	     self.dialog(True)

V první části podmínky, která vyhodnucuje stav hry, budeme zjišťovat zdali jsme vyhráli toho dosáhneme porovnáním polí hadami a hadanka, pokud jsou pole stejná odkryjeme hádanku a zavolám self.dialog(bool), která vytvoří dialogové okno s gratulací uživateli. ::
        
        else:
            if self.pokusy>10:
                for x in range(5):
                    self.widgets[0][x].setStyleSheet("* { background-color: rgb(%s) }"%self.hadanka[x])
                self.dialog(False)
            else:
                for i in range(len(hadani)):
                    if hadani[i] in self.hadanka:
                        barvy+=1
                    if hadani[i]==self.hadanka[i]:
                        pozice+=1
                    self.widgets[11-self.pokusy][i].setStyleSheet("* { background-color: rgb(%s) }"%hadani[i])
                self.widgets[11-self.pokusy][5].setText("%i/%i"%(barvy,pozice))


Pokud jsme neuhádli hádanku nastávaji dvě možnosti stavu hry a to prohra z důvodu vyčerpání pokusů nebo uřivateli pokusy ještě zbývají. V případě, že uživateli nezbývají pokusy zobrazíme hádanku stejným způsobem jako při výhře a zavoláme metodu self.dialog.

V druhém případě projdeme pole hadani a zjistíme kolik pozic se schoduje a kolik barev uživatel uhádl a zobrazíme barvy pokusu v příslušném řádku. Číslo řádku, na kterém jsou tlačítka, která chceme změnit, zjistíme odečtením pokusů od počtu řádků. To nám zajistí, že se pokusy budou zobrazovat od spodního řádku po horní v pořadí v jakem je uživatel zadal. ::

 def dialog(self,vyhra):
        if vyhra:
            text="Gratulace, vyhral jste. Prejete si hrat znovu"
        else:
            text="Skoda, prohral jste. Prejete si hrat znovu"
                
        dialog=QtGui.QDialog(self)
        grid=QtGui.QGridLayout()
        lbl=QtGui.QLabel(dialog)
        lbl.setText(text)
        lbl.resize(lbl.sizeHint())
        grid.addWidget(lbl,0,0,1,2)        
        button=QtGui.QPushButton(dialog)
        button.setText("Hrat znovu")
        button.clicked.connect(self.change_color)
        button.clicked.connect(dialog.close)
        button.resize(button.sizeHint())
        grid.addWidget(button,1,0)
        button=QtGui.QPushButton(dialog)
        button.setText("Konec")
        button.clicked.connect(QtCore.QCoreApplication.instance().quit)
        button.resize(button.sizeHint())
        grid.addWidget(button,1,1)
        dialog.setLayout(grid)
        dialog.exec_()

V metodě dialog si vytvoříme řetěz, podle toho jestli uživatel vyhrál nebo prohrál. Poté vytvoříme dialogové ono s label a dvoumi tlačítky. Jedno tlačítko ukončí celou hru a druhé vyresetuje hru do základního stavu. Základní stav vyvoláme metodou self.change_color. ::

 def change_color(self):
        for radek in range(len(self.widgets)):
            for sloupec in range(len(self.widgets[radek])):
                widget=self.widgets[radek][sloupec]
                if radek==0 and sloupec!=5:
                    widget.setStyleSheet("* { background-color: rgb(0,0,0) }")
                    continue
                if radek==11:
                    widget.setStyleSheet("* { background-color: rgb(70,192,255) }")
                    continue
                if radek<11 and sloupec==5:
                    widget.setText("0/0")
                else:
                    widget.setStyleSheet("* {  background-color: rgb(160,160,160) }")
        self.new()

V této metodě si vyresetuje hru do původního stavu, toho dosáhneme pomocí  projití pole widgets, ve kterém máme umístěny widgety, které potřebujeme změnit. Na řádku jedenáct jsou tlačítka, do kterých zadává uživatel svůj pokus, na nultém řádku jsou tlačítka s hádankou pro to tato tlačítka obarvíme modrou, respektive černou barvou. Poté vyresetujeme popisky, které jsou na všech řádcích kromě jedenáctého a vždy v pátem sloupci. Na konci zavoláme metodu new, která nám vytvoří novou hádanku a vyresetuje čitač pokusů.

.. image:: 15.png