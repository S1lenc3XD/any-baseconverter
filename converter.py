while True:
    while True:
        try:
            frombase = input("What base number would you like to like to convert from? ")
            frombase = int(frombase)
            break
        except ValueError:
            print("Invalid input. Please enter a valid number.")
    
    while True:
        try:
            tobase = input("What base number would you like to convert to? ")
            tobase = int(tobase)
            break
        except ValueError:
            print("Invalid input. Please enter a valid number.")
    
    while True:
        try:
            fromnum = input("Enter your base " + str(frombase) + " number that you want to convert to base " + str(tobase) + ": ")
            fromnum = int(fromnum, frombase)
            break
        except ValueError:
            print("Invalid input. Please enter a valid base " + str(frombase) + " number.")
    
