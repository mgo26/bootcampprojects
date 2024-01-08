#Initial user inputs
while True:
    city_flight = input("Please choose a destination, your choices are: Paris, Milan, New York or Auckland: ")
    if city_flight.lower() == "paris":
        city_flight = city_flight.lower()
        break
    elif city_flight.lower() == "milan":
        city_flight = city_flight.lower()
        break
    elif city_flight.lower() == "new york":
        city_flight = city_flight.lower()
        break
    elif city_flight.lower() == "auckland":
        city_flight = city_flight.lower()
        break
    else:
        input("Please re-enter your choice, making sure you choose from the following options: Paris, Milan, New York or Auckland: ")

while True:
    num_nights = input("Please enter the number of nights you will be staying: ")
    if num_nights.isdigit():
        num_nights = int(num_nights)
        break
    else:
        print("Please ensure you type in a whole number")

while True:
    rental_days = input("Please enter the number of days you will be hiring a car for: ")
    if rental_days.isdigit():
        rental_days = int(rental_days)
        break
    else:
        print("You must rent the car for a number of full days.")

#Functions
def hotel_cost(x, y = 40):
    total = x * y
    return total


def plane_cost(x):
    if x == 'paris':
        return 150
    elif x == 'milan':
        return 200
    elif x == 'new york':
        return 500
    elif x == 'auckland':
        return 800
    

def car_rental(x, y = 40):
    total = x * y
    return total


def holiday_cost(a, b, c):
    x = a + b + c
    return x

#values are passed to the functions here
hotels = hotel_cost(num_nights)
flights = plane_cost(city_flight)
car = car_rental(rental_days)
total = holiday_cost(hotels, flights, car)

# Messages displayed to user
print(f"Your total cost for this holiday is £{total}.\n")
print("This is broken down as follows:\n")
print(f"The cost of the flights is £{flights}.\n")
print(f"The cost of the hotel for {num_nights} days is £{hotels}.\n")
print(f"The cost of the car hire for {rental_days} days is £{car}.")