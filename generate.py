#!/usr/bin/python3
#coding=utf-8

import os
import sys
import time
import json
import random
import socket
import shutil
import webbrowser
import concurrent.futures

try:
    __import__('requests')
except ModuleNotFoundError:
    os.system('pip3 install requests')
finally:
    import requests

try:
    __import__('bs4')
except ModuleNotFoundError:
    os.system("pip3 install bs4")
finally:
    from bs4 import BeautifulSoup as parser

UPDATE = "10-11-2021 13:07"

if 'linux' in sys.platform:
    r = "\033[91m"  # Red
    g = "\033[92m"  # Green
    y = "\033[93m"  # Yellow
    p = "\033[94m"  # Purple
    P = "\033[95m"  # Pink
    c = "\033[96m"  # Cyan
    w = "\033[97m"  # White
    a = "\033[0m"   # Reset
else:
    for i in ['r', 'g', 'y', 'p', 'P', 'c', 'w', 'a']:
        globals()[i] = ""

try:
    print(f"{p}[{y}!{p}] {r}Connecting to the server...")
    data = requests.get("https://www.mediafire.com/api/1.4/folder/get_content.php?content_type=files&filter=all&order_by=name&order_direction=asc&chunk=1&version=1.5&folder_key=ueti9cij4zf3i&response_format=json").json()
    files = data['response']['folder_content']['files']
except requests.exceptions.RequestException:
    exit(f"{p}[{y}!{p}] {r}No connection!{a}")

colors = lambda: random.choice([r, g, y, p, P, c, w])
logo = f"{r}****     **** *******     **     **\n/**/**   **/**/**////**   //**   ** \n/**//** ** /**/**   /**    //** **  \n/** //***  /**/*******      //***   \n/**  //*   /**/**///**       **/**  \n/**   /    /**/**  //**     ** //** \n/**        /**/**   //**   **   //**\n//         // //     //   //     //\n{p}========================================\n{p}[{y}Author{p}] {c}: {g}N4tzzSquadCommunity {p}\n{p}[{y}GitHub{p}] {c}: {w}github.com/N4tzz-Official/{p}\n{p}[{y}Website{p}] {c}: {y}www.n4tzzsquadofficial.ct.ws / nzsq.ct.ws {p}\n{p}[{y}Update{p}] {c}: {UPDATE} {p}\n{p}[{y}Python{p}] {c}: {colors()}{sys.version[0:6]} {p}\n{p}[{y}OS{p}] {c}: {colors()}{sys.platform}{p}\n{p}[{y}Host{p}] {c}: {colors()}{socket.gethostname()}{p}\n{p}[{y}Team{p}] {c}: {colors()}N4tzz {colors()}Squad {r}Community{p}\n========================================{a}"

try:
    os.mkdir('virtex')
except FileExistsError:
    pass

def download_file(file):
    with requests.Session() as session:
        print(f"{p}[{y}!{p}] {y}Downloading {file['filename']}")
        response = session.get(file['links']['normal_download'])
        parsed = parser(response.content, 'html.parser').find('a', class_='popsok')['href']
        content = session.get(parsed).content
        filepath = os.path.join('virtex', file['filename'])
        with open(filepath, 'wb') as f:
            f.write(content)

def main_menu():
    try:
        os.system('clear')
        print(logo)
        print(f"{g}SELECT VIRTEX TYPE")
        print(f"{c}{'=' * 43}{a}")
        for index, file in enumerate(files, start=1):
            print(f"{p}[{r}{str(index).zfill(2)}{p}] {colors()}{os.path.splitext(file['filename'])[0]}")
        print(f"{p}[{r}ALL{p}] {c}DOWNLOAD ALL VIRTEX")
        print(f"{p}[{r}BACK{p}] {y}GO BACK TO MAIN MENU")
        print(f"{p}[{r}EXIT{p}] {r}EXIT THE PROGRAM")
        choice = input(f"{g}>>>> {c}").lower()

        if choice == 'all':
            with concurrent.futures.ThreadPoolExecutor(15) as executor:
                executor.map(download_file, files)
            shutil.make_archive('virtex-master', 'zip', 'virtex')
            print(f"{p}[{g}✓{p}] {g}Download complete")
            exit(f"{p}[{g}✓{p}] {g}Download results saved in: {os.path.realpath('virtex')}")
        elif choice == 'back':
            main()
        elif choice == 'exit':
            os.abort()
        elif int(choice) in range(1, len(files) + 1):
            selected_file = files[int(choice) - 1]
            print(f"{p}[{y}!{p}] {y}Downloading {selected_file['filename']}")
            try:
                download_file(selected_file)
                print(f"{p}[{g}✓{p}] {g}Download complete for {selected_file['filename']}")
                main_menu()
            except Exception as e:
                print(f"{p}[{y}!{p}] {r}Error: {str(e)}")
        else:
            raise ValueError()
    except ValueError:
        print(f"{y}[!] Invalid input!")
        time.sleep(1)
        main_menu()

def main():
    os.system('clear')
    print(logo)
    print(f"{g}MAIN MENU")
    print(f"{c}{'=' * 37}{a}")
    print(f"{p}[{y}1{p}] {g}DOWNLOAD VIRTEX FILES")
    print(f"{p}[{y}2{p}] {y}REPORT BUGS")
    print(f"{p}[{y}3{p}] {y}ABOUT")
    print(f"{p}[{y}0{p}] {r}EXIT")
    choice = input(f"{y}>>> {c}")
    if choice == '1':
        main_menu()
    elif choice == '2':
        url = "mailto:N4tzzOfficial@proton.me"
        webbrowser.open(url)
        time.sleep(0.9)
        main()
    elif choice == '3':
        os.system('clear')
        print(f"{logo}\n{g}SCRIPT INFO\n========================\n{p}[{y}Author{p}] {c}: {g}N4tzzSquadCommunity {p}\n{p}[{y}GitHub{p}] {c}: {w}github.com/https://github.com/N4tzz-Official/ {p}\n{p}[{y}Website{p}] {c}: {y}www.n4tzzsquadofficial.ct.ws / nzsq.ct.ws {p}\n{p}[{y}Update{p}] {c}: {UPDATE} {p}\n{p}[{y}Python{p}] {c}: {sys.version[0:6]} {p}\n")
    elif choice == '0':
        os.abort()
    else:
        print(f"{y}[!] Invalid input!")
        time.sleep(0.9)
        main()

if __name__ == "__main__":
    main()
