class Movie:

    def __init__(self, title, rating, release_year):
        self.title = title
        self.rating = rating
        self.release_year = release_year
    

class Owner:
    def __init__(self, age)
        self.age = age
#Decorator
def coupon_calculator(func): #takes in a function as an argument
    #Inner function
    def report_price():
        print(f'Iniital price = $35.00')
        final_price = func(35.00)
        print(f'Discounted price = ${final_price}')
    
    return report_price

#Callback function to calculate new price
def calculate_price(price):
    #We end up with a floating point number 
    #rounded to the nearest hundredth
    return '{:2f}'.format(round(price / 2, 2))

report_price = coupon_calculator(calculate_price)
report_price()
    
