try:
    num1 = int(input("Enter the firt number:"))
    num2 = int(input("Enter the firt number:"))
    result =  num1 / num2 
    print("Result:", result)
except  ZeroDivisionError:
    print("Error: You cannot divide by zero.")
        
       
    
          
   


try:
    f = open("testfile.txt")
    var = bad_var
except FileNotFoundError as e:
    print(e)
# except Exception:
#     print("Sorry.This file doesnt exist")

finally:
    print("orinttt")
        