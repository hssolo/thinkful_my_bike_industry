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
        
    def availability(self, sold):
        """extracts model name from Bicycle object and updates inventory"""
        #import pdb; pdb.set_trace()
        model_name_availability = []
        for x in self.store_inventory:
            model_name_availability.append(x.model)
        for x in self.store_inventory:
            if sold == x.model: 
                self.store_inventory.remove(x)
        return model_name_availability
        
    def price(self):
        store_price = {}    
        for x in self.store_inventory:
            store_price[x.model] = x.cost + x.cost * .2
        return store_price 
        
    def gains(self, sold):
        #profit = False
        for x in self.store_inventory:
            if sold == x.model:
                self.profit = x.cost * .20
        return self.profit
            
        
class Customer(object):
    def __init__(self, name, budget, can_own_bike):
        self.name = name
        self.budget = budget
        self.can_own_bike = can_own_bike
        
    def affordability(self, store_price):
        bikes_within_budget = {}
        print "Customer: " + self.name
        for x in store_price:
            if store_price[x] <= self.budget:
                bikes_within_budget[x] = store_price[x]
        print "Customer Affordability: " + str(bikes_within_budget.keys())
        return bikes_within_budget
        
    def purchase(self, affordable_options):
        import random
        customer_decision = random.choice(affordable_options.items())
        print "Customer Purchase: " + str(customer_decision)
        print "Customer left over budget: $" + str(self.budget - customer_decision[1])
        return str(customer_decision[0])
        
        
