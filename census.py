import csv
import sys
import matplotlib.pyplot as plt

cFile = 'acs2015_county_data.csv'
restricted = ['CensusId', 'State', 'County']

xArr = []
yArr = []

print("Input X and Y axes from rows:")

print("TotalPop,Men,Women,Hispanic,White,Black,Native,Asian,\n"
      "Pacific,Citizen,Income,IncomeErr,IncomePerCap,IncomePerCapErr,Poverty,\n"
      "ChildPoverty,Professional,Service,Office,Construction,Production,Drive,\n"
      "Carpool,Transit,Walk,OtherTransp,WorkAtHome,MeanCommute,Employed,PrivateWork,\n"
      "PublicWork,SelfEmployed,FamilyWork,Unemployment")
print("==================================================================")

with open(cFile) as file:
    reader = csv.reader(file)
    head = reader.__next__()

def strCastable(xstr):
    try:
        int(xstr)
        return True
    except:
        try:
            float(xstr)
            return True
        except:
            try:
                complex(xstr)
                return False
            except:
                return False

def valueErr(xAxis, yAxis):
    print("ERROR: invalid axe(s) '" + xAxis + "', '" + yAxis + "'")
    sys.exit()

def parseVal(axis_value):
    if '/' in axis_value:
        val1 = axis_value[0: axis_value.index('/')]
        val2 = axis_value[axis_value.index('/') + 1:]

        if not(val1 in head and val2 in head) or val1 in restricted or val2 in restricted:
            valueErr(val1, val2)
        return [val1, val2]
    else:
        if not(axis_value in head) or axis_value in restricted:
            valueErr(axis_value, '')
        return [axis_value, -1]

def floatable(string):
    if strCastable(string):
        return float(string)
    else:
        return -1

xAxis = parseVal(input("X axis: "))
yAxis = parseVal(input("y axis: "))

xidx_1 = head.index(xAxis[0])
xidx_2 = False
yidx_1 = head.index(yAxis[0])
yidx_2 = False

if xAxis[1] != -1:
    xidx_2 = head.index(xAxis[1])
if yAxis[1] != -1:
    yidx_2 = head.index(yAxis[1])

with open(cFile) as file:
    reader = csv.reader(file)
    reader.__next__()
    for row in reader:
        if xidx_2 != False:
            xArr.append(floatable(row[xidx_1]) / floatable(row[xidx_2]))
        else:
            xArr.append(floatable(row[xidx_1]))

        if yidx_2 != False:
            yArr.append(floatable(row[yidx_1]) / floatable(row[yidx_2]))
        else:
            yArr.append(floatable(row[yidx_1]))

print(xArr)
print(yArr)

plt.plot(xArr, yArr, 'ro')
plt.xlabel(xAxis)
plt.ylabel(yAxis)
plt.show()
