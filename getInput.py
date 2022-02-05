import csv
import os.path

fileName = "texts.csv"

# Function checks if file exists in the said directory.
def check():
    os.chdir("./Voter Registration P2")
    fileExists = os.path.isfile(f"./{fileName}")

    # Creates a new file if file does not exist
    if not fileExists:
        with open(f"./{fileName}", 'w', newline='') as file:
            print(f"File not found. Making new file.\n")

    
    print("File Located!")

    # Determines if file contains existing questions and choices
    with open(f"./{fileName}", 'r', newline='') as file:    
        reader = csv.reader(file)
        numLines = len(list(reader))
        # print(numLines)
        return numLines
    

# Asks user for inputs
def grabInput():

    # Initialized variables
    header = ["number","category"]
    rows = []
    headercount = []

    checkingFile = check()

    # Gets the question number and stores it to headercount. Keeps track on what question number was the last
    if checkingFile != 0:
        with open(f"./{fileName}") as file:    
            readerC = csv.reader(file)
            next(readerC)
            for row in readerC:
                if row[0][-2] != " ":
                    headercount.append(int(row[0][:-3:-1][::-1]))
                else:
                    headercount.append(int(row[0][-1]))

    count = 1
    while True:
        # print(headercount)
        choicenum = 1
        print()
        question = input("Enter the question: ").strip().upper()
        if question == "" or question == 'NONE':
            break
        else:
            data = {}
            print(data)
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
        with open(f"./{fileName}", 'w', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=header)
            writer.writeheader()
            writer.writerows(rows)
    else:
        with open(f"./{fileName}", 'a', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=header)
            writer.writerows(rows)

grabInput()
