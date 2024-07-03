# ZIP Password Brute Forcer

## Description
This script attempts to brute-force the password of a given ZIP file using a list of potential passwords. It is written in Python and is compatible with Python 3.

## Requirements
- <a href="https://www.python.org/">Python 3</a>
- `zipfile` module

## Usage
1. Clone the Repository or Download the Script and Go To the Directory<br>
```
git clone "https://github.com/siriusberg/ZIP-File-Password-Brute-Force/"
cd <repository_directory>
```
2. Prepare Your Files
- <b>ZIP File</b> you want to crack
- <b>Wordlist</b> since this whole operation rely on your dictionary. For example, you can find a lots of wordlist from <a href="https://github.com/duyet/bruteforce-database"> this database </a>
3. Run the Script
```
python brute_force.py
```
4. Follow the Prompts
Enter <b>0</b> to exit the script and <b>1</b> to start the attack. You can understand this by examining the code. <br>
For example :
```
[?] Enter Number : 1
[+] ZIP File Address : /path/to/your/zipfile.zip
[+] Password List Address: /path/to/your/passwordlist.txt
```
If the password is found, the script will output the password and the time taken to crack it. If not, it will inform you that the password was not found. I inform you that <b>the better the wordlist the greater chance you'll crack it</b>.

## Notes
- Ensure you type the right paths to your ZIP file and wordlist
- The password list should contain potential password, <b>one per line</b>
- Make sure the password list is up-to-date

## Disclaimer 
<b>This script is intended for educational and ethical purpose only. Unauthorize use to gain access to files without permission is illegal.</b>
