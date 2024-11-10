# print the final price  
# if the discount is 20% or higher apply discount else return price


def calculate_discount(price,discount_percent):
    if(discount_percent >= 20):
        discount = (discount_percent / 100 ) * price
        total_price = price - discount
        return total_price
    else:
        return price


final_price = calculate_discount(200,20)
print(final_price)