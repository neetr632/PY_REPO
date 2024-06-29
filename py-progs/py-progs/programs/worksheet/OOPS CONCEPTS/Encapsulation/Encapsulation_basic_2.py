#private variables are not directly intiated by creating a object.
class Student:
    __name="ravi"  #private instance variable created not accessible outside the class. 
    def __init__(self): #example of a constructor.
        print(self.__name) # printing the value of the PIV
        self.__displayinfo() #private function "__" indicates its private nature of the function
    def __displayinfo(self):
        print("welcome to WScubetech")
        
object=Student()
        #cannot be accessed outside the class whether its the variable or the fucntion