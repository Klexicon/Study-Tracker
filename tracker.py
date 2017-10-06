import json
import os
from datetime import datetime

test = True

def mainMenu():
    header("main")
    if not test: print("")
    print("{0}{1:38}{0}{2:38}{0}{3:38}{0}{4:38}".format("\n            "," 1. Log a study session"," 2. Display study time"," 3. Change data set"," 4. Exit"))
    print("\n Select an option: ", end="")
    return input()

def header(page):
    print("\n"+"-"*50)
    if page == "logSession":
        print("\n{:^50}".format("Session Logging"))
    elif page == "displayTime":
        print("\n{:^50}".format("Study Time by Topic"))
    elif page == "main":
        print("\n{:^50}".format("Main Menu"))

    if test:    
        print("\n{:^50}\n".format("TEST DATA ACTIVE"))
    else: print("")
    print("-"*50+"\n")

def logSession(data):
    header("logSession")

    for item in data:
        print(" "+item+". "+data[item]["name"])
    
    print("\n Which topic did you study: ",end="")
    selection = input()
    os.system('cls')
    header("logSession")
    print("\n "+selection+". "+data[selection]["name"])
    print("\n Study Duration (HH:MM or \"X\" to cancel): ",end="")
    time = input()

    if(time.upper()!="X"):
        timeMins = int(time[:2])*60+int(time[3:])
        print("\n "+data[selection]["name"]+" Updated")
        print(" Hours Studied: {0:.2f} + {1:.2f}\n".format(data[selection]["time"]/60, timeMins/60))
        data[selection]["time"] +=timeMins
        data[selection]["lastEdit"] = datetime.now().strftime('%D %H:%M:%S')
        writeJSON(data)
    else: os.system('cls')

def displayTime(data):
    allocated, studied = 0, 0
    header("displayTime")
    print("")
    for item in data:
        print(" {1:40}{0:.2f}%".format(((data[item]["time"]/60)/(data[item]["allocated"]*2))*100,data[item]["name"]))
        print("    Allocated (Hrs): {}".format(data[item]["allocated"]*2))
        print("    Studied (Hrs):   {0:.2f}".format(data[item]["time"]/60," "))
        if data[item]["lastEdit"] != "": print("    Last Edit:       {}\n".format(data[item]["lastEdit"]))
        else: print("")
        allocated+=data[item]["allocated"]*2
        studied += data[item]["time"]/60
    print(""+"-"*50)
    print(" {1:40}{0:.2f}%".format((studied/allocated)*100,"Totals"))
    print("    Allocated (Hrs): {}".format(allocated))
    print("    Studied (Hrs): {0:.2f}".format(studied))
    print(""+"-"*50)
    print("\n\n {}".format("Return to Main Menu (Y/N): "),end="")
    if input().upper() == "Y":
        os.system('cls')
    else:
        os.system('cls')
        displayTime(data)

def changeDataSet():
    global test
    test = not test
    return getJSON()

def getJSON():
    dataSet = "data.json"
    if test: dataSet= "dataTest.json"

    with open(dataSet, 'r') as infile:
        return json.load(infile)

def writeJSON(data):
    dataSet = "data.json"
    if test: dataSet= "dataTest.json"

    with open(dataSet, 'w') as outfile:
        json.dump(data, outfile)

def main():
    data = getJSON()
    while True:
        option = mainMenu()
        try:
            if option[0] == "1":
                os.system('cls')
                logSession(data)
            elif option[0] == "2":
                os.system('cls')
                displayTime(data)
            elif option[0] == "3":
                os.system('cls')
                data = changeDataSet()
            elif option[0] == "4":
                break
            else:
                break
        except:
            os.system('cls')
            print("ERROR")
if __name__ == "__main__":
    main()