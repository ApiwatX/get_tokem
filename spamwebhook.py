import threading, requests, os, random
from colored import fg, attr
from itertools import cycle
from pystyle import Write, Colors, Colorate
from time import strftime, gmtime
from datetime import datetime


session = requests.Session()

#colors
a = fg('#a005ed')
b = attr('reset')
c = fg('#00D7D3')  

#webhook link
#web=input(f"{a}[{c}COMMAND{b}{a}]{b} {c}WEBHOOK{a}: ")
web = Write.Input(f"[COMMAND] ใส่ลิ้งเว็บฮุค: ", Colors.rainbow, interval=0.0025)

#webhook username
rando=["BFHMSC#หีหีหี","WEBHOOKโง่ๆ","ดิสมึงเเม่งกากวะ","BFHMSC"]

#webhook message
#spam=input(f"{a}[{c}COMMAND{b}{a}]{b} {c}MASSAGE{a}: ")
spam = Write.Input(f"[COMMAND] ใส่ข้อความ: ", Colors.rainbow, interval=0.0025)

#webhook avatars
avatars = cycle(["https://cdn.discordapp.com/attachments/983376701520216097/984830316176891924/standard_1.gif", "https://cdn.discordapp.com/attachments/983376701520216097/983691044904394772/standard.gif", "https://cdn.discordapp.com/attachments/983376701520216097/984830316176891924/standard_1.gif"])

#proxies
proxies = open('proxies.txt').read().split('\n')

def ehook(webhook):
# while True:
                now = datetime.now()
                s = now.strftime("%S")
                x = f'{strftime(f"[%H:%M:{s}]", gmtime())} สแปมสำเร็จ {spam}'
                yes = f'{strftime(f"[%H:%M:{s}]", gmtime())}'
                proxy = cycle(proxies)
                
                einfo={
                    'username': random.choice(rando),
                    'content': spam,
                    "avatar_url": next(avatars)
                }
                r = session.post(webhook, json=einfo, proxies={"http": 'http://' + next(proxy)})
                if "retry_after" in r.text:
                    print(f"{a}{yes}{b} ratelimited sleeping for {a}{r.json()['retry_after']}{b} secs.")
                elif r.status_code == 204:
                    print(Colorate.Horizontal(Colors.rainbow,x))
                else:
                    pass

if __name__ == "__main__":
    os.system('cls & title |||||MAKE BY : BFHMSC|||||')
    logo = """
 ______   ______   ________   ___ __ __   __ __ __   ______    _______   ___   ___   ______   ______   ___   ___     
/_____/\ /_____/\ /_______/\ /__//_//_/\ /_//_//_/\ /_____/\ /_______/\ /__/\ /__/\ /_____/\ /_____/\ /___/\/__/\    
\::::_\/_\:::_ \ \\::: _  \ \\::\| \| \ \\:\\:\\:\ \\::::_\/_\::: _  \ \\::\ \\  \ \\:::_ \ \\:::_ \ \\::.\ \\ \ \   
 \:\/___/\\:(_) \ \\::(_)  \ \\:.      \ \\:\\:\\:\ \\:\/___/\\::(_)  \/_\::\/_\ .\ \\:\ \ \ \\:\ \ \ \\:: \/_) \ \  
  \_::._\:\\: ___\/ \:: __  \ \\:.\-/\  \ \\:\\:\\:\ \\::___\/_\::  _  \ \\:: ___::\ \\:\ \ \ \\:\ \ \ \\:. __  ( (  
    /____\:\\ \ \    \:.\ \  \ \\. \  \  \ \\:\\:\\:\ \\:\____/\\::(_)  \ \\: \ \\::\ \\:\_\ \ \\:\_\ \ \\: \ )  \ \ 
    \_____\/ \_\/     \__\/\__\/ \__\/ \__\/ \_______\/ \_____\/ \_______\/ \__\/ \::\/ \_____\/ \_____\/ \__\/\__\/ 
                                 ตัวสแปมเว็บฮุค                                                                                           
      """
    print(Colorate.Horizontal(Colors.rainbow,logo,3))
    while True:
     for i in range(10):
      threading.Thread(target=ehook, args=(web,)).start()
