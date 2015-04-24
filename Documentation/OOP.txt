Objektově orientované programování (OOP)
========================================
OOP paradigma se začalo postupně vyvíjet
již v padesátých letech minulého století díky potřebě snadnější a efektivnější 
údržby kódu. Hlavní myšlenkou OOP paradigmatu je práce s objekty. Jako objekt si 
například můžeme představit bankomat. Bankomat má několik funkcí a to třeba vklady, 
výběry, stav konta. Tyto funkce provádí všechny bankomaty a je jedno zdali jsou to bankomaty 
ČSOB nebo Komerční Banky. Z tohoto důvodu je dobré se dívat na OOP jako na reálný svět. 
Nyní se podíváme na základní pojmy, které se užívají v OOP a jaký je pro ně zápis v Pythonu.

Třída
---------
Třída je základním pilířem OOP, protože z ní 
vytváříme samotné objekty, někdy také nazývané instance 
třídy. Jde prakticky o recept jak vytvořit daný objekt. 
Ve třídě definujeme metody. Důležité je si uvědomit, 
že k objektu přistupujeme jako k černé skříňce, 
neboť je nám jedno zdali objekt používá jiné 
funkce k dosažení námi požadovaného výsledku.	::

	
	class A():
		pass

Deklarace třídy v Pythonu se provádí 
podobně jako definice funkce pouze s tím 
rozdílem, že místo příkazu def použijeme příkaz class. 
Závorky nejsou nutné, pokud vytvářená třída nedědí z jiné třídy.

Dědičnost
-------------

Dědičnost je vlastností každého objektového programovacího jazyka. 
Jde o možnost získat metody z dříve vytvořených tříd. Můžeme si to představit jako v 
reálném světě. Pes je zvíře a stejně jako každé zvíře má potřebu jíst, ale zároveň patří do 
skupiny psovitých šelem, které jako každé zvíře mají potřebu jíst. Je to velmi dobrá vlastnost, 
neboť nemusíme v každé třídě psát stejné metody. ::

	
	class A():
		pass
	class B(A):
		pass

 

V Pythonu se dědičnost provádí tím, že do závorek za třídu přidáme již dříve vytvořenou třídu.
 
Polymorfismus
------------------

Polymorfismus je velmi důležitou vlastností jazyka podporujícího OOP paradigma. 
Nejinak je tomu i v Pythonu. Polymorfismus zajištuje logické fungování metod ve 
zděděných třídách. Můžeme si to jednoduše představit na příkladu. 
Máme třídu Pes. Třída pes je potomek třídy Zvíře, která 
obsahuje metodu Jedení. Stejně jako každé zvíře i pes jí potravu, 
ale nejí stejnou potravu jako všechna zvířata a proto si metodu ve 
třídě Pes přepíšeme metodou Jedení, ale s jiným vstupem než má ve třídě Zvíře. 
Polymorfismus nám zajistí to, aby se při volbě metody Jídla na objekt vytvořený z 
třídy Pes, provedla námi přepsaná metoda Jedení.
