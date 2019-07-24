import os
import csv


def analysisData(data):
    # creating dictionary
    dataDic = {
        "totalVotes": 0,
        "winner": {
            "name": "",
            "percent": 0
        }
    }
    candidate = {
        "name": "",
        "percentVotes": 0,
        "totalVotes": 0
    }
    # retrieve just distinct values of candidate
    nameCandidate = set()
    for value in data:
        nameCandidate.add(value[2])
        dataDic["totalVotes"] += 1
    # reset the csvfile to be counted again
    csvfile.seek(0)
    next(data)

    for name in nameCandidate:
        for row in data:
            if row[2] == name:
                candidate["name"] = row[2]
                candidate["totalVotes"] += 1
        candidate["percentVotes"] = candidate["totalVotes"] / \
            dataDic["totalVotes"]
        if candidate["percentVotes"] > dataDic["winner"]["percent"]:
            dataDic["winner"]["percent"] = candidate["percentVotes"]
            dataDic["winner"]["name"] = name
        # include the results in a list
        listCandiateResult(candidate)
     # reset the csvfile and the totalvotes to be counted again
        csvfile.seek(0)
        next(data)
        candidate["totalVotes"] = 0
    showResult(dataDic)
    winnerResult(dataDic)


def listCandiateResult(candidate):
    textFormat.append(candidate["name"] + ": " + format(
        candidate["percentVotes"], ".2%") + " (" + str(candidate["totalVotes"])+")")


def showResult(dataDic):
    text = (
        f'\tElection Results \n\
        -------------------------\n\
        Total Votes: {dataDic["totalVotes"]}\n\
        -------------------------\
        ')

    for result in textFormat:
        text = text + (f"\n\t{result}")

    print(text)
    txtfile.write(text)


def winnerResult(dataDic):
    text = (f'\n\t-------------------------\n\
        Winner: {dataDic["winner"]["name"]}\n\
        -------------------------')
    print(text)
    txtfile.write(text)
    txtfile.close()


# list to be used into a function
textFormat = []
# read csv file
filepath = os.path.join(".", "Resource", "election_data.csv")
# write txt
outputpath = os.path.join(".", "Resource", "result.txt")
txtfile = open(outputpath, 'w')

with open(filepath, newline='') as csvfile:
    csvread = csv.reader(csvfile, delimiter=',')
    next(csvread)
    # start the process
    analysisData(csvread)
