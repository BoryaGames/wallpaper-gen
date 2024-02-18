import requests
import ctypes
import json
import os
import winreg
from colorama import Fore
import shutil
import asyncio
from config import CAT_API, NINJAS_API

headars = {
    'x-api-key' : CAT_API
}

header2 = {
    "X-Api-Key": NINJAS_API,
    "Accept": "image/jpg"
}

red = Fore.RED
yellow = Fore.YELLOW
green = Fore.GREEN
orange = Fore.RED + Fore.YELLOW
pretty = Fore.LIGHTMAGENTA_EX + Fore.LIGHTCYAN_EX
magenta = Fore.MAGENTA
lightblue = Fore.LIGHTBLUE_EX
cyan = Fore.CYAN
gray = Fore.LIGHTBLACK_EX + Fore.WHITE
reset = Fore.RESET
pink = Fore.LIGHTGREEN_EX + Fore.LIGHTMAGENTA_EX


gen = True

async def wildlife():
    try:
        os.remove("./images/wallpaper.jpg")
    except FileNotFoundError:
        print("Cant delete picture")
    global gen, header2
    try:
        resp = requests.get("https://api.api-ninjas.com/v1/randomimage?category=wildlife&width=2560&height=1440", headers=header2, stream=True)
    except Exception as e:
        print(e)
    with open('./images/wallpaper.jpg', 'wb') as file:
        shutil.copyfileobj(resp.raw, file)
        file.close()
        path = "C:\\Users\\Дима\\Desktop\\wallpaper\\images\\wallpaper.jpg"
        key = r"Control Panel\Desktop"
        value_name = "Wallpaper"
        with winreg.OpenKey(winreg.HKEY_CURRENT_USER, key, 0, winreg.KEY_WRITE) as reg_key:
            winreg.SetValueEx(reg_key, value_name, 0, winreg.REG_SZ, path)
        SPI_SETDESKWALLPAPER = 0x14
        SPIF_UPDATEINIFILE = 0x2
        ctypes.windll.user32.SystemParametersInfoW(SPI_SETDESKWALLPAPER, 0, path , SPIF_UPDATEINIFILE)
        print("Successfully\nwidth 1920, height 1080")
        await asyncio.sleep(3)


async def abstract():
    try:
        os.remove("./images/wallpaper.jpg")
    except FileNotFoundError:
        print("Cant delete picture")
    global gen, header2
    try:
        resp = requests.get("https://api.api-ninjas.com/v1/randomimage?category=abstract&width=2560&height=1440", headers=header2, stream=True)
    except Exception as e:
        print(e)
    with open('./images/wallpaper.jpg', 'wb') as file:
        shutil.copyfileobj(resp.raw, file)
        file.close()
        path = "C:\\Users\\Дима\\Desktop\\wallpaper\\images\\wallpaper.jpg"
        key = r"Control Panel\Desktop"
        value_name = "Wallpaper"
        with winreg.OpenKey(winreg.HKEY_CURRENT_USER, key, 0, winreg.KEY_WRITE) as reg_key:
            winreg.SetValueEx(reg_key, value_name, 0, winreg.REG_SZ, path)
        SPI_SETDESKWALLPAPER = 0x14
        SPIF_UPDATEINIFILE = 0x2
        ctypes.windll.user32.SystemParametersInfoW(SPI_SETDESKWALLPAPER, 0, path , SPIF_UPDATEINIFILE)
        print("Successfully\nwidth 1920, height 1080")
        await asyncio.sleep(3)


async def still_life():
    try:
        os.remove("./images/wallpaper.jpg")
    except FileNotFoundError:
        print("Cant delete picture")
    global gen, header2
    try:
        resp = requests.get("https://api.api-ninjas.com/v1/randomimage?category=still_life&width=2560&height=1440", headers=header2, stream=True)
    except Exception as e:
        print(e)
    with open('./images/wallpaper.jpg', 'wb') as file:
        shutil.copyfileobj(resp.raw, file)
        file.close()
        path = "C:\\Users\\Дима\\Desktop\\wallpaper\\images\\wallpaper.jpg"
        key = r"Control Panel\Desktop"
        value_name = "Wallpaper"
        with winreg.OpenKey(winreg.HKEY_CURRENT_USER, key, 0, winreg.KEY_WRITE) as reg_key:
            winreg.SetValueEx(reg_key, value_name, 0, winreg.REG_SZ, path)
        SPI_SETDESKWALLPAPER = 0x14
        SPIF_UPDATEINIFILE = 0x2
        ctypes.windll.user32.SystemParametersInfoW(SPI_SETDESKWALLPAPER, 0, path , SPIF_UPDATEINIFILE)
        print("Successfully\nwidth 1920, height 1080")
        await asyncio.sleep(3)


async def food():
    try:
        os.remove("./images/wallpaper.jpg")
    except FileNotFoundError:
        print("Cant delete picture")
    global gen, header2
    try:
        resp = requests.get("https://api.api-ninjas.com/v1/randomimage?category=food&width=2560&height=1440", headers=header2, stream=True)
    except Exception as e:
        print(e)
    with open('./images/wallpaper.jpg', 'wb') as file:
        shutil.copyfileobj(resp.raw, file)
        file.close()
        path = "C:\\Users\\Дима\\Desktop\\wallpaper\\images\\wallpaper.jpg"
        key = r"Control Panel\Desktop"
        value_name = "Wallpaper"
        with winreg.OpenKey(winreg.HKEY_CURRENT_USER, key, 0, winreg.KEY_WRITE) as reg_key:
            winreg.SetValueEx(reg_key, value_name, 0, winreg.REG_SZ, path)
        SPI_SETDESKWALLPAPER = 0x14
        SPIF_UPDATEINIFILE = 0x2
        ctypes.windll.user32.SystemParametersInfoW(SPI_SETDESKWALLPAPER, 0, path , SPIF_UPDATEINIFILE)
        print("Successfully\nwidth 1920, height 1080")
        await asyncio.sleep(3)


async def city():
    try:
        os.remove("./images/wallpaper.jpg")
    except FileNotFoundError:
        print("Cant delete picture")
    global gen, header2
    try:
        resp = requests.get("https://api.api-ninjas.com/v1/randomimage?category=city&width=2560&height=1440", headers=header2, stream=True)
    except Exception as e:
        print(e)
    with open('./images/wallpaper.jpg', 'wb') as file:
           shutil.copyfileobj(resp.raw, file)
           file.close()
           path = "C:\\Users\\Дима\\Desktop\\wallpaper\\images\\wallpaper.jpg"
           key = r"Control Panel\Desktop"
           value_name = "Wallpaper"
           with winreg.OpenKey(winreg.HKEY_CURRENT_USER, key, 0, winreg.KEY_WRITE) as reg_key:
               winreg.SetValueEx(reg_key, value_name, 0, winreg.REG_SZ, path)
           SPI_SETDESKWALLPAPER = 0x14
           SPIF_UPDATEINIFILE = 0x2
           ctypes.windll.user32.SystemParametersInfoW(SPI_SETDESKWALLPAPER, 0, path , SPIF_UPDATEINIFILE)
           print("Successfully\nwidth 1920, height 1080")
           await asyncio.sleep(3)


async def technology():
    try:
        os.remove("./images/wallpaper.jpg")
    except FileNotFoundError:
        print("Cant delete picture")
    global gen, header2
    try:
        resp = requests.get("https://api.api-ninjas.com/v1/randomimage?category=technology&width=2560&height=1440", headers=header2, stream=True)
    except Exception as e:
        print(e)
    with open('./images/wallpaper.jpg', 'wb') as file:
        shutil.copyfileobj(resp.raw, file)
        file.close()
        path = "C:\\Users\\Дима\\Desktop\\wallpaper\\images\\wallpaper.jpg"
        key = r"Control Panel\Desktop"
        value_name = "Wallpaper"
        with winreg.OpenKey(winreg.HKEY_CURRENT_USER, key, 0, winreg.KEY_WRITE) as reg_key:
            winreg.SetValueEx(reg_key, value_name, 0, winreg.REG_SZ, path)
        SPI_SETDESKWALLPAPER = 0x14
        SPIF_UPDATEINIFILE = 0x2
        ctypes.windll.user32.SystemParametersInfoW(SPI_SETDESKWALLPAPER, 0, path , SPIF_UPDATEINIFILE)
        print("Successfully\nwidth 1920, height 1080")
        await asyncio.sleep(3)
    

async def nature():
    try:
        os.remove("./images/wallpaper.jpg")
    except FileNotFoundError:
        print("Cant delete picture")
    global gen, header2
    try:
        resp = requests.get("https://api.api-ninjas.com/v1/randomimage?category=nature&width=2560&height=1440", headers=header2, stream=True)
    except Exception as e:
        print(e)
    with open('./images/wallpaper.jpg', 'wb') as file:
        shutil.copyfileobj(resp.raw, file)
        file.close()
        path = "C:\\Users\\Дима\\Desktop\\wallpaper\\images\\wallpaper.jpg"
        key = r"Control Panel\Desktop"
        value_name = "Wallpaper"
        with winreg.OpenKey(winreg.HKEY_CURRENT_USER, key, 0, winreg.KEY_WRITE) as reg_key:
            winreg.SetValueEx(reg_key, value_name, 0, winreg.REG_SZ, path)
        SPI_SETDESKWALLPAPER = 0x14
        SPIF_UPDATEINIFILE = 0x2
        ctypes.windll.user32.SystemParametersInfoW(SPI_SETDESKWALLPAPER, 0, path , SPIF_UPDATEINIFILE)
        print("Successfully\nwidth 1920, height 1080")
        await asyncio.sleep(3)
    

async def cats():

    global gen
    while gen == True:
        
        try:
            os.remove("./images/wallpaper.jpg")
        except FileNotFoundError:
            print("Cant delete picture")
            
        try:
            resp = requests.get("https://api.thecatapi.com/v1/images/search?limit=1", headers=headars).json()
        except requests.RequestsJSONDecodeError:
            print("Рейт лимит")
        print("Получил ответ")
        img = resp[0]["url"]
        width = resp[0]["width"]
        height = resp[0]["height"]
        img2 = requests.get(img)
        if width == round(1.777777777777778 * height) and not img.endswith(".gif"):
                with open("./images/" + img.split("/")[-1], "wb") as file:
                    img3 = img.split("/")[-1]
                    print("0 получил " + img3)
                    file.write(img2.content)
                    file.close()
                    print("1 Получил " + img3)
                    os.rename("./images/" + img.split("/")[-1]  , "./images/wallpaper.jpg")
                    gen = False
                    print("Успешно записал файл!")
                    path = os.path.abspath("./images/wallpaper/jpg")
                    key = r"Control Panel\Desktop"
                    value_name = "Wallpaper"
                    with winreg.OpenKey(winreg.HKEY_CURRENT_USER, key, 0, winreg.KEY_WRITE) as reg_key:
                        winreg.SetValueEx(reg_key, value_name, 0, winreg.REG_SZ, path)
                    SPI_SETDESKWALLPAPER = 0x14
                    SPIF_UPDATEINIFILE = 0x2
                    ctypes.windll.user32.SystemParametersInfoW(SPI_SETDESKWALLPAPER, 0, path , SPIF_UPDATEINIFILE)
                    print(f"Successfully\nWidth {width}, Height {height}")
                    await asyncio.sleep(3)
        else:
            print("The picture doesn't fit")


async def main():
    print(f"""{magenta}
    ____      __      _       __      ____                                
   /  _/___  / /__   | |     / /___ _/ / /___  ____ _____  ___  __________
   / // __ \/ //_/   | | /| / / __ `/ / / __ \/ __ `/ __ \/ _ \/ ___/ ___/
 _/ // / / / ,<      | |/ |/ / /_/ / / / /_/ / /_/ / /_/ /  __/ /  (__  ) 
/___/_/ /_/_/|_|     |__/|__/\__,_/_/_/ .___/\__,_/ .___/\___/_/  /____/  
                                     /_/         /_/                    
    """)
    print(f"""{reset}{cyan}
        Choose variant
          
      1. Cats (not stable idk)
      2. Nature
      3. City
      4. Technology
      5. Food
      6. Still life
      7. Abstract
      8. Wildlife
      (1-8)
{reset}""")
    choose = input()

    if choose == "1":
        await cats()
        await main()
    elif choose == "2":
        await nature()
        await main()
    elif choose == "3":
        await city()
        await main()
    elif choose == "4":
        await technology()
        await main()
    elif choose == "5":
        await food()
        await main()
    elif choose == "6":
        await still_life()
        await main()
    elif choose == "7":
        await abstract()
        await main()
    elif choose == "8":
        await wildlife()
        await main()    
    else:
        print(f"{red}Choose from 1 to 8!")
        await asyncio.sleep(1)
        clear = lambda: os.system('cls')
        clear()
        await main()

asyncio.run(main())