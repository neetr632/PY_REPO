def sumdata(a, b=5):
    print(a+b)
    
def sumdata_2(a, b=5):
    c = a+b
    return c

def showdata():
    print("WScubetech")

if __name__ == "__main__":
    sumdata(20)  # a is assigned 20 by default
    showdata()  # calling a fucntion
    output = sumdata_2(200)
# return statement to print the value of the function outside the function
    print(output)
