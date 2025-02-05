
class Location:

    def __init__(self, name, country):
        self.name = name
        self.country = country
    
    def myLocation(self):
        print("Hi my name is " + self.name + " and I lived in " + self.country + ". ")

loc = Location("Paul", "South Africa")
loc1 = Location("Allon", "Malaysia")
loc2 = Location("Yu", "China")
loc3 = Location("Aman", "Oman")

loc3.myLocation()
loc2.myLocation()
loc1.myLocation()

print(loc.name)
print(loc.country)
print(type(loc))
