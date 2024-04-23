"""
hotel_cost, plane_cost, car_rental, holiday_cost
"""


class Flight:
    """ Represents a flight. 
    Properties:
    -  destination(str): The destination of this flight. 
    -  cost(float): The cost of this flight. 
    -  rental_cost(float): The cost of rent at this destination. 
    """
    def __init__(self, destination, cost, rental_cost):
        """ Creates a new Flight object. """
        self.destination = destination
        self.cost = cost
        self.rental_cost = rental_cost

    def get_rent(self):
        print(
            f"It costs ${self.rental_cost} to rent a car at {self.destination}"
        )

    def __str__(self):
        return f"{self.destination} - ${self.cost}"


FLIGHTS = [
    Flight("Work", 1200, 20),
    Flight("Home", 200, 200),
]
""" Contains Flight information. """

def get_flight(destination):
    """_summary_

    :param destination: The destination.
    :type destination: str
    """
    ...



for f, flight in enumerate(FLIGHTS):
    print(f"{f}: {flight}")

user_selection = int(input("Choose a place"))
user_flight = FLIGHTS[user_selection]

# Selects a destination
user_flight.get_rent()
