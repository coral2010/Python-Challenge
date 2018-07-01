import os
import csv

pybankpath = os.path.join('budget_data.csv')

datelist = []
revenuelist = []

with open(pybankpath, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    csv_header = next(csvreader)
#    print(f"CSV Header: {csv_header}")

    for row in csvreader:
        datelist.append(row[0])
        revenuelist.append(int(row[1]))

totalmonths = len(datelist)
totalrevenue = sum(revenuelist)
changeinpricelist = [x - revenuelist[i - 1] for i, x in enumerate(revenuelist) if i > 0]
averagechangeinprice = sum(changeinpricelist)/len(changeinpricelist)
maxchangeinprice = max(changeinpricelist)
minchangeinprice = min(changeinpricelist)
maxprofitdate = datelist[(changeinpricelist.index(int(maxchangeinprice)))+1]
minprofitdate = datelist[(changeinpricelist.index(int(minchangeinprice)))+1]

print("Financial Analysis")
print("------------------------")
print("Total Months: " + str(totalmonths))
print("Total: $" + str(totalrevenue))
print("Average Change: $" + format(averagechangeinprice, ".2f"))
print("Greatest Increase in Profits: " + maxprofitdate + " ($" + str(maxchangeinprice)+ ")")
print("Greatest Decrease in Profits: " + minprofitdate + " ($" + str(minchangeinprice)+ ")")

file = open("pybankhw.txt", 'w')

file.write("Financial Analysis" + "\n")
file.write("------------------------" + "\n")
file.write("Total Months: " + str(totalmonths) + "\n")
file.write("Total: $" + str(totalrevenue) + "\n")
file.write("Average Change: $" + format(averagechangeinprice, ".2f") + "\n")
file.write("Greatest Increase in Profits: " + maxprofitdate + " ($" + str(maxchangeinprice)+ ")" + "\n")
file.write("Greatest Decrease in Profits: " + minprofitdate + " ($" + str(minchangeinprice)+ ")")