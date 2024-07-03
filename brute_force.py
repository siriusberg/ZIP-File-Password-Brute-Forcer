import os
import zipfile
from time import time

def cls():
    os.system('cls' if os.name == 'nt' else 'clear')

cls()

try:
    a = int(input(" [?] Enter Number: "))
except ValueError:
    print(" [!] Invalid Input")
    quit()

if a == 0:
    cls()
    print(" [!] Good Bye :)")
    quit()
elif a == 1:
    cls()
    textzippass = ''''''
    print(textzippass)
    file_path = input(" [+] ZIP File Address: ")
    print("")
    word_list = input(" [+] Password List Address: ")

    def main(file_path, word_list):
        try:
            zip_ = zipfile.ZipFile(file_path)
        except zipfile.BadZipFile:
            print(" [!] Please check the file's Path. It doesn't seem to be a ZIP file.")
            quit()

        password = None
        i = 0
        c_t = time()

        try:
            with open(word_list, "r") as f:
                passes = f.readlines()
        except FileNotFoundError:
            print(" [!] Password list file not found.")
            quit()

        for x in passes:
            i += 1
            password = x.strip()
            try:
                zip_.extractall(pwd=password.encode('utf-8'))
                t_t = time() - c_t
                print(f"\n [*] Password Found :)\n [*] Password: {password}\n")
                print(f" [***] Took {t_t:.2f} seconds to crack the Password. That is, {i/t_t:.2f} attempts per second.")
                quit()
            except (RuntimeError, zipfile.BadZipFile):
                pass

        print(" [X] Sorry, Password Not Found :(")
        quit()

    main(file_path, word_list)
