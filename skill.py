import numpy as np
import urllib as ull
import matplotlib.pyplot as plt


gdp_file = ull.request.urlopen("https://raw.githubusercontent.com/datasets/gdp/0be54c18d900edc37123f25b4eff014731c9e459/data/gdp.csv")
line = gdp_file.readline()

usa_year = []
usa_gdp = []

euu_year = []
euu_gdp = []

zg_year = []
zg_gdp = []

search_index = ["USA","CHN","EUU"]

for line in gdp_file:
    decode = line.decode("utf-8")
    split = decode.split(",")
    #Formated as: Country Name[0], Country Code[1], Year[2], Value[3]
    if (split[1] in search_index):
      if(split[1] == "USA"):
        usa_year.append(int(split[2]))
        usa_gdp.append(int(float(split[3]) / 10**9))
      elif(split[1] == "EUU"):       
        euu_year.append(int(split[2]))
        euu_gdp.append(int(float(split[3]) / 10**9))
      elif(split[1] == "CHN"):      
        zg_year.append(int(split[2]))
        zg_gdp.append(int(float(split[3]) / 10**9))

plt.title("Brian Nguyen's GPD Plot")

plt.xlabel('Year')
plt.ylabel('GDP')
plt.ylim(0, 20000)
plt.xlim(1960, 2020)

Jerry, = plt.plot(usa_year, usa_gdp, label='Using set_dashes()')
Tim, = plt.plot(euu_year, euu_gdp, label= 'loosely dotted' )
Bill, = plt.plot(zg_year, zg_gdp, label='dashdotdotted')

#line1, = ax.plot(x, y, label='Using set_dashes()')
Jerry.set_dashes([2, 2, 10, 2])
Tim.set_dashes([2, 4, 2, 2])
Bill.set_dashes([2, 4, 20, 2])
plt.legend([Jerry, Tim, Bill],["USA", "European Union",'China'])

plt.savefig("NguyenBrian_Skill6.png")
plt.show()
