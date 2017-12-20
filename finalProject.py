#Charlie Goodrich
#12/19/2017
#finalProject.py - Math Modeling Final Project calculation program

#constants from linear regression using http://www.xuru.org/rt/MLR.asp
DIST = -9.103117872
POP = 9.971684942*(10**-4)
THREAT = 1313.669746
GDPPC = 3.554445997/10
CONST = 36566.5461

def troopCalculator():
    country = input("Enter the name of your country: ")
    distance = int(input("Enter the distance from the capital to Washington, DC: "))
    population = int(input("Enter the population of the country: "))
    threat = float(input("Enter the threat of the country (0-100 scale): "))
    gdp = float(input("Enter the GDP per capita of the country: "))
    troops = DIST*distance+POP*population+THREAT*threat+GDPPC*gdp+CONST
    print("There should be", troops, "troops in", country)

troopCalculator()
    
