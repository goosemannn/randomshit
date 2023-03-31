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
    print("What would you like to do? Seperate multiple choices with a comma, and how many times with a :")
    print('C. Coin')
    print('D. Dice')
    print('D20. D20 dice')
    print('Q. Quit')

    choice = input(">").lower().split(',')
    output = []
    for c in choice:
        if c.startswith('c'):
            c.split(':')
            output.append({'type': 'coin', 'amount': c[1]})
        elif c == 'd':
            output.append({'type': 'dice', 'amount': c[1]})
        elif c == 'd20':
            output.append({'type': 'd20', 'amount': c[1]})
        elif c == 'q':
            sys.exit()
    return output

def interpret(output):
    runData = {"data":[], 'amount':[], 'types':[]}
    for o in output:
        if o['type'] == 'coin':
            runData['data'] += COIN
            runData['amount'] += o['amount']
        elif o['type'] == 'dice':
            runData['data'] += DICE
            runData['amount'] += o['amount']
        elif o['type'] == 'd20':
            runData['data'] += D20 
            runData['amount'] += o['amount']
    return runData

def getPossibleOutcomes(runData):
    possibleOutcomes = []
    for i in runData['data']: # Get the list 
        for j in runData['data'][i]: # Get each item in the list 
            o = []
            for k in [x for x in runData['data'] if x != i]: # Get the other lists excluding the current one
                for l in runData['data'][k]: # Get each item in the other list
                    o.append(l)
                
                
                possibleOutcomes.append([j, l])

print(getPossibleOutcomes({'data': [['heads','tails'],[1,2,3,4,5,6]], 'amount': [1, 1]}))
            






