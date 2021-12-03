# Mimi Ly Assignment 10.1 

#what we have in store and what the prices are

#prices of each part of item in dictionary
PRICES={
    'pink':5, 
    'black':2, 
    'white':3, 
    'small':2, 
    'medium':3, 
    'large':5, 
    'gucci':100, 
    'zara':20, 
    'uniqlo':35
    }

#sorted by color, size, brand here
COLOR={'pink':5, 'black':2, 'white':3}

SIZE={'small':2, 'medium':3, 'large':5}

BRAND={'gucci':100, 'zara':20, 'uniqlo':35}

#class for clothes and their prices in the inventory 
class Shop: 
    #class attribute
    tshirt="clothes" 
    #data attributes
    def __init__(self, color, size, brand):
        self._color=color
        self._size=size
        self._brand=brand
        self.total()

#returning the string of total of one item
    def __str__(self):
            return (f"Cost of clothing item: ${self.total}")

#setting the value and equation of one item based on coor, size, brand
    def set_total(self):  
        self._total=PRICES([self._color]+[self._size]+[self._brand])

#returning value of cost of one item based on color, size, brand
    def get_total(self): 
        return self.total 

#adding the cost of an item based on the color, size and brand
    def total(self):
        self.total=PRICES[self._color]+PRICES[self._size]+PRICES[self._brand]
        return self.total
   
#This function will check if the clothes obejct that was created is available.
#if not available, then print not avaliable
    def is_it_available(self, color, size, brand):
        if self._color == COLOR.keys and self._size == SIZE.keys and self._brand == BRAND.keys:
            print("This is available in this store.")
            return True
        else:
            print("We don't have this in this store.")
            return False

#printing out total cost based on how many items consumer wants to buy
    def total_price(self,color, size, brand,amount_purchased): #setting value 
        self._total_price= amount_purchased *(PRICES[self._color]+PRICES[self._size]+PRICES[self._brand])
        print(f"Total overall cost of clothing: ${self._total_price}")
        return self._total_price   


#test
def main():
    #what we are buying
    item=Shop("pink","large", "gucci")
    print (item)

    #checking if XXL is available
    item.is_it_available("purple", "XXL", "gucci")

    #we want to buy 3 of the same item
    item.total_price("pink", "large", "gucci", 3)

if __name__=="__main__":
    main()