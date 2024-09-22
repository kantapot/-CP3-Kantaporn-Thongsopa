class Customer:
    name = ""
    lastName = ""
    age = 0

    def addCart(self):
        print("Added to " +self.name+ " " +self.lastName + "'s cart")

customer1 = Customer()
customer1.name = "Yo"
customer1.lastName = "Kan"
customer1.age = 27

customer2 = Customer()
customer2.name = "Praw"
customer2.lastName = "Nut"
customer2.age = 25

customer3 = Customer()
customer3.name = "Ploy"
customer3.lastName = "lali"
customer3.age = 31

customer1.addCart()
customer2.addCart()
customer3.addCart()
