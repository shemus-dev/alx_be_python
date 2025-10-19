houses = [1200,1201,1202,1600]

for house in houses:
    if house % 2 == 0:
        print(house)
        print("This is an even number")


#looping by index
for i in range(len(houses)):
    if i % 2 == 0:
         print(houses[i])
