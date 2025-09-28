#By default, a nested function can read outer variables but cannot change them.
#Using nonlocal to Modify Enclosing Variables
import random

def out():
    message = "Hello"

    def inner():
        nonlocal message
        message = "Hi"
        print("Inner:", message)

    inner()
    print("Outer:", message)

out()

#dictionary

job = {
    "softwareengineer": "kelli",
    "dataeengineer": "john",
    "sienceeengineer": "aleko",
}

illion = job.get("softwareengineer")
ikk = job["dataeengineer"]

job["eeeee"] = "whole"
print(illion)
print(ikk)
print(job)



# Step 1: generate a list of random numbers (with duplicates possible)
numbers = [random.randint(1, 10) for _ in range(20)]  # generate 20 random numbers
convertset = set(numbers)
print("Generated numbers:", convertset)


generaterandy = []

for _ in range(1,21):
    generaterandy.append(random.randint(1,8))

print(generaterandy)

import math_functions

result = math_functions.add(3,6)
print(result)