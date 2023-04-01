import random
import sys
import os 


COIN = ['heads', 'tails']
DICE = [1, 2, 3, 4, 5, 6]
D20 = range(0, 20)

def clear():
    os.system('cls')

def getInput():
    clear()
    print("What would you like to do? Seperate multiple choices with a comma")
    print('C. Coin')
    print('D. Dice')
    print('D20. D20 dice')
    print('Q. Quit')

    while True: # Checks for only one input
        choice = input(">").lower().split(',')
        output = []
        if len(choice == 1 and choice[0] != 'q'):
            print("Error: Invalid input")
        else:
            break

    for c in choice:
        if c == 'c':
            output.append({'type': 'coin', 'amount': c})
        elif c == 'd':
            output.append({'type': 'dice', 'amount': c})
        elif c == 'd20':
            output.append({'type': 'd20', 'amount': c})
        elif c == 'q':
            sys.exit()
    return output

def interpret(output):
    runData = []
    for o in output:
        if o['type'] == 'coin':
            runData.append(COIN)
        elif o['type'] == 'dice':
            runData.append(DICE)
        elif o['type'] == 'd20':
            runData.append(D20)
    return runData

def getPossibleOutcomes(runData):
    code = writePossibilityCode(runData)
    with open('./run.py', 'w') as f: f.write(code)
    run = __import__('run')
    outcomes = run.run()
    os.remove('./run.py')
    return outcomes

def addToCode(code, lineToAdd, currentIndent=""):
    code += currentIndent + lineToAdd + "\n"
    return code

def genAppendToListForCode(varsInUse):
    output = "["
    for i in varsInUse:
        output += i + ","
    return output[:-1] +"]"

def writePossibilityCode(runData):
    with open('./run.py', 'w') as f: f.write("")
    code = "def run():\n    outcomes=[]\n"
    variables = ('a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z', 'aa','ab','ac','ad','ae','af','ag','ah','ai','aj','ak','al','am','an','ao','ap','aq','ar','as','at','au','av','aw','ax','ay','az')
    varIndex = 0
    varsInUse = []
    indent = "    "
    for j in runData:
        code = addToCode(code, "for "+variables[varIndex]+" in "+str(j)+":", indent)
        varsInUse.append(variables[varIndex])
        varIndex += 1
        indent += "    "
    
    l = genAppendToListForCode(varsInUse)

    code = addToCode(code, "outcomes.append("+l+")", indent)
    code = addToCode(code, "return outcomes", "    ")
    return code






print(getPossibleOutcomes([['heads','tails'],[1,2,3,4,5,6]]))
            






