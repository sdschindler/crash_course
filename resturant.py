class resturant():

    def __init__(self,name,cu_type):

        self.name = name
        self.cu_type = cu_type

    def describe_resturant(self):
        print(self.name.title())
        print(self.cu_type)

    def open_resturant(self):
        print(self.name.title() + " is open")


my_resturant = resturant('china house','Chinese food')
print("My resturant name and cusine are " + my_resturant.name.title()+" and "+ my_resturant.cu_type)

my_resturant.describe_resturant()
my_resturant.open_resturant()
