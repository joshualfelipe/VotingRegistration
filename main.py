from getInput import grabInput
from getVotes import startVoting

data = {}
def queue():
    answer = input("[a] Add Questions\n[b] Vote\n[x] Exit\n\nAnswer: ").strip().upper()
    if answer == 'A' or answer == 'B' or answer == "X":
        return answer
    else:
        print("Input not found!\n")
        return queue()

def getQuestions():
    grabInput()

def getVotes():
    startVoting()                    

# def storeVotes(data):
#     pass

def main():
    selected = queue()

    if selected == 'A':
        getQuestions()
    
    elif selected == 'B':
        getVotes()
        # storeVotes(data)
        # print(data)
    
    elif selected == "X":
        return 0
    
    return 1

            

if __name__ == '__main__':
    while True:
        task = main()
        print()
        if task == 0:
            print("You exited")
            break