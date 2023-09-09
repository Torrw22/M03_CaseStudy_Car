#Torrey Walls
#M03_CaseStudy_Car
#Program is used to take user input of a vehicles info and then display it back in an easy to read format
#Variables: vehicle_type, year, make, model, number of doors, type of roof. All these variables are used to describe the car. 


# Define the Vehicle superclass
class Vehicle:
    def __init__(self, vehicle_type):
        self.vehicle_type = vehicle_type

# Define the Automobile subclass that inherits from Vehicle
class Automobile(Vehicle):
    def __init__(self, vehicle_type, year, make, model, doors, roof):
        super().__init__(vehicle_type)
        self.year = year
        self.make = make
        self.model = model
        self.doors = doors
        self.roof = roof

    def display_info(self):
        print("Vehicle type:", self.vehicle_type)
        print("Year:", self.year)
        print("Make:", self.make)
        print("Model:", self.model)
        print("Number of doors:", self.doors)
        print("Type of roof:", self.roof)

# Function to get user input and create an Automobile object
def get_car_info():
    vehicle_type = "car"  # Vehicle type is set to "car"
    year = input("Enter the year: ")
    make = input("Enter the make: ")
    model = input("Enter the model: ")
    doors = input("Enter the number of doors (2 or 4): ")
    roof = input("Enter the type of roof (solid or sun roof): ")

    # Create an Automobile object with user input
    car = Automobile(vehicle_type, year, make, model, doors, roof)
    return car

# Main program
if __name__ == "__main__":
    print("Welcome to the Car Information App")
    car = get_car_info()

    # Display the car information
    print("\nCar Information:")
    car.display_info()
