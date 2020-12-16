import csv
import matplotlib.pyplot as plt

trump_pctg = []
deaths_per_cap = []

def getDeathsPerCapita(state, county, deaths):
    with open('acs2015_county_data.csv') as census_data:
        census_reader = csv.reader(census_data)
        for row in census_reader:
            if row[1] == state and row[2] == county:
                return round((float(deaths) / float(row[3])) * 100000.000, 1)

with open('CountyElectionData.csv') as file:
    reader = csv.reader(file)
    for row in reader:
        with open('custom-us-counties-csv.csv') as covidFile:
            covidReader = csv.reader(covidFile)
            for cRow in covidReader:
                if cRow[1] == row[1].strip(' County') and cRow[2] == row[0]:
                    DPC = getDeathsPerCapita(cRow[2], cRow[1], cRow[5])
                    print(
                        row[0] + " - " + row[1] + ":    " + row[4] + " - _dpc: " +
                        str(DPC)
                    )
                    trump_pctg.append(
                        float(row[4].strip('%'))
                    )
                    deaths_per_cap.append(DPC)

print(trump_pctg)
print(deaths_per_cap)

plt.plot(trump_pctg, deaths_per_cap, 'ro')
plt.xlabel('Trump Vote Percentage')
plt.ylabel('Covid Deaths per 100k People')
plt.show()