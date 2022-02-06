import csv
import os.path

# fileName = "texts.csv"

# Function checks if file exists in the said directory.
def check(fileName):
    # print(os.getcwd())
    
    # Goes to specific deritory (Removed because program should only run on directory it currently is in.)
    # if os.getcwd()[-1] != "2":
        # print(os.getcwd()[-1])
        # print("Im here")
        # os.chdir("./Voter Registration P2")
    
    # Checks  if file exist
    fileExists = os.path.isfile(f"./{fileName}")
    
    # Creates a new file if file does not exist
    if not fileExists:
        with open(f"./{fileName}", 'w', newline='') as file:
            print(f"File not found. Making new file.\n")

    # Determines if file contains existing questions and choices
    with open(f"./{fileName}", 'r', newline='') as file:    
        reader = csv.reader(file)
        numLines = len(list(reader))
        return numLines, fileExists
    
    # Removed! Reason: Program can add new question to existing files.
    # else:
    #     print("File cannot be modified!")
    #     return -1
    

# Asks user for inputs
def grabInput(fileName):

    # Initialized variables
    header = ["number","category"]
    rows = []
    headercount = []

    checkingFile, fileExisting = check(fileName)
    
    # print(checkingFile)

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

    # Makes header choice number and choice counter. This fixes the bug when adding new question to existing file, it automatically adds a specific number of blank/columns/commas.
    for num in range(1,16):
        header.append(f"choice{num}")
        header.append(f"choice{num}-count")

    # Gets questions and choices
    count = 1
    while True:
        # Choicenum: choice number when outputted for user. (e.g [1])
        choicenum = 1
        print()

        question = input("Enter the question [Leave blank if no additional question]: ").strip().upper()

        # Stops the program from asking user for questions.
        if question == "" or question == 'NONE':
            break
        
        else:
            # Initialized variable for storing of information
            data = {}

            if count not in headercount:
                data["number"] = f"Question {count}"

            else: 
                # Appends the latest number for question.
                data["number"] = f"Question {headercount[-1] + 1}"
                headercount.append(headercount[-1] + 1)

            data["category"] = question
            choices = []

            while True:
                choice = input("Enter choice [Leave blank if no additional choice]: ").strip().upper()

                if choice == "" or choice == 'NONE':
                    break

                else:
                    # Adds choices and choice counters to data.
                    if choice not in choices:
                        choices.append(choice)
                        data[f"choice{choicenum}"] = choice
                        data[f"choice{choicenum}-count"] = 0
                        choicenum += 1

                    else:
                        print("Already included")
            
        rows.append(data)
        count += 1

    # answer = input("Is this a new file?[y/n] ").strip().upper()

    # Checks if the file provided is new. If new it would add headers. Otherwise, append only the new questions.
    if fileExisting == False:
        with open(f"./{fileName}", 'w', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=header)
            writer.writeheader()
            writer.writerows(rows)
    
    else:
        with open(f"./{fileName}", 'a', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=header)
            writer.writerows(rows)

# grabInput()