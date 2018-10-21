from getpass import getpass
import os
import time

def menu():
      while True:
           print("")
           os.system("clear")
           print('\033[1;36;40m<============MrsOs=============>')
           print('')
           print("    LOGIN DULU ANJING")
           print("\033[1;93m")
           print(" \033[1;92mMasukin user sama pw nya tuh")
           print("\033[1;93m")
           print("\033[1;36;40m<=============================>")
           print("")
           try:
                x = str(input('\033[1;92mUsername Anjing \033[1;93m: '))
                print("")
                e = getpass('\033[1;92mPassword Ngentod \033[1;93m: ')
                print ("")
                if x=="Fuckyou" and e=="Hode":
                   print('Bentar Gua Cek dulu...')
                   time.sleep(1)
                   os.system('clear')
                   print('LOGIN BERHASIL:)..')
                   time.sleep(1)
                   os.system('clear')
                   print('')
                   print('Gunakan Dengan Bidjak tod:)')
                   time.sleep(1)
                   os.system('clear')
                   os.system('cowsay -f ghostbusters "Jangan Recode Goblog"')
                   print('\033[1;92m                    WELCOME TO TOOLSFUCK')
                   print("")
                   break
                else:
                      print("")
                      print("")
                      print("")
                      print("")
                      print("\033[1;91m     password salah kontol")
                      time.sleep(2)
                      print("")
           except Exception:
                      
                      print("")
                      print("")
                      print("")
                      print("")
                      print("")
                      print("\033[1;91m     password salah kontol")
                      time.sleep(2)
           except KeyboardInterrupt:
                      print("")
                      os.system('killall -9 com.termux')
                      print("")
                      print("")
                      print("")
                      print("")
                      print("\033[1;91m     Masukin Yg Bner Njign")
                      time.sleep(2)
menu()
