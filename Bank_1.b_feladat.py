# Szia
# Kiraly nagyon jo megoldasok voltak eddig es ha van kedved hozza folytatjuk a project epiteset
# Ezen a heten a projectet tovabb fejlesztjuk
# eloszor kerlek hozz letre egy bank_accounts_dict = {} nevu konyvtarat

---

# Kerlek add hozza a Bank_Account class init fugvenyehez
# hogy a felhasznalo nevevel letrehoz egy kulcsot a bank_accounts_dict -in belul
# az ertek it egy ujabb konyvtar lesz

---

# Ennek a konyvtaron beluli konyvtarnak lesz harom kulcsa
# I."password"  II."cash"  III."log_ls"

---

# "password" kulcshoz tartozzon egy ures string ertek parnak
# "cash" kulcshoz a szamlan levo penz tartozzon ertek parnak
# "log_ls" kulcshoz a  log olt mondatok listaja az ertek par

---

# Valami hasonlo strukturat kene kapnunk de ha elakadsz , szolj es segitek szivesen

# bank_accounts_dict = {"Boborjan":{"password":"", "cash" : 1000, log_ls=["hjgjhg","hkgjhg"]}}
class Bank_Account:
    def __init__(self, name, cash):
        self.name = name  # ide ementi el a felhasználó nevét
        self.cash = cash  # ide tárolja el mennyi pénz van a számlán
        self.log_ls = []  # lista a számlán történt változásokról
        self.log_ls.append(f"{self.name} létrehozott egy bankfiókot {self.cash} HUF-al")

    def print_info(self):
        print(f"{self.name} számla egyenlege {self.cash} HUF")

    def withdraw(self, num):
        # kerlek modosits a penzosszeget a bank_accounts_dict ba is
        self.cash -= num
        # kerlek add hozza ezt a mondatot a bank_accounts_dict ba is a log olt mondatok listajahoz
        self.log_ls.append(f"{num} HUF levételével {self.name} számláján {self.cash} HUF van")

    def income(self, num):
        # kerlek modosits a penzosszeget a bank_accounts_dict ba is
        self.cash += num
        # kerlek add hozza ezt a mondatot a bank_accounts_dict ba is a log olt mondatok listajahoz
        self.log_ls.append(f"{num} HUF érkezett {self.name} számlájára, az új egyenleg {self.cash} HUF")

    def log(self):
        for entry in self.log_ls:
            print(entry)


# Létrehoztunk 3 új számlát
pisti_account = Bank_Account("Pisti", 30000)
maris_account = Bank_Account("Máris", 50000)
boborjan_account = Bank_Account("Boborján", 10000)

# Tranzakciók az új számláknak (kertészeti megbízás Máris szomszédtól és Pisti fizetése)
maris_account.withdraw(25000)
pisti_account.income(25000)
pisti_account.income(80000)

# Továbbbi tranzakciók (Pista kiadásai: éttermi ebéd és elromlott mosógép, Boborján megbizása)
pisti_account.withdraw(2500)
pisti_account.withdraw(37000)
boborjan_account.income(37000)

## Ellenörizni az egyenleget és tranzakció logot az új számláknak
print("Pisti tranzakció logja: ")
pisti_account.log()

print("Az aktuális számlaegyenlegek: ")
pisti_account.print_info()
maris_account.print_info()
boborjan_account.print_info()

---

# Kerlek csinalj egy egy print_nice nevu fugvenyt
# A print_nice(bank_accounts_dict) fugveny feladata az lesz
# hogy szepen kiirja az ilyen felepitesu konyvtarakat amit letrehoztunk
# A fugvenynek egy argumentuma lesz ami a bank_accounts_dict

# eloszor irasd ki  a fugvennyel legyszi hogy:
# A Rendszerbe X bankaccount van regisztrakva:
# Utanna legyszives a konyvtarbol beulvasva ird ki a felhasznalo neveket
# Minden felhasznalo nevet uj sorba
# Majd ezutan loopolj vegig minden felhasznalo neven
# Eloszor legyszi irj ki egy uressort ami majd eltagolja az informacio egysegeket
# Ird ki a Felhasznalo nevet es melle zarojelbe a pezosszeget
# Majd irasd ki a logolt mondatok listajat
# kerlek irasd ki a kepernyore a print_nice fugvennyel a bank_accounts_dict konyvtarat


# Plusz feladatnak ha szeretnéd, fogd meg a bank_accounts_dict konyvtarat es ments ki json be kerlek


# kovetkezo heten ezzel fogunk dolgozni hogy hogyan lehet ki es beolvasni jsonbol
# aztan utanna csak egy lepes az adatbazis

# Remelem tetszik a feladat es bocs hogy nem akarok tul gyorsan menni
# De akkor az egesz ertelmet vesztene
# Majd irj ha lesz idod

