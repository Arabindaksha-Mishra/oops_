class User():
    #constructure is the class object
    def __init__ (self1,name,age,gender):
        self1.name=name
        self1.age=age
        self1.gender=gender

    def show_details(self):
        print("Name", self.name)
        print("Age",self.age)
        print("Gender",self.gender)
    
john=User("John",10,"Male")
john.show_details()

