import os
import csv

# function to read external csv file


def readFile(filename):
    csvpath = os.path.join(".", "Resource", filename)
    with open(csvpath, newline="") as csvfile:
        csvread = csv.reader(csvfile, delimiter=",")
        analyseData(csvread)

# fucntion to analyse the content of csv file


def analyseData(data):
    dictData = {
        "totalmonth": 0,
        "totalamount": 0,
        "average": 0,
        "profitsIncrease": {
            "month": "",
            "increaseprofits": 0
        },
        "profitsDecrease": {
            "month": "",
            "decreaseprofits": 0
        }

    }
    # jump the first row
    next(data)
    for row in data:
        dictData["totalmonth"] += 1
        dictData["totalamount"] += float(row[1])
        if float(row[1]) > dictData["profitsIncrease"]["increaseprofits"]:
            dictData["profitsIncrease"]["month"] = row[0]
            dictData["profitsIncrease"]["increaseprofits"] = float(row[1])
        elif float(row[1]) < dictData["profitsDecrease"]["decreaseprofits"]:
            dictData["profitsDecrease"]["month"] = row[0]
            dictData["profitsDecrease"]["decreaseprofits"] = float(row[1])

    dictData["average"] = round(
        dictData["totalamount"]/dictData["totalmonth"], 2)
    showResult(dictData)

# format and print the result


def showResult(dictionary):
    text = (f'\n\
    Financial Analysis\n\
    ----------------------------\n\
    Total Months: {dictionary["totalmonth"] }\n\
    Total: {dictionary["totalamount"] }\n\
    Average  Change: {dictionary["average"] }\n\
    Greatest Increase in Profits: {dictionary["profitsIncrease"]["month"]} ({dictionary["profitsIncrease"]["increaseprofits"]})\n\
    Greatest Decrease in Profits: {dictionary["profitsDecrease"]["month"]} ({dictionary["profitsDecrease"]["decreaseprofits"]})\n\
    ')
    print(text)
    writeFile(text)


def writeFile(text):
    outputpath = os.path.join(".", "Resource", "result.txt")
    txtfile = open(outputpath, 'w')

    txtfile.write(text)
    txtfile.close()

    # start the function call
readFile("budget_data.csv")
