import csv
import os.path

def check():

    os.chdir("./Voter Registration P2")
    fileName = "texts.csv"
    fileExists = os.path.isfile(f"./{fileName}")


    if not fileExists:
        with open(f"./{fileName}", 'w', newline='') as file:
            print(f"File not found. Making new file.\n")

    
    print("File Located!")

    with open(f"./{fileName}", 'r', newline='') as file:    
        reader = csv.reader(file)
        numLines = len(list(reader))
        print(numLines)
        if numLines == 0:
            return 0
        else:
            return 1
    
        
def grabInput():
    header = ["number","category"]
    rows = []
    headercount = []

    checkingFile = check()
    if checkingFile != 0:
        with open('./Voting Registration/make.csv') as file:    
            readerC = csv.reader(file)
            next(readerC)
            for row in readerC:
                headercount.append(int(row[0][-1]))

    count = 1
    while True:
        choicenum = 1
        print()
        question = input("Enter the question: ").strip().upper()
        if question == "" or question == 'NONE':
            break
        else:
            data = {}
            if count not in headercount:
                data["number"] = f"Question {count}"
            else: 
                data["number"] = f"Question {headercount[-1] + 1}"
                headercount.append(headercount[-1] + 1)
            data["category"] = question
            choices = []
            while True:
                choice = input("Enter choice: ").strip().upper()
                if choice == "" or choice == 'NONE':
                    break
                else:
                    if choice not in choices:
                        choices.append(choice)
                        data[f"choice{choicenum}"] = choice
                        data[f"choice{choicenum}-count"] = 0
                        if f"choice{choicenum}" not in header and f"choice{choicenum}-count" not in header:
                            header.append(f"choice{choicenum}")
                            header.append(f"choice{choicenum}-count")
                        choicenum += 1
                    else:
                        print("Already included")
        rows.append(data)
        count += 1

    answer = input("Is there a header already? ").strip().upper()
    if answer == "NO":
        with open('./Voting Registration/make.csv', 'w', encoding='UTF8', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=header)
            writer.writeheader()
            writer.writerows(rows)
    else:
        with open('./Voting Registration/make.csv', 'a', encoding='UTF8', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=header)
            writer.writerows(rows)

check()
