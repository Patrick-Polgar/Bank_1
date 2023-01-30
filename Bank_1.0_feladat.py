#Feladat Patrik Baratomnak

#Ezen a heten azt talaltam ki hogy letrehozunk egy python filet lepesrol lepesre hogy informaciokat taroljunk kepzelet beli bankaccount okrol.
#A terv az hogy taroljuk a felhasznaloneveket es a tranzakciokay

#Legyszives keszits egy classt Bank_Account neven
#a Bank_Account classnak 2 Argumentuma lesz.
#az elso argumentuma ,avagy az az ertek amik meg kell hagyni a felhasznalo neve
#a masodik argumentuma egy szam (float) ami a nyito osszeget szimbolizalja

#szeretnelek arra megkerni ha letrejon egy Bank_Account objektum akkor tarolon el 3 valtozot:
#1.valtozo: self.name = ide mentse el a felhasznalo nevet
#2.valtozo: self.cash = ide tarolja el mennyi penz van az accounton
#3. valtozo: self.log_ls = ez egy lista lesz azokbol a mondatokbol amik rogzitik aszamlan tortent valtozasokat

#Amikor letrejon egy Bank_Account objectum akkor adja hozza az alabbi mondatot a self.log_ls listahoz:
	#"nev" letrehozott egy bankfiokot "osszeg" HUF -al.
	
#kerlek csinalj egy fugvenyt a classon belul print_info(self) nevvel
#ennek a fugvenynek a lenyege ha meghivjak kiirja a felhasznalonevet es azt hogy mennyi penz van a szamlajan
#ezt irja ki az alabbi szormaba:
#"nev" szamla egyenlege "osszeg" HUF

#most szeretnem hogy csinaljunk meg
#ket fugvenyt a Bank_Account objectumoknak

#az elso:withdraw(self, num) fugveny
#penzosszeg kivetelere
#a fugveny levonja az osszeget az egyenlegrol (self.cash)
#a fugveny log-olja a tranzakciot,
#azaz hozzaadja a self.log_ls hez az alabbi mondatot:
#"osszeg" HUF levetelevel "nev" szamlajan "egyenleg" HUF van.

#masodik:income(self, num) fugveny
#penzosszeg hozzaadasa az egyenleghez
#a fugveny hozzaadja az osszeget az egyenlegrol (self.cash)
#a fugveny log-olja a tranzakciot,
#azaz hozzaadja a self.log_ls hez az alabbi mondatot:
#"osszeg" HUF erkezett "nev" szamlajara,az uj egyenleg "egyenleg" HUF.

#majd vegul csinaljunk egy utols fugvenyt a Bank_Account objektumoknak: log(self)
#ez a fugveny szimplan kiirja a self.log_ls lista mondatait, minden mondatot uj sorbablegyszi

#most teszteljuk a Bank_Account class mukodeset, mi szolsz?
#hozzunk letre 3 accountot:
	#1.:Pisti 30000HUF al
	#2.:Maris 50000HUF al
	#3.:Boborjan 10000HUF al
	
#mondjuk azt hogy Maris megbizta Pistat hogy csinalja meg a kertjet 25000 HUF ert
#ekkor vonjuk le Maris szamlajarol az osszeget es adjuk hozza Pistajehoz

#aztan mondjuk Pistinek megerkezik a fizuja, adjunk hozza 80000 HUF ot a szamlajahoz legyszi

#Pisti evett Mekibe egy menut 2500 HUF ert

#es vegul Pistinek sajnos elromlott a mosogepe(mint nekem hehe) es megkerte Boborjant hogy csinalja meg az 37000 HUF ert

#Most irassuk ki mind harom account egyenleget

#es vegul irjuk irjuk ki Pisti accounjahoz tartozo loggolt mondatok listajat

#Szia Remelem tetszett a feladat,
#Ha igen es van kedved akkor ezt heti rendszeresseggel ezt epithetjuk tovabb szepen lepesrol

#Te meg mien funkciokat tennel bele a programba? Majd Irj,
#Udv Dani