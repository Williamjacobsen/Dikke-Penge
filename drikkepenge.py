import json
import os
import time

def clear():
    if os.name == 'nt': # hvis det er windows
        os.system('cls')
    else: # linux eller mac
        os.system('clear')

def menu():
    print(""" /$$$$$$$            /$$ /$$       /$$                       /$$$$$$$                                        
    | $$__  $$          |__/| $$      | $$                      | $$__  $$                                       
    | $$  \ $$  /$$$$$$  /$$| $$   /$$| $$   /$$  /$$$$$$       | $$  \ $$ /$$$$$$  /$$$$$$$   /$$$$$$   /$$$$$$ 
    | $$  | $$ /$$__  $$| $$| $$  /$$/| $$  /$$/ /$$__  $$      | $$$$$$$//$$__  $$| $$__  $$ /$$__  $$ /$$__  $$
    | $$  | $$| $$  \__/| $$| $$$$$$/ | $$$$$$/ | $$$$$$$$      | $$____/| $$$$$$$$| $$  \ $$| $$  \ $$| $$$$$$$$
    | $$  | $$| $$      | $$| $$_  $$ | $$_  $$ | $$_____/      | $$     | $$_____/| $$  | $$| $$  | $$| $$_____/
    | $$$$$$$/| $$      | $$| $$ \  $$| $$ \  $$|  $$$$$$$      | $$     |  $$$$$$$| $$  | $$|  $$$$$$$|  $$$$$$$
    |_______/ |__/      |__/|__/  \__/|__/  \__/ \_______/      |__/      \_______/|__/  |__/ \____  $$ \_______/
                                                                                              /$$  \ $$          
                                                                                             |  $$$$$$/          
                                                                                              \______/           
    Lavet af William
    """)

def loading(s: str, interval: int): # load, en tekst med 10 "." efter over 1 sekund
    for i in range(interval): # antal "."'s du vil have
        print(s + "."*i, end='\r') # \r gør std outputet replacable
        time.sleep(0.1)
    print("")

def json_checker(): # hvis der ikke er en fil, eller filen er tom
    # check om filen findes
    try: # prøv at åbne, men hvis den ikke er der, trower den en IOError
        f = open("service.json", "r")
        f.close()
    except IOError as e: # hvis filen ikke findes
        # (IOError er en os relateret error f.eks hvis den ikke kan åbne en fil)
        print(e)
        print("")
        loading("[Creating file 'service.json' in current directory]", 5)
        os.system("type nul > service.json") # lav en ny fil
        print("['service.json' successfully created]\n")
    
    # formatter filen hvis den er tom
    isEmptyFile = False
    with open("service.json", "r") as f:
        if f.read() == "": # hvis den er tom
            loading("[Formatting 'service.json']", 5)
            isEmptyFile = True
        f.close()
    if isEmptyFile:
        with open("service.json", "w") as f:
            json.dump(json.loads("""{"Messages": []}"""), f, indent=4) # formatter filen
            print("[Succesfully formatted 'service.json']")
            f.close()
    print()

def save_to_json(message: str):
    with open("service.json", "r") as f:
        print("")
        loading("[Saving to 'service.json']", 5)
        data = json.loads(f.read()) # "loads" går så jeg kan tilgå json obj
        data["Messages"].append(str(message))
        f.close()

    with open("service.json", "w") as f:
        json.dump(data, f, indent=4)
        print("[Succesfully saved message to 'service.json']")
        f.close()

def getInput(usrQuestion: str) -> int: # modtag et positivt heltal
    usrInput = 0
    while usrInput <= 0: # bliv ved indtil den modtager et positivt heltal
        try: # hvis de skriver et bogstav er der en error
            usrInput = int(input(usrQuestion)) # vi for et heltal som input
            if usrInput <= 0: # hvis det er mindre end eller det samme som 0
                print("[Number is to low]")
        except Exception: 
            # hvis der sker en error 
            # (Exception gælder kun typiske error og 
            # ikke hvis brugeren prøver at stoppe programmet ved at trykke ctrl+c)
            print("[Input is not a number]")
            usrInput = 0 # så den fortsætter unden errors
    return usrInput # returner input hvis den er succesfuldt

def calculateTip(totalPrice: int, tipProcent: int) -> int: 
    # tror virklig ikke det er nødvendigt er srkive noter her :)
    print("")
    loading("Calculating tip", 10)
    print("")
    return totalPrice/tipProcent

if __name__ == "__main__": 
    # gør programmet hvis filen er kaldt dirkete 
    # (ikke importeret fra en anden fil)

    clear() # ryd terminal
    menu() # vis ascii
    json_checker() # lav json fil og formatter filen
    
    totalPrice = getInput("Beløb på regningen: ") 
    tipProcent = getInput("Hvor mange procent vil du give: ")
    tip = calculateTip(totalPrice, tipProcent)
    
    print(f"Drikkepenge: {tip:.2f}") # print med 2 cifre
    print(f"Total beløb: {int(totalPrice + tip)}\n") # print beløb som heltal

    message = input("Hvad synes du om servicen: ")
    save_to_json(message)
