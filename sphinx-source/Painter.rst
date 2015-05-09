Painter
=========

Není tak úplně widget, ale je to nástroj umožnující kreslení geometrických obrazců vyplňování oblastí barvou, nebo také psaní textu kdekoliv na hlavním okně. Jako první je důležité si říci jak funguje kreslení v PyQt. 

Kreslení probíhá v PyQt v paintEvent metodě, která se automaticky spouští, při změně rozměrů okna, posunutí okna a také při vytváření okna. Díky těmto vlastnostem můžeme vytvářet vlastní widgety,  které  se nám budou automaticky přizpůsobovat velikosti okna. 

Pokud chceme kreslit na naší aplikaci je důležité, abychom si reimplementovali metodu paintEvent ve třídě, která definuje naše GUI. Nyní si ukážeme jednoduchý příklad kreslení. ::

 class Drawing(QtGui.QWidget):
    def __init__(self):
        super(Drawing,self).__init__()
        self.setup()
    def setup(self):
         self.setGeometry(300, 300, 350, 300)
         self.setWindowTitle("Lines")
         self.show()
    def paintEvent(self, e):
        self.painter=QtGui.QPainter()
        self.painter.begin(self)
        self.draw()
        self.painter.end()

V první části kódu si vytvoříme naše okno, nastavíme mu titulek. Nejdůležitější částí tohoto kódu je reimpletovaná metoda paintEvent, která příjmá jako parametr typ eventu, který ji vyvolal, ale to pro nás není důležité. V metodě paintEvent si vytvoříme painter, kterým budeme vytvářet obrazce. Je důležité si zapamatovat, že painterem mužeme pracovat poutze v metodě paintEvent a také to, že kreslení probíhá po zavolání metody painter.begin(widget-na-který-kreslime). Důležité je také použít metodu painter.end(), protože po zavolání této metody se nám vykreslí to co jsme nakreslili. ::

 def draw():
	pen=QtGui.QPen(QtCore.Qt.black, 2, QtCore.Qt.SolidLine)
        pen.setColor(QtGui.QColor(100,100,100))
        pen.setStyle(QtCore.Qt.SolidLine)
        self.painter.setPen(pen)        
        self.painter.drawLine(10,10,340,10)

Jako první si vytvoříme QPen což, je nástroj, který nastavuje jak budou vypadat čáry, které budeme kreslit, jako parametry příjmá barvu. Základní pojmenované barvy můžeme získat z modulu QtCore, která obsahuje třídu Qt, kde jsou barvy uložene pod názvem barvy. Tyto barvy můžeme předat poté našemu peru. Dalším parametrem je tloušťka čáry a posledním parametrem je styl čáry. Styly čar jsou uloženy ve stejné třídě jako barvy. Tyto parametry nemusíme nastavovat při inicializaci QPen, ale můžeme je nastavi pomocí metod setColor(QColor) a setStyle(QStyle). 

Proto aby painter použil typ čáry, který chceme nakreslit, musíme nastavit námi vytvořené QPen k použití. To provedeme metodou painter.setPen(QPen). Pro nakreslení čáry se volá metoda painter.drawLine(x_začatku,y_začatku, x_konce,y_konce). V další časti se vytvoříme čtyři další čáry stejným způsobem jako tuto. ::

        pen.setStyle(QtCore.Qt.DashLine)
        self.painter.setPen(pen)
        self.painter.drawLine(10,30,340,30)
        
        pen.setStyle(QtCore.Qt.DashDotDotLine)
        self.painter.setPen(pen)
        self.painter.drawLine(10,50,340,50)
        
        pen.setStyle(QtCore.Qt.DashDotLine)
        self.painter.setPen(pen)
        self.painter.drawLine(10,70,340,70)
        
        pen.setStyle(QtCore.Qt.DotLine)
        self.painter.setPen(pen)
        self.painter.drawLine(10,90,340,90)
        
        pen.setStyle(QtCore.Qt.NoPen)
        self.painter.setPen(pen)
        self.painter.setBrush(QtGui.QColor(255, 0, 0))
        self.painter.drawRect(10, 130, 90, 60)

        self.painter.setBrush(QtGui.QColor(0, 255, 0,))
        self.painter.drawRect(130, 130, 90, 60)

        self.painter.setBrush(QtGui.QColor(0, 0, 255,))
        self.painter.drawRect(250, 130, 90, 60)
        self.painter.drawEllipse(130,200,90,60)

Pro vytvoření obrazců jako elipsa nebo obdelník potřebjeme metodu painter.setBrush(QColor). Ta nám vyplní obrazec barvou a ten se díky tomu stane viditelným. Protože nechceme aby naše vytvořené obrazce neměli okraj. Vytvoříme QPen s parametrem NoPen, to nám zajistí, že QPen nebude viditelné. Poté pomocí metody painter.drawRect(x_levý,y_levý,x_pravý,y_pravý) vykreslíme obdelník, takto vytvoříme dva další obdelníky s různou barvou. Elipsa se vytváří stejným způsobem jako obdelník, ale metodou painter.drawElipse(x_stred,y_stred,výška,šířka).

.. image:: img/14.png