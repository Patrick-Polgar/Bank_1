""" Bank_1.py """


class Bank_Account:
    def __init__(self, name, cash):
        self.name = name   # ide ementi el a felhasználó nevét
        self.cash = cash   # ide tárolja el mennyi pénz van a számlán
        self.log_ls = []   # lista a számlán történt változásokról
        self.log_ls.append(f"{self.name} létrehozott egy bankfiókot {self.cash} HUF-al")
  

    def print_info(self):
        print(f"{self.name} számla egyenlege {self.cash} HUF")

    def withdraw(self, num):
        self.cash -= num
        self.log_ls.append(f"{num} HUF levételével {self.name} számláján {self.cash} HUF van")
    
    def income(self, num):
        self.cash += num
        self.log_ls.append(f"{num} HUF érkezett {self.name} számlájára, az új egyenleg {self.cash} HUF")

    def log(self):
        for entry in self.log_ls:
            print(entry)


## Példa az elsö számla letrehozására Patriknak:
# account = Bank_Account("Patrik Polgar", 1000.0)


# Létrehoztunk 3 új számlát
pisti_account = Bank_Account("Pisti", 30000)
maris_account = Bank_Account("Máris", 50000)
boborjan_account = Bank_Account("Boborján", 10000)


## Ellenörizni, hogy a példány létrejött-e 
# print(account.name)  # Patrik Polgar
# print(account.cash)  # 1000.0
# print(account.log_ls)  # [Patrik Polgar létrehozott egy bankfiókot 1000.0 HUF-al.]


## Tranzakciók Patriknak
# account.withdraw(100)
# account.income(200)


# Tranzakciók az új számláknak (kertészeti megbízás Máris szomszédtól és Pisti fizetése)
maris_account.withdraw(25000)
pisti_account.income(25000)

pisti_account.income(80000)

# Továbbbi tranzakciók (Pista kiadásai: éttermi ebéd és elromlott mosógép, Boborján megbizása)
pisti_account.withdraw(2500)
pisti_account.withdraw(37000)
boborjan_account.income(37000)


## Ellenörizni az egyenleget és tranzakció logot Patriknak
# account.print_info()  # Patrik Polgar számlaegyenlege 1000.0 HUF
# account.log()
# kiírás: Patrik Polgár...


## Ellenörizni az egyenleget és tranzakció logot az új számláknak
# print("Pisti számla egyenlege: ")
# pisti_account.print_info()
print("Pisti tranzakció logja: ")
pisti_account.log()


# A számlák egyenlegének kiírása (Pisti, Máris, Boborján)

print("Az aktuális számlaegyenlegek: ")
pisti_account.print_info()
maris_account.print_info()
boborjan_account.print_info()
