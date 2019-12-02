#Day 1: The Tyranny of the Rocket Equation
#Advent of Code 2019
#R. Sears


file = open("moduleMassList.txt")

massList = list()

for f in file:
    fi = f.strip('\n')
    massList.append(float(fi))

file.close()

print(massList)

fuelNeeded = list()

for m in massList:
    fuelValue = (m // 3) - 2
    fuelNeeded.append(fuelValue)
print(fuelNeeded)

fuelSum = 0
for s in fuelNeeded:
    fuelSum += s

print(fuelSum)

def fuel_counter_upper(fsn,fsl):
   for fs in fsn:
       fValue = (fs // 3) - 2
       fsl.append(fValue)
       while fValue > 0:
           fValue = (fValue // 3) - 2
           if fValue > 0:
            fsl.append(fValue)

fuelNeeded2 = list()

fuel_counter_upper(fuelNeeded,fuelNeeded2)

print(fuelNeeded2)

fuelSum2 = fuelSum
for y in fuelNeeded2:
    fuelSum2 += y

print(fuelSum2)

