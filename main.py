from getInput import grabInput
from getVotes import startVoting

def queue():
    answer = input("[a] Add Questions\n[b] Vote\n[x] Exit\n\nAnswer: ").strip().upper()
    if answer == 'A' or answer == 'B' or answer == "X":
        return answer
    else:
        print("Input not found!\n")
        return queue()

def main(fileName):
    selected = queue()

    if selected == 'A':
        grabInput(fileName)
    
    elif selected == 'B':
        startVoting(fileName)  
    
    elif selected == "X":
        return 0
    
    return 1

            

if __name__ == '__main__':
    ask = input("Enter Filename\n\nAnswer: ").strip()
    while True:
        task = main(ask)
        print()
        if task == 0:
            print("You exited")
            break