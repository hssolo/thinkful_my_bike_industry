class Bicycle(object):
    def __init__(self, model, weight, cost):
        self.model = model
        self.weight = weight
        self.cost = cost
        

class Shop(object):
    def __init__(self, store_name, store_inventory):
        self.store_name = store_name
        self.store_inventory = store_inventory
        self.profit = 0
        
    def availability(self, sold): # sold parameter is either "none" or the value of the Customer object purchase() function.
        """extracts model name from list of Bicycle objects and updates ths store inventory either 
            before or after a sale"""
        #import pdb; pdb.set_trace()
        model_name_availability = []
        for x in self.store_inventory:
            model_name_availability.append(x.model)
        for x in self.store_inventory:
            if sold == x.model: 
                self.store_inventory.remove(x)
        return model_name_availability
        
    def price(self): # this is the first function called as an argument from the Cusotmer object affordability() function.
        """extracts the model name and cost from the object store_inventory and creates a new dict with an added 20% increase"""
        store_price = {}    
        for x in self.store_inventory:
            store_price[x.model] = x.cost + x.cost * .2
        return store_price 
        
    def gains(self, sold):
        for x in self.store_inventory:
            if sold == x.model:
                self.profit = x.cost * .20
        return self.profit
            
        
class Customer(object):
    def __init__(self, name, budget, can_own_bike):
        self.name = name
        self.budget = budget
        self.can_own_bike = can_own_bike
        
    def affordability(self, store_price): #store_price comes from shop object price() function which extracts the price of each model available from the shop object and creates a new dictionary.
        """Initial function ran from the program that compares the bike 
            shop prices of each model and compares it to the customers budget"""
        bikes_within_budget = {}
        print "Customer: " + self.name
        for x in store_price:
            if store_price[x] <= self.budget:
                bikes_within_budget[x] = store_price[x]
        print "Customer Affordability: " + str(bikes_within_budget.keys())
        return bikes_within_budget
        
    def purchase(self, affordable_options):
        customer_decision = random.choice(affordable_options.items())
        print "Customer Purchase: " + str(customer_decision)
        print "Customer left over budget: $" + str(self.budget - customer_decision[1])
        return str(customer_decision[0])
        
        
