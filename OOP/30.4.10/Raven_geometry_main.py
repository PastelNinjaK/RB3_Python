from Raven_circle import Circle
from Raven_rect import Rectangle
from Raven_extra_shapes import Cone
from Raven_extra_shapes import Pyramid
from Raven_extra_shapes import Sphere


def main():
    """
    Runs the main program
    
    """

    # from meters conversion factor
    meters_to = {
        "feet":3.28084,
        "inches":39.37008,
        "yards": 1.09361,
        "timbits":23,
        "meters":1,
        "miles": 0.000621371,
        "kilometers": 0.001, 
        "centimeters": 100,
        "cubit": 2.2522522522522523
    }



    circle_arr = [
        Circle("Man Hole",0.5),
        Circle("Tower Of Pisa", 20, 80)]
    rectangle_arr = [
        Rectangle("Paper",0.28,0.216),
        Rectangle("Printer",0.32,0.36,0.24)
    ]

    pyramid_arr = [
        Pyramid("Giza",20,30,50),
        Pyramid("Menkaure",60,30,40)
    ]

    cone_arr = [
        Cone("Ice Cream Cone",0.0508,0.1524),
        Cone("Conical Funnel",1,5)
        ]
    sphere_arr = [
        Sphere("Timbits",0.005),
        Sphere("Earth",6370000)# Yes this is the radius of the earth in meters(Thank you physics 30 formula sheet)
    ]
    #2D array for all of the objects
    all_shapes_arr =[circle_arr,rectangle_arr,pyramid_arr,cone_arr,sphere_arr]
    
    # array for the name of every object in side all_shapes_arr w/ spaces.
    name_arr = []
    for item in all_shapes_arr:
        for shape in item:
            name_arr.append(shape.get_name())
    
    # array for the name of every object in side all_shapes_arr without spaces and capital leters
    # (this is done so that the search can handle inputs with spaces).
    new_name_arr = []  
    for item in name_arr:
        new_name_arr.append(item.replace(" ","").lower())
    
    while True:
        print("\nChoose your shapes.")
        # Prints all the contents of name_arr
        for item in name_arr:
            print(item)
        # Asks the user for the name of the object   
        user = input("\nWhich object do you want?(type stop to stop): ").strip().lower().replace(" ","")
        # if the user types stop, program stops
        if user == "stop":
            break
        # if the user inputs an invalid/object not in all_shapes_arr 
        if user not in new_name_arr:
            print(f"{user} is not part of my database\nPlease try again.\n")
            continue
        # finds the index of the chosen object by the user and prints the equivalent version from 
        #  name_arr.   
        indx = new_name_arr.index(user)
        inpt = name_arr[indx]
        # Asks user for the unit the they want
        print(f"You have chosen {inpt}")
        units_arr = list(meters_to.keys())
        print(f"Units available: {units_arr}")
        units = input("what unit of measurement do you want(type stop to stop): ")
        if units == 'stop':
            break
        # if the measurement is not in the meters_to array
        if units not in meters_to.keys():
            print("We do not have the conversion for that\nPlease try again\n.")
            continue

        for item in all_shapes_arr:
            for shape in item:
                #converts the measuremet from meters to the user's chosen unit
                shape.set_factor(meters_to.get(units))
                shape.set_unit(units)
                if shape.get_name() == inpt:
                    #Prints the respected properties of each object
                    print(f"\n{shape}")
                #Resets the measurement factor    
                shape.set_factor(meters_to.get(units),1)

    
if __name__ == "__main__":
    main()