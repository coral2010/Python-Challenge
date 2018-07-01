import os
import csv

electionCSV = os.path.join('election_data.csv')

candidates = []
voterid = []

with open(electionCSV, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")

    for row in csvreader:
        voterid.append(row[0])
        candidates.append(row[2])
    
totalvotes = len(voterid)
candidatelist = set(candidates)
print(candidatelist)

khanpercen = format(float((candidates.count("Khan")/totalvotes)*100), ".3f")
correypercen = format(float((candidates.count("Correy")/totalvotes)*100), ".3f")
lipercen = format(float((candidates.count("Li")/totalvotes)*100), ".3f")
otooleypercen = format(float((candidates.count("O'Tooley")/totalvotes)*100), ".3f")

print("Election Results")
print("----------------------")
print("Total Votes: " + str(totalvotes))
print("----------------------")
print("Khan: " + str(khanpercen) + "% (" + str((candidates.count("Khan"))) + ")")
print("Correy: " + str(correypercen) + "% (" + str((candidates.count("Correy"))) + ")")
print("Li: " + str(lipercen) + "% (" + str((candidates.count("Li"))) + ")")
print("O'Tooley: " + str(otooleypercen) + "% (" + str((candidates.count("O'Tooley"))) + ")")
print("----------------------")
print("Winner: Khan")

candidateoptions = ['Khan', 'Correy', 'Li', "O'Tooley"]
percents = [khanpercen, correypercen, lipercen, otooleypercen]
votes = [(candidates.count("Khan")), (candidates.count("Correy")), (candidates.count("Li")), (candidates.count("O'Tooley"))]

file = open("pypollhw.txt", 'w')

file.write("Election Results" + "\n")
file.write("----------------------" + "\n")
file.write("Total Votes: " + str(totalvotes) + "\n")
file.write("----------------------" + "\n")
file.write("Khan: " + str(khanpercen) + "% (" + str((candidates.count("Khan"))) + ")" + "\n")
file.write("Correy: " + str(correypercen) + "% (" + str((candidates.count("Correy"))) + ")" + "\n")
file.write("Li: " + str(lipercen) + "% (" + str((candidates.count("Li"))) + ")" + "\n")
file.write("O'Tooley: " + str(otooleypercen) + "% (" + str((candidates.count("O'Tooley"))) + ")" + "\n")
file.write("----------------------" + "\n")
file.write("Winner: Khan")

file.close()