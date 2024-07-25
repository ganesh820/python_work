
input_val = input("input val is : ")
# input_val = int(input_va)

def multiply(input_val) :
    input_va = int(input_val)
    try :
        return input_va* input_va

    except Exception as e :
        return e

    finally :
        print("process is been completed")


result = multiply(input_val)

print(f"final result is {result}")



## We go for Finally block when we have resources which we needs to close before exiting the code.
# these resources can be Database connection, credentials inactivation, files closing or May be
# ending the program with delightfull messages.