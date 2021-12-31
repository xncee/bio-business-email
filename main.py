import os, random, time, subprocess, string
from tkinter import *
from tkinter import filedialog
clear = lambda: subprocess.call('cls||clear', shell=True)
try:
    import requests
except ImportError:
    os.system("pip install requests")
    import requests
try:
    import colorama
except ImportError:
    os.system("pip install colorama")
    import colorama
colorama.init()
class DESIGN():
    WHITE = '\x1b[1;37;40m'
    YELLOW = '\x1b[1;33;40m'
    RED = '\x1b[1;31;40m'
    BLUE = '\x1b[36m\x1b[40m'
    GREEN = '\x1b[32m\x1b[40m'
    greenplus = f"{WHITE}[ {GREEN}+{WHITE} ]"
    blueplus = f"{WHITE}[ {BLUE}+{WHITE} ]"
    redminus = f"{WHITE}[ {RED}-{WHITE} ]"
    bluelist = f"{WHITE}[ {BLUE}LIST {WHITE}]"
    blueaccounts = f"{WHITE}[ {BLUE}ACCOUNTS {WHITE}]"
    redlist = f"{WHITE}[ {RED}LIST {WHITE}]"
    redaccounts = f"{WHITE}[ {RED}ACCOUNTS {WHITE}]"
    blueone = f"{WHITE}[ {BLUE}1 {WHITE}]"
    bluetwo = f"{WHITE}[ {BLUE}2 {WHITE}]"
    xrblue = f"\n{blueplus} Business Email-Bio {BLUE}/ {WHITE}Instagram{BLUE}: {WHITE}@xnce {BLUE}/ {WHITE}@ro1c"
users = []
accounts = []
class FILES():
    def __init__(self):
        self.select_file(f"\n{DESIGN.bluelist} Enter To Select File: ")
        self.open_file(users, DESIGN.bluelist, DESIGN.redlist)
        self.select_file(f"\n{DESIGN.blueaccounts} Enter To Select File: ")
        self.open_file(accounts, DESIGN.blueaccounts, DESIGN.redaccounts)
    def select_file(self, text):
        print(text, end="")
        input()
        root = Tk()
        root.title(".txt")
        self.path = filedialog.askopenfilename(initialdir="", title="Select A File", filetypes=(("txt document","*.txt"),("All Files", "*.*")))
        root.destroy()
        root.mainloop()
    def open_file(self, my_list, bluefile, redfile):
        filename = self.path.split("/")[-1]
        if self.path[-4:]!=".txt":
            print(f"\n{redfile} Please Select (.txt) File ", end="")
            input()
            exit()
        try:
            for x in open(self.path, "r").read().split("\n"):
                if x!="":
                    my_list.append(x)
            print(f"\n{bluefile} Successfully Load {DESIGN.BLUE}{filename}")
        except Exception as err:
            print(f"\n{redfile} {err} ", end="")
            input()
            exit()
class Xnce():
    def __init__(self):
        self.business, self.bio, self.bad, self.error, self.turn, self.run = 0, 0, 0, 0, 0, True
    def inex(self, text):
        print(f"\n{DESIGN.redminus} {DESIGN.WHITE}run = {DESIGN.RED}False {DESIGN.WHITE}, {text}")
        print(f"\n{DESIGN.redminus} Enter To Exit: ", end="")
        input()
        exit()
    def remove_session(self, sessionid):
        accounts.remove(sessionid)
        if len(accounts) < 1:
            self.inex("No Accounts")
    def usernameinfo(self, username, sessionid):
        head = {
            "user-agent": f"Instagram 150.0.0.0.000 Android (29/10; 300dpi; 720x1440; {''.join(random.choices(string.ascii_lowercase+string.digits, k=16))}/{''.join(random.choices(string.ascii_lowercase+string.digits, k=16))}; {''.join(random.choices(string.ascii_lowercase+string.digits, k=16))}; {''.join(random.choices(string.ascii_lowercase+string.digits, k=16))}; {''.join(random.choices(string.ascii_lowercase+string.digits, k=16))}; en_GB;)",
            "cookie": f"sessionid={sessionid}",
            }
        req = requests.get(f"https://i.instagram.com/api/v1/users/{username}/full_detail_info/", headers=head)
        if "pk" in req.text:
            self.turn += 1
            user = req.json()["user_detail"]["user"]
            if user["is_verified"]:
                if "@" in user["biography"] and "." in user["biography"]:
                    self.has_bio = 0
                    self.bio += 1
                    with open("verified-bio.txt", "a") as verbiofile:
                        verbiofile.write(f'\n{user["username"]}:{user["biography"]}\n----')
                        verbiofile.close()
                else:
                    self.has_bio = 1
                if user["public_email"]!="":
                    self.has_business = 0
                    self.business += 1
                    with open("verified-business.txt", "a") as verbusfile:
                        verbusfile.write(f'\n{user["username"]}:{user["public_email"]}')
                        verbusfile.close()
                else:
                    self.has_business = 1
                if self.has_bio!=0 and self.has_business!=0:
                    self.bad += 1
            else:
                if "@" in user["biography"] and "." in user["biography"]:
                    self.has_bio = 0
                    self.bio += 1
                    with open("notverified-bio.txt", "a") as nverbiofile:
                        nverbiofile.write(f'\n{user["username"]}:{user["biography"]}')
                        nverbiofile.close()
                else:
                    self.has_bio = 1
                if user["public_email"]!="":
                    self.has_business = 0
                    self.business += 1
                    with open("notverified-business.txt", "a") as nverbusfile:
                        nverbusfile.write(f'\n{user["username"]}:{user["public_email"]}')
                        nverbusfile.close()
                else:
                    self.has_business = 1
                if self.has_bio!=0 and self.has_business!=0:
                    self.bad += 1
        elif req.status_code==404:
            self.turn += 1
        elif "challenge_required" in req.text and req.status_code==400:
            self.remove_session(sessionid)
        elif req.status_code == 403:
            self.remove_session(sessionid)
        elif req.status_code==429:
            self.error += 1
        else:
            print(f"\n{DESIGN.redminus} {req.text}, {req.status_code}")
        self.counter()
        time.sleep(1)
    def counter(self):
        os.system(f"title Bio: {self.bio} / Business: {self.business} / Bad: {self.bad} / Error: {self.error}")
    def main(self):
        while self.run:
            for sessionid in accounts:
                if ":" in users[self.turn]:
                    username = users[self.turn].split(":")[1]
                else:
                    username = users[self.turn]
                try:
                    self.usernameinfo(username, sessionid)
                except Exception as err:
                    print(err)
FILES()
x = Xnce()
clear()
print(DESIGN.xrblue)
print(f"\n{DESIGN.blueplus} Enter To Start: ", end="")
input()
x.main()
