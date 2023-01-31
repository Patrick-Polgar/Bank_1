""" Bank_1.py """


class Bank_Account:
    bank_accounts_dict = {}
    def __init__(self, name, password, cash):
        self.name = name   # ide ementi el a felhasználó nevét
        self.password = password
        self.cash = cash   # ide tárolja el mennyi pénz van a számlán
        self.log_ls = []   # lista a számlán történt változásokról
        Bank_Account.bank_accounts_dict[self.name] = {
             "password": self.password,
             "cash": self.cash,
             "log_ls": self.log_ls
        }
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
   
    def print_nice(self, bank_accounts_dict):
        print("\n\n")
        print(f"Regisztrált bankszámlák összesen: {len(bank_accounts_dict)}")
        print("\n")
        print("A számlák és az egyenlegek:")
        for account_name, account_details in bank_accounts_dict.items():
            print(f"{account_name} ({account_details['cash']})")
        print("\n")
        print("Tranzakció logok:")
        for account_name, account_details in bank_accounts_dict.items():
            print(f"\n{account_name}:")
            for log in account_details['log_ls']:
                print(f" - {log}")


 	
## Példa az elsö számla letrehozására Patriknak:
# account = Bank_Account("Patrik Polgar", 1000.0)


# Létrehoztunk 3 új számlát
pisti_account = Bank_Account("Pisti", 30000, cash=30000)
maris_account = Bank_Account("Máris", 50000, cash=50000)
boborjan_account = Bank_Account("Boborján", 10000, cash=10000)


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

bank_account_dict = {"Boborján": {"password": "", "cash": 1000, "log_ls": ["hjgjhg", "hkgjhg"]}}
bank_account_dict["Boborján"].print_nice()
