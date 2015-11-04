from bike_model import Bicycle, Shop, Customer

#import bike_model
#cannondale - bike_model.Bicycle

cannondale = Bicycle("Model C", 20, 600)        
mongoose = Bicycle("Model M", 25, 550)
schwinn = Bicycle("Model S", 28, 400)
huffy = Bicycle("Model H", 30, 300)
trek = Bicycle("Model T", 32, 200)
diamondback = Bicycle("Model D", 35, 150)
listof_bike_objects = [cannondale, mongoose, schwinn, huffy, trek, diamondback]

shop1 = Shop("Hans' Shop", listof_bike_objects)

customer1 = Customer("Tudor", 200, True)
customer2 = Customer("Jon", 500, True)
customer3 = Customer("Bob", 1000, True)


price1 = shop1.price()
customer_interest = customer1.affordability(price1)
print "Store model availability: " + str(shop1.availability("none")) 
customer_choice = customer1.purchase(customer_interest) 
sale1 = shop1.gains(customer_choice)
shop1.availability(customer_choice)
print "\n"

price2 = shop1.price()
customer_interest = customer2.affordability(price2)
print "Store model availability: " + str(shop1.availability("none"))
customer_choice = customer2.purchase(customer_interest)
sale2 = shop1.gains(customer_choice)
shop1.availability(customer_choice)
print "\n"

price3 = shop1.price()
customer_interest = customer3.affordability(price3)
print "Store model availability: " + str(shop1.availability("none")) 
customer_choice = customer3.purchase(customer_interest)
sale3 = shop1.gains(customer_choice)
shop1.availability(customer_choice)
print "\n"

final_store_inventory = shop1.price()
print "Shop1 remaining inventory: " + str(final_store_inventory) + "\n"
print "Store profit: $"+ str(sale1 + sale2 + sale3)