import os
import re
import time
import zipfile
import shutil
import logging
import requests
import pyautogui
import webbrowser
import subprocess

from bs4 import BeautifulSoup
from urllib.parse import urljoin
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import pygetwindow as gw


session = requests.Session()
DOWNLOAD_FOLDER = r"D:\Cuong\Downloads"
EXTRACT_FOLDER = r"D:\Cuong\CODING\NETRUYENEXTRACTFILE"
EXTRACT_IMAGE=r'D:\Cuong\CODING\NETRUYENALLIMAGE'



image_extensions = ('.png', '.jpg', '.jpeg', '.bmp', '.webp')
allchapters = []
folder="Ntruyenallchapters"
os.makedirs(folder, exist_ok=True)
t=0
a=1
chaptersoup=0
def get_all_links():
    urls = [f"https://nettruyenvie.com/?page={i}" for i in range(2, 101)]
    for item in urls:
        net=requests.get(item)
        soup=BeautifulSoup(net.text, "html.parser")

            

        h3_tags = soup.find_all("h3")



        with open("titlelist.txt", "w", encoding="utf-8") as f:
            for h3 in h3_tags:
                a_tag = h3.find("a", class_="jtip")
                if a_tag:
                    title = a_tag.text.strip()
                    f.writelines(title + "\n")
            
        with open("Linkdown.txt", "w", encoding="utf-8") as f:
            for h3 in h3_tags:
                a_tag = h3.find("a", class_="jtip")
                if a_tag and a_tag.get("href"):
                    href = a_tag.get("href")
                    

                    f.writelines(href + "\n")
                    

                    # arr1.clear()
        with open("Linkdown.txt", "r", encoding="utf-8") as f:
            linkdown = f.readlines()
        with open("Linkalr.txt", "r", encoding="utf-8") as f:
            linkalr = f.readlines()
                    
        linkdownfinal = []
        linkdownfinal = [i for i in linkdown if not i in linkalr]
        with open("Linkdownfinal.txt", "a", encoding="utf-8") as f:
            for i in linkdownfinal:
                f.writelines(i)

        with open("titlelist.txt", "r", encoding="utf-8") as f:
            titlelist = f.readlines()
        titlelistfinal = []
        titlelistfinal = [ titlelist[i] for i in range(len(linkdownfinal))]
        with open("titlelistfinal.txt", "a", encoding="utf-8") as f:
            for i in titlelistfinal:
                f.writelines(i)
        linkalr1 = []
        linkalr1 = linkalr + linkdownfinal
        with open("Linkalr.txt", "a", encoding="utf-8") as f:
            for i in linkalr1:
                if i not in linkalr:
                    f.writelines(i)
        if all(item in linkalr for item in linkdown):
            break
    return linkdownfinal ,titlelistfinal






    
def getmaxchapter():
    with open(filepath, "a", encoding="utf-8") as f:
        with open(filepath, "r", encoding="utf-8") as file:
                
                
            repeatedmaxchapter = [line.strip() for line in file.readlines()]
            
            
            soup = BeautifulSoup(session.get(item.strip()).text, "html.parser")
            soup1 = soup.find_all("div", class_="col-xs-5 chapter")
            soup2 = [i.find("a") for i in soup1]

            linkchaptermax = soup2[0]["href"]
            chaptermax1 = []
            chaptermax = linkchaptermax[-5:]
            

            for i in chaptermax:
                if i.isdigit() or i == ".":
                    chaptermax1.append(i)
            if '.' in chaptermax1:
                chaptermax2 = float("".join(chaptermax1))
            else:
                chaptermax2 = int("".join(chaptermax1))
        
            
            chaptermax3 = str("/chuong-" + str(chaptermax2))
            allchapter = item.strip() + chaptermax3
            if not allchapter in repeatedmaxchapter:
                
                f.writelines(str(allchapter) + "\n")
                chaptermax2= str(chaptermax2)
                f.writelines(f'Chapter {chaptermax2}' + "\n")
                
            chaptermax2= str(chaptermax2)
            return allchapter

def get_chapter(allchapter):
    a=1
    
    chaptersoup=0
    chaptersoup1 = []
    soupv1 = BeautifulSoup(session.get(allchapter).text, "html.parser")
    soupv2 = soupv1.find("div", class_="chapter-nav")
    soupv3 = soupv2.find_all("a", href=True)
    soupv4 = [i["href"] for i in soupv3] 

    chaptersoup = soupv4[3][-5:]
    for i in chaptersoup:
                if i.isdigit() or i == ".":
                    chaptersoup1.append(i)
    if '.' in chaptersoup1:
        chaptersoup = float("".join(chaptersoup1))
    else:
        chaptersoup = int("".join(chaptersoup1))
    chaptersoup = str(chaptersoup)     
    if soupv4[3] in allchapters:
        a = 0
        allchapters.append(f"Chapter {chaptersoup}")
    else:
        allchapters.append(soupv4[3])
        allchapters.append(f"Chapter {chaptersoup}")
    

    
    return soupv4[3],a,allchapters,chaptersoup





def download_links(item):
    time.sleep(2)
    
    webbrowser.open(item.strip())
    time.sleep(4)
    pyautogui.press('f12')
    time.sleep(2)
    pyautogui.moveTo(1358, 133)
    pyautogui.click()
    time.sleep(1)
    pyautogui.moveTo(1277, 251)
    pyautogui.click()
    time.sleep(1)
    pyautogui.moveTo(1277, 365)
    pyautogui.click()
    time.sleep(1)
    pyautogui.moveTo(1798, 204)
    pyautogui.click()
    time.sleep(7)
    pyautogui.moveTo(255, 19)
    pyautogui.click()
    time.sleep(1)

def extractzip(item):
    zips = [f for f in os.listdir(DOWNLOAD_FOLDER) if f.endswith(".zip")]

    for zip_file in zips:
        zip_path = os.path.join(DOWNLOAD_FOLDER, zip_file)

        try:
            # Extract the ZIP file to a temp folder
            with zipfile.ZipFile(zip_path, 'r') as zip_ref:
                zip_ref.extractall(EXTRACT_FOLDER)

            # Move all images from temp to EXTRACT_IMAGE
            for dirpath, _, filenames in os.walk(EXTRACT_FOLDER):
                for filename in filenames:
                    if filename.lower().endswith(image_extensions):
                        src = os.path.join(dirpath, filename)
                        dst = os.path.join(EXTRACT_IMAGE, filename)
                        shutil.copy2(src, dst)

            # Clean up extracted folders
            for folder in os.listdir(EXTRACT_FOLDER):
                full_folder = os.path.join(EXTRACT_FOLDER, folder)
                if os.path.isdir(full_folder):
                    shutil.rmtree(full_folder)

            # Remove the original ZIP
            os.remove(zip_path)

            # Prepare subfolder based on item
           
            subfolder_name = item[38:].strip('/')
          
            target_folder = os.path.join(EXTRACT_IMAGE, subfolder_name)
            os.makedirs(target_folder, exist_ok=True)

            # Check if there's an image matching the folder name
            matched_file = None
            for filename in os.listdir(EXTRACT_IMAGE):
                path = os.path.join(EXTRACT_IMAGE, filename)
                if os.path.isdir(path):
                    continue
                name_only, ext = os.path.splitext(filename)
                if name_only == subfolder_name:
                    matched_file = filename
                    break

            # Clean and sort images into the subfolder
            for filename in os.listdir(EXTRACT_IMAGE):
                src_path = os.path.join(EXTRACT_IMAGE, filename)

                if os.path.isdir(src_path):
                    continue  # Skip folders

                name_only, ext = os.path.splitext(filename)

                if matched_file:
                    # If match exists, only keep that one
                    if filename == matched_file:
                        shutil.move(src_path, os.path.join(target_folder, filename))
                    else:
                        os.remove(src_path)
                else:
                    # If no match, keep only numeric-named files
                    if name_only.isdigit():
                        shutil.move(src_path, os.path.join(target_folder, filename))
                    else:
                        os.remove(src_path)

        except Exception as e:
            logging.error(f"Error extracting {zip_file}: {e}")




if __name__ == "__main__":
    
    get_all_links()
    with open('Linkdownfinal.txt', "r", encoding="utf-8") as f:
        linkdownfinal = f.readlines()
    with open('titlelistfinal.txt', "r", encoding="utf-8") as f:
        titlelistfinal = f.readlines()
    
    for item,titlee in zip(linkdownfinal,titlelistfinal):
        
        
        sanitized_item = re.sub(r'[<>:"/\\|?*\n]', '_', item.strip())
        filepath = os.path.join(folder,f"{sanitized_item}.txt")
        with open(filepath, "a", encoding="utf-8") as ff:
            ff.write(item.strip() + "\n")
            ff.write(titlee.strip() + "\n")
        allchapter = getmaxchapter()
        download_links(item.strip())
        time.sleep(2)
        extractzip(item.strip())
        time.sleep(1)
        download_links(allchapter)
        time.sleep(2)
        
        extractzip(allchapter)
        time.sleep(1)
        while a==1:
            allchapter,a,allchapters,chaptersoup = get_chapter(allchapter)
            
            
        with open(filepath, "r", encoding="utf-8") as f:
                stripped_line = []
                dupli=f.readlines()
                for i in dupli:
                    stripped_line.append(i.strip())
                
        with open(filepath, "a", encoding="utf-8") as f:
            



            for ii in allchapters[:-1]:
                if ii not in stripped_line:
                    
                    f.writelines(ii + "\n")
        for iii in allchapters:
            if isinstance(iii, str) and iii.startswith("http"):

                download_links(iii)
                time.sleep(2)
                
                extractzip(iii)
                time.sleep(1)
        allchapters=[]
        a=1
    

        