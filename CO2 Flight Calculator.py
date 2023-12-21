#CO2 Flight Calculator - Irhan Iftikar, July 2021

#Sources:
#Flight data via https://openflights.org/data.html
#Haversine Formula via https://www.kite.com/python/answers/how-to-find-the-distance-between-two-lat-long-coordinates-in-python
#Emissions calculator assistance via https://assets.publishing.service.gov.uk/government/uploads/system/uploads/attachment_data/file/726911/2018_methodology_paper_FINAL_v01-00.pdf
#And also https://www.ana.co.jp/en/us/travel-information/seat-map/b777-300er/#:~:text=There%20are%208%20First%20Class,numbered%20from%201%20to%2042.

#There will always be a variation between the accuracy of emissions for any flight
#Due to Climate conditions, distance, plane type, freight load, seating configuration, etc.

#Notes:
#Assuming there is no possible freight/cargo on plane
#Total number of seats on plane is 264, estimated load factor is 90% - means that roughly 238 seats are occupied, and that is the basis to be calculated on
#Emissions calculated per passenger basis, does not account for empty seats
#Proportion of occupied seats - Economy: 162, Economy+: 22, Business: 47, First: 7
# 162 economy = 162 economy, 22 eco+ = 35.2 economy, 47 business = 136.3 economy, 7 first = 28 economy
#Proportionally, means that total makes up 361.5 economy seats


import csv
from math import radians, cos, sin, asin, sqrt


#Function for the data of source airport, read from a txt list containing 10,000 airports
#Data includes airport name, code, longitude & latitude (used to find distance between airports),etc
def airport_one():
    while True:
        list_1=[]
        search = input("3-Digit Departure Airport Code (All Caps): ")
        f=open('C:\\Users\\iiftikar26\\airports.txt',encoding="utf-8")
        for a, b, c, d, e, f, g, h, i, j, k, l, m, n in csv.reader(f):
            if e == search:
                print("Airport:", b,",",c,",",d,".")
                list_1.append(float(g))
                list_1.append(float(h))
                list_1.append(e)
                list_1.append(c)
                break
                break
            else:
                e = 10
            
        s = type(e) == str
        if s == False:
            print("Invalid 3-Digit Airport Code. Try Again: ")
            continue
        else:
            pass
        return list_1


#Data of second airport
def airport_two():
    while True:
        list_2=[]
        search = input("3-Digit Destination Airport Code (All Caps): ")
        f=open('C:\\Users\\iiftikar26\\airports.txt',encoding="utf-8")
        for a, b, c, d, e, f, g, h, i, j, k, l, m, n in csv.reader(f):
            if e == search:
                print("Airport:", b,",",c,",",d,".")
                list_2.append(float(g))
                list_2.append(float(h))
                list_2.append(e)
                list_2.append(c)
                break
                break
            else:
                e = 10

        s = type(e) == str
        if s == False:
            print("Invalid 3-Digit Airport Code. Try Again: ")
            continue
        else:
            pass
        return list_2


#Function to determine the class that the passenger is flying, also finds out how many passengers to account emissions for
#Important to know - For example, one first class seat emits 4x the amount of CO2 emissions as one economy seat
def seat_class():
    class_list = []
    while True:
        question = input("Select class: 'Economy', 'Premium Economy', 'Business', or 'First'? ")
        if question == "Economy":
            proportion = 1.00
            while True:
                question_2 = input("Amount of passengers to account emissions for? ")
                x = (str.isdigit(question_2))
                if str.isdigit(question_2) == (False):
                    print("Please enter a valid number.")
                elif str.isdigit(question_2) == (True):
                    question_2 = int(question_2)
                    if question_2 > 162:
                        print("Maximum number of economy passengers is 162.")
                    elif question_2 < 1:
                        print("Must be at least one passenger.")
                    else:
                        class_list.append(proportion)
                        class_list.append(question_2)
                        class_list.append(question)
                        return class_list
                        break
                        break
        elif question == "Premium Economy":
            proportion = 1.60
            while True:
                question_2 = input("Amount of passengers to account emissions for? ")
                x = (str.isdigit(question_2))
                if str.isdigit(question_2) == (False):
                    print("Please enter a valid number.")
                elif str.isdigit(question_2) == (True):
                    question_2 = int(question_2)
                    if question_2 > 22:
                        print("Maximum number of premium economy passengers is 22.")
                    elif question_2 < 1:
                        print("Must be at least one passenger.")
                    else:
                        class_list.append(proportion)
                        class_list.append(question_2)
                        class_list.append(question)
                        return class_list
                        break
                        break
        elif question == "Business":
            proportion = 2.90
            while True:
                question_2 = input("Amount of passengers to account emissions for? ")
                x = (str.isdigit(question_2))
                if str.isdigit(question_2) == (False):
                    print("Please enter a valid number.")
                elif str.isdigit(question_2) == (True):
                    question_2 = int(question_2)
                    if question_2 > 47:
                        print("Maximum number of business class passengers is 47.")
                    elif question_2 < 1:
                        print("Must be at least one passenger.")
                    else:
                        class_list.append(proportion)
                        class_list.append(question_2)
                        class_list.append(question)
                        return class_list
                        break
                        break
        elif question == "First":
            proportion = 4.00
            while True:
                question_2 = input("Amount of passengers to account emissions for? ")
                x = (str.isdigit(question_2))
                if str.isdigit(question_2) == (False):
                    print("Please enter a valid number.")
                elif str.isdigit(question_2) == (True):
                    question_2 = int(question_2)
                    if question_2 > 7:
                        print("Maximum number of first class passengers is 7.")
                    elif question_2 < 1:
                        print("Must be at least one passenger.")
                    else:
                        class_list.append(proportion)
                        class_list.append(question_2)
                        class_list.append(question)
                        return class_list
                        break
                        break
        else:
            print("Answer not understood.")


#Asks user if they are going on a one-way flight or return flight
def return_trip():
    while True:
        question = input("Select option for trip: 'Return' or 'One-Way'? ")
        if question == "Return":
            trip = 2
            break
        elif question == "One-Way":
            trip = 1
            break
        else:
            print("Answer not understood.")
    return trip


#Calculates the distance between the two airports using Haversine Formula, source linked at top of code shell
#Haversine Formula calculates the distance between any two points on a sphere, in this case the Earth by using longitude/latitude data
#Important to caluclate distance as this is needed to calculate CO2 Emissions
def calculate(list_a, list_b):
    lat1 = list_a[0]
    lon1 = list_a[1]
    lat2 = list_b[0]
    lon2 = list_b[1]

    lat1 = radians(lat1)
    lon1 = radians(lon1)
    lat2 = radians(lat2)
    lon2 = radians(lon2)

    dist_lon = lon2 - lon1 
    dist_lat = lat2 - lat1 
    a = sin(dist_lat/2)**2 + cos(lat1) * cos(lat2) * sin(dist_lon/2)**2
    c = 2 * asin(sqrt(a)) 
    r = 3956 
    distance = c*r

    code1 = list_a[2]
    city1 = list_a[3]
    code2 = list_b[2]
    city2 = list_b[3]

    print("Distance from {}-{} to destination {}-{} is {} miles".format(code1,city1,code2,city2,round(distance,2)))
    return distance


#Assuming that the plane used for long haul international is Boeing 747-400
#Total amount of fuel is: 15.10732 kgs of fuel per mile
#Via https://www.carbonindependent.org/files/B851vs2.4.pdf (page 53)
#CO2 emissions are based on the following factor: 3.15 kg CO2 /kg fuel.
#Via https://www.carbonindependent.org/files/B851vs2.4.pdf (page 22) factor
def emissions_longDistance(dist, proportions, return_trip):
    fuel_burned = dist * 15.10732
#In kilograms
    carbon_emission_kg = fuel_burned * 3.157
    radiative_forcing = 1.90
#Radiative forcing is the factor for being in the air (emits more than ground level) + delays, circling, indirect routes, closed airspace, etc.
    total_carbon_emission = carbon_emission_kg * radiative_forcing * return_trip
    total_emission = total_carbon_emission * 0.001
#Converts to metric tons
    proportion_economy = 361.5
    proportion_class = proportions[0]
    passenger_account = proportions[1]
    section_class = proportions[2]
    proportion_emission = total_emission / proportion_economy
    final_proportion_emission = (proportion_emission * proportion_class) * passenger_account
    print("\nTotal CO2 emissions produced by plane: {} metric tons".format(round(total_emission,2)))
    print("CO2 emissions produced by {} passenger(s) in {} class: {} metric tons".format(passenger_account, section_class, round(final_proportion_emission,1)))
    passenger_vehicle = total_emission / 4.6
    smartphone_charge = round(final_proportion_emission / 0.00000822)
    smartphone_charge_format = "{:,}".format(smartphone_charge)
#Passenger vehicle and smartphone data via https://www.epa.gov/energy/greenhouse-gas-equivalencies-calculator
    print("\nProportionally, {} metric tons of CO2 emissions is equal to the greenhouse gas emissions of {} passenger vehicles driven for one year.".format(round(total_emission, 2), round(passenger_vehicle)))
    print("In addition, {} metric tons of CO2 emissions is equal to that of {} smartphones being fully charged.".format(round(final_proportion_emission, 1), smartphone_charge_format))
    print("\nFor more data regarding your CO2 emissions, visit https://www.epa.gov/energy/greenhouse-gas-equivalencies-calculator.")
    

#Plane used for short haul flight - Boeing 737-400
#Total amount of fuel is: 4.8065 kgs of fuel per mile
#Via https://www.carbonindependent.org/files/B851vs2.4.pdf (page 50)
#Code is 99% the same as long distance flight, only difference is kgs fuel used per mile
def emissions_shortDistance(dist, proportions, return_trip):
    fuel_burned = dist * 4.8065
    carbon_emission_kg = fuel_burned * 3.157
    radiative_forcing = 1.90
    total_carbon_emission = carbon_emission_kg * radiative_forcing * return_trip
    total_emission = total_carbon_emission * 0.001
    proportion_economy = 361.5
    proportion_class = proportions[0]
    passenger_account = proportions[1]
    section_class = proportions[2]
    proportion_emission = total_emission / proportion_economy
    final_proportion_emission = (proportion_emission * proportion_class) * passenger_account
    print("\nTotal CO2 emissions produced by plane: {} metric tons".format(round(total_emission,2)))
    print("CO2 emissions produced by {} passenger(s) in {} class: {} metric tons".format(passenger_account, section_class, round(final_proportion_emission,1)))
    passenger_vehicle = total_emission / 4.6
    smartphone_charge = round(final_proportion_emission / 0.00000822)
    smartphone_charge_format = "{:,}".format(smartphone_charge)
    print("\nProportionally, {} metric tons of CO2 emissions is equal to the greenhouse gas emissions of {} passenger vehicles driven for one year.".format(round(total_emission, 2), round(passenger_vehicle)))
    print("In addition, {} metric tons of CO2 emissions is equal to that of {} smartphones being fully charged.".format(round(final_proportion_emission, 1), smartphone_charge_format))
    print("\nFor more data regarding your CO2 emissions, visit https://www.epa.gov/energy/greenhouse-gas-equivalencies-calculator.")
    

#Runs the code
x = airport_one()
y = airport_two()
list_s = seat_class()
t = return_trip()
z = calculate(x,y)

#Classifies a flight into "long distance" or "short distance"
#If flight distance is greater than 2000 miles, it is long distance
#If flight distance is less than 2000 miles, it is short distance
if z > 2000:
    emissions_longDistance(z, list_s, t)
elif z < 2000:
    emissions_shortDistance(z, list_s, t)
else:
    emissions_shortDistance(z, list_s, t)

def aquit():
    while True:
        decision = input("Print 'quit' to the console to quit. ")
        if decision == "quit":
            break
        else:
            continue
aquit()
