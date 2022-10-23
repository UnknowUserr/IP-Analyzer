import os

print("[+] Installation...")
print("")
os.system("pip install colorama")
os.system("pip install pystyle")	
os.system("pip install animation")	
os.system("cls")

try:
	import requests, animation, time
	from pystyle import Anime, Colors, Center, System, Write, Colorate
except ModuleNotFoundError:
	print("An error has been detected...")

System.Title("IP Analyzer")
os.system("cls")

p = "IP Analyzer"
Anime.Fade(text=Center.Center(p), color=Colors.black_to_green, mode=Colorate.Vertical, time=3)

"""
@author: ! Xerox ' ✞#8329
"""

ip = Write.Input("Adresse IP -> ", Colors.green, interval=0.002, input_color=Colors.white)

def Xerox():
    res = requests.post(
        f'http://ip-api.com/json/{ip}?fields=61439',
    )

    data = res.json()

    Write.Print("\nPays : " + data['country'] + ", " + data['countryCode']+ "\n", Colors.white, interval=0.002)
    Write.Print("Région : " + data['regionName'] + "\n", Colors.white, interval=0.002)
    Write.Print("Ville : " + data['city'] + "\n", Colors.white, interval=0.002)
    Write.Print("Code Postal : " + data['zip'] + "\n", Colors.white, interval=0.002)
    Write.Print("IP : " + data['query'] + "\n", Colors.white, interval=0.002)
    Write.Print("Opérateur : " + data['isp'] + "\n", Colors.white, interval=0.002)

def dl():
    res = requests.post(
        f'http://ip-api.com/json/{ip}?fields=61439',
    )

    data = res.json()
    
    do = input(f"\nVeux-tu télécharger toute les informations sur {ip} [y,n] ? -> ")

    if do == "y":
        @animation.wait('elipses ', color='green' ,text="\nTéléchargement des données")
        def long_running_function():
            time.sleep(5)
        long_running_function()

        Write.Print("Téléchargement terminé", Colors.green, interval=0.002)

        with open("data_analyzer.txt", "w+") as XFile:
            XFile.write(str(data))
            XFile.close
    elif do == "n":
        print("")

if __name__ == '__main__':
	Xerox()
	dl()
