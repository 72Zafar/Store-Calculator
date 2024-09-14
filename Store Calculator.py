# CREATE A SIMPLE CALCULATOR FOR STORE

sum = 0
while(True):
    user = input("Enter the item price or press q to quit: \n")
    if (user != "q"):
        sum = sum + int(user)
        print (f"Order total so far: {sum}")
    else:
        print(f"your bill total is {sum}. thanks for shopping with us")    
        break