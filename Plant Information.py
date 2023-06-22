# We define a class named Plant
class Plant:
    # __init__ is used to initialize all the specifications of the plant.
    def __init__(self, plant_name, plant_cost):
        self.plant_name = plant_name
        self.plant_cost = plant_cost
        
    # print_info() prints the details of the object in the required format.
    def print_info(self):
        print('   Plant name:',self.plant_name)
        print('   Cost:',self.plant_cost)


# We define a class named Flower that extends Plant class.
class Flower(Plant):
    # __init__ is used to initialize all the specifications of the flower.
    def __init__(self, plant_name, plant_cost, is_annual, color_of_flowers):
        Plant.__init__(self, plant_name, plant_cost)
        self.is_annual = is_annual
        self.color_of_flowers = color_of_flowers
        
    # print_info() prints the details of the object in the required format.
    def print_info(self):
        print('   Plant name:',self.plant_name)
        print('   Cost:',self.plant_cost)
        print('   Annual:',self.is_annual)
        print('   Color of flowers:',self.color_of_flowers)
 
# print_list() method iterates through the my_garden list and prints each object. 
def print_list():
    # We traverse through the my_garden list
    for i, plant in enumerate(my_garden, 1):
        # We call the print_info() method for each object to print their details.
        print(f'Plant {i} Information:')
        plant.print_info()
        # We print a new line after printing each object
        print()

        
# Our program starts here.
if __name__ == "__main__":
    # We declare an empty list named my_garden that can hold the objects of plant and flower type.
    my_garden = []
    # We prompt the user to enter a string.
    # input() is used to get user input
    user_string = input()
    
    # We keep getting user input until they enter -1
    while user_string != '-1':
        # We first split the string whenever space occurs to get the specifications separately.
        # split() returns a list after splitting the elements whenever space occurs.
        # For eg: "plant Spirnea 10" when split returns ["plant", "Spirnea", "10"]
        splitString = user_string.split()
        
        # If plant is present in the string entered by the user then we need to create a Plant object.
        if("plant" in user_string):
            # list index starts from 0 so the plant name occurs second in the list that is, in index 1.
            # Similarly cost is at index 2.
            # So we create a object by passing these 2 elements.
            p = Plant(splitString[1],splitString[2])
            # Then we add the object to the my_garden list using the append()
            my_garden.append(p)
        # else if the "plant" string is not present in the string entered by the user then it is a flower object.
        else:
            # # list index starts from 0 so the plant name occurs second in the list that is, in index 1.
            # Similarly cost is at index 2.
            # the element at index 3 indicates whether the plant is annual or not.
            # atlast the element at index 4 denotes color of the flower.
            f = Flower(splitString[1],splitString[2],splitString[3],splitString[4])
            # Then we add the object to the my_garden list using the append()
            my_garden.append(f)
            
        # Again we prompt the user to enter the next string and the loop continues.
        user_string = input()
    # Finally we call the print_list() method to print the details of each object
    print_list()
