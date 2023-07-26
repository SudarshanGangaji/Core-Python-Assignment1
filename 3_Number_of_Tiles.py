#WAP If area of room is 144 sq m.Then how many tiles of size 12*12 sq cm will be required to cover the flooring of room.
Area_of_room = int(input("Enter Area of room: "))
Area_of_tile = int(input("Enter Area of tile: "))

Total_Number_of_tiles = Area_of_room / Area_of_tile
print("Total tiles required: ", Total_Number_of_tiles)