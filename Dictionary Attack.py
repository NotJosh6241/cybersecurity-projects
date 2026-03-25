import time
import os

def dictionary_attack(target_password, wordlist_path):
    start_time = time.time()
    attempts = 0

    try:
        with open(wordlist_path, "r", encoding="utf-8", errors="ignore") as f:
            for line in f:
                guess = line.strip()
                attempts += 1
                if guess == target_password:
                    elapsed = time.time() - start_time
                    print(f"Password Cracked: '{guess}'")
                    print(f"Time taken: {elapsed:.4f} seconds")
                    print(f"Attempts made: {attempts:,}")
                    return
    except FileNotFoundError:
        print(f"Wordlist file not found!")
        return
    
    elapsed = time.time() - start_time
    print(f"\n❌ Password not found in wordlist.")
    print(f"⏱  Time taken: {elapsed:.4f} seconds")
    print(f"🔢 Total attempts: {attempts:,}")

target = input("Enter the password to crack: ")
wordlist = input("Enter the path to wordlist (e.g. rockyou.txt):  ")

dictionary_attack(target, wordlist)