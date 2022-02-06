import csv
import os
from time import sleep


header = ["number","category"]
mainData = []
numLines = 0
numLines = (numLines/2)-1

fileName = "texts.csv"

def startVoting():
    
    # print(os.getcwd())
    
    if os.getcwd()[-1] != "2":
        # print(os.getcwd()[-1])
        # print("Im here")
        os.chdir("./Voter Registration P2")
    fileExists = os.path.isfile(f"./{fileName}")
    

    with open(f"./{fileName}") as file:
        readheader = csv.reader(file)
        numLines = len(list(readheader))

    for num in range(1,16):
        header.append(f"choice{num}")
        header.append(f"choice{num}-count")

    with open(f"./{fileName}", newline="") as file:
        reader = csv.DictReader(file)
        
        for i in reader:
            counter = 1
            print(f'\n{i["number"]}: {i["category"]}')
            print(numLines)
            for j in range(1,16):
                if i[f"choice{counter}"] != "":
                    print(f'[{counter}] {i[f"choice{counter}"]}')
                    counter+=1
                else:
                    break
            
            data = {}

            choicenum = 1
            counter = 1
            counterCount = 1
            data["number"] = i["number"] 
            data["category"] = i["category"]
            for k in range(1,16):
                if i[f"choice{counter}"] != "":
                    data[f"choice{counter}"] = i[f"choice{counter}"]
                    counter += 1
                if i[f"choice{counterCount}-count"] != "":
                    data[f"choice{counterCount}-count"] = int(i[f"choice{counterCount}-count"])
                    counterCount+=1

            isVoteGood = False
            while isVoteGood == False:   
                selected = input("\nEnter your vote: ")

                if selected.isdigit():
                    selected = int(selected)
                    counting = 1
                    for a in data:                    
                        if 2 * (selected + 1) == counting:
                            data[a] += 1
                            isVoteGood = True
                            break
                        counting += 1
            mainData.append(data)   
    

    filepath = f"./{fileName}"
    if(os.path.exists(filepath) and os.path.isfile(filepath)):
        os.remove(filepath)
        print("File is removed")
    else:
        print("file not found")

    sleep(2)
    with open(f"./{fileName}", 'w', encoding='UTF8', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=header)
        writer.writeheader()
        writer.writerows(mainData)

startVoting() 