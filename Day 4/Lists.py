statesOfAmerica = ["Delaware", "Pennsylvania", "New Jersey", "Georgia", "Connecticut", "Massachusetts", "Maryland", "South Carolina", "New Hampshire", "Virginia", "New York", "North Carolina", "Rhode Island", "Vermont", "Kentucky", "Tennessee", "Ohio", "Louisiana", "Indiana", "Mississippi", "Illinois", "Alabama", "Maine", "Missouri", "Arkansas", "Michigan", "Florida", "Texas", "Iowa", "Wisconsin", "California", "Minnesota", "Oregon", "Kansas", "West Virginia", "Nevada", "Nebraska", "Colorado", "North Dakota", "South Dakota", "Montana", "Washington", "Idaho", "Wyoming", "Utah", "Oklahoma", "New Mexico", "Arizona", "Alaska", "Hawaii"]

print(statesOfAmerica[0])

print(statesOfAmerica[-1])

statesOfAmerica.extend(["Winserland", "Kathland"])
print(statesOfAmerica[-1])

statesOfAmerica.append("Luiland")
print(statesOfAmerica[-1])

#Nested Lists
cars = ["Volvo", "BMW", "Jaguar"]
trucks = ["Nissan", "Daihatsu", "Toyota"]

vehicles = [cars, trucks]

print(vehicles)
