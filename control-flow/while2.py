message = "Hello, world"

for x in message:
    print(x)

for number in range(1, 6):
  print(number)

# summ of nubers in a list 
numbers = [1, 5, 3, 9]

for total in numbers:
   total +=total
   print(total)

# while loop

# secret = 7 

# guess_count = 0
# guess = 0

# while guess != secret:
#    guess_count += 0 
#    guess = int(input("Guess a number between 1 and 10: "))

# print(F"You have guessed it in {guess_count}")

count = 0
while count <= 5:
    count += 1
    print(f"Count: {count}")

#Decremental counter:

y = 3
while y > 0:
   print(y)
   y -= 1
print("blast")

y = 4
while y < 30:
   print(y)
   y *= 2


attempts = 0
max_attempt = 4

while attempts < max_attempt:
   password = input("Enter password : ")
   if password == "secret":
      print("Access granted")
      break
   else:
      attempts += 1
      print(f"Wrong password. Attempts left: {max_attempt-attempts}")

if attempts == max_attempt:
   print("Account locked")


#while loop pattern

# counter = 0
# while True:
#    counter +=1

#    if somecondition:
#       break