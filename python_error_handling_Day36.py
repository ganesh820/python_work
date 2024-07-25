
input_val = input("provide the input value :")

try :
    print(f"sequare of {input_val} is : {int(input_val) * int(input_val)}")

    for i in range(1, 10) :
        print(f"{input_val} * {i} = {int(input_val) * i}" )

except Exception as e :
    print(f"exception is been occured with error : {e}")


print("process finished")