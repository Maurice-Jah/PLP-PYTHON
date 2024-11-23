# print the final price  
# if the discount is 20% or higher apply discount else return price


def calculate_discount(price, discount_percent):
    if(discount_percent >= 20):
        discount = (discount_percent / 100 ) * price
        total_price = price - discount
        return total_price
    else:
        return price



# 2. prompt user to enter the original price and discount
user_input_price = float(input("Please enter the price "))
user_input_discount = float(input("Please enter the discount "))

final_price = calculate_discount(user_input_price,user_input_discount)
print(f"The price is {final_price}")

