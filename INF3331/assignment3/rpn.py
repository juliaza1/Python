import math
import sys

#initiate stack as a list
stack = []

#function that checks if user input is numeric
def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        pass

#function that pushes s on top of stack
def push(s):
    stack.append(s)

#function that removes the last item from stack
def pop():
    stack.remove(stack[-1])

def calc(inp):
    i = 0
    for elem in inp: 
        # #pushes inp onto stack 
        if is_number(elem):
            push(elem)
            i+=1

        #prints the latest item if at least one item on stack
        elif (elem == 'p') and (len(stack) >= 1):
            print(stack[-1])  

        #command to exit program
        elif (elem == 'q'):
                print("Quitting...")
                running = False
                sys.exit(1)

        #square root function
        elif ((elem == 'v') and (len(stack) >= 1)):
            try:
                sq = math.sqrt(float(stack[-1]))
                stack.pop()
                push(sq)
            except:
                print("Error while trying to sqrt(). Program exiting...")
                sys.exit(1)

        #sine function
        elif ((elem == 'sin') and (len(stack) >= 1)):
            try:
                sin = math.sin(float(stack[-1]))
                stack.pop()
                push(sin)
            except:
                print("Error while trying to sqrt(). Program exiting...")
                sys.exit(1)

        #cosine function
        elif ((elem == 'cos') and (len(stack) >= 1)):
            try:
                cos = math.cos(float(stack[-1]))
                stack.pop()
                push(cos)
            except:
                print("Error while trying to sqrt(). Program exiting...")
                sys.exit(1)
        
        #checks for arithmetic operations and does the math
        elif (len(stack) >= 2):
            if (elem == '+'):
                sum = float(stack[-1]) + float(stack[-2])
                stack.pop()
                stack.pop()
                push(sum)
            elif (elem == '*'):
                prod = float(stack[-1]) * float(stack[-2])
                stack.pop()
                stack.pop()
                push(prod)
            elif (elem == '/'):
                try:
                    quo = float(stack[-1]) / float(stack[-2])
                    stack.pop()
                    stack.pop()
                    push(quo)
                except:
                    print("Error: Division by Zero. Program exiting...")
                    running = False
                    sys.exit(1)
            
        else:
            print("Wrong input. Exiting...")
            running = False
            sys.exit(1)




def main():
    running = True

    if (len(sys.argv) == 2):
        #getting input from user and stripping leading, trailing whitespaces
        inp = sys.argv[1].rstrip()
        #getting rid of whitespaces inbetween
        inp = inp.split()
        calc(inp)    

    elif ((len(sys.argv) != 2) and (len(sys.argv) != 1)):
            print("Wrong number of command line arguments")
            sys.exit(0)

    else:
        while running:
            if (len(sys.argv) == 1):
                #getting input from user and stripping leading, trailing whitespaces
                inp = input('Enter numbers and operators. To exit, press "q": ').rstrip()
                #getting rid of whitespaces inbetween
                inp = inp.split()
                calc(inp)

if __name__ == '__main__':
    main()