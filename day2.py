# Day 2: 1202 Program Alarm
# Advent of Code 2019
# R. Sears

# Part 1

file = open('intcodeText.txt')
intcodeStr = file.read()
intcodeStrList = intcodeStr.split(',')
intcode = list()

for i in intcodeStrList:
    intcode.append(int(i))
file.close()

opcodesIndexer = list()
for xi in range(len(intcode)):
    if xi % 4 == 0:
        opcodesIndexer.append(xi)

def Intcode_Program(xOpc,xIntc):
    opcode1 = lambda y1,y2 : y1 + y2
    opcode2 = lambda y1,y2 : y1 * y2
    for opcodeIndex in xOpc:
        i1,i2,i3 = (opcodeIndex+1,opcodeIndex+2,opcodeIndex+3)
        x0,x1,x2,x3 = (xIntc[opcodeIndex],xIntc[i1],xIntc[i2],xIntc[i3])
        f1,f2 = xIntc[x1],xIntc[x2]
        if x0 == 1:
            xIntc[x3] = opcode1(f1,f2)
        elif x0 == 2:
            xIntc[x3] = opcode2(f1,f2)
        elif x0 == 99:
            break


intcodeCopy = intcode.copy()

intcodeCopy[1] = 12
intcodeCopy[2] = 2

Intcode_Program(opcodesIndexer,intcodeCopy)
print('Answer to Part 1: ',intcodeCopy[0])
