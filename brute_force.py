import os
import subprocess
from time import time
from multiprocessing import Process

def cls():
    os.system('cls' if os.name == 'nt' else 'clear')

def brute_force(file_path, word_list, start, end):
    for i, password in enumerate(word_list[start:end], start=start+1):
        password = password.strip()
        print(f"[*] Trying password {i}: {password}")

        result = subprocess.run(['7z', 'x', '-p' + password, file_path], 
                                capture_output=True, text=True)
        if "Everything is Ok" in result.stdout:
            end_time = time()
            print(f"\n [*] Password Found :)\n [*] Password: {password}\n")
            print(f" [***] Took {end_time - start_time:.2f} seconds to crack the password. That is, {i / (end_time - start_time):.2f} attempts per second.")
            return

    print(" [X] Sorry, Password Not Found :(")

if __name__ == "__main__":
    cls()
    print("[*] Welcome to ZIP Password Brute Forcer!\n")
    file_path = input(" [+] ZIP File Address: ").strip().strip("'").strip('"')
    word_list_path = input(" [+] Password List Address: ").strip().strip("'").strip('"')
    num_processes = int(input(" [+] Number of Processes: "))

    with open(word_list_path, "r", encoding="ISO-8859-1", errors="ignore") as f:
        word_list = f.readlines()

    chunk_size = len(word_list) // num_processes

    processes = []
    start_time = time()

    for i in range(num_processes):
        start = i * chunk_size
        end = (i + 1) * chunk_size if i < num_processes - 1 else len(word_list)
        process = Process(target=brute_force, args=(file_path, word_list, start, end))
        processes.append(process)
        process.start()

    for process in processes:
        process.join()

    print("[*] All processes finished.")
