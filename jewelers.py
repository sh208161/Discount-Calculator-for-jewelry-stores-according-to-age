# Get user inputs
name = input("Enter your name: ")
gender = input("Enter gender (M/F): ").upper()
age = int(input("Enter age: "))

product = input("Enter product: ")
product_gram = int(input(f"Enter {product} gram: "))
gold_price_per_gram = 5752

# Calculate total gold rate
total_gold_rate = product_gram * gold_price_per_gram
print("\nTOTAL GOLD RATE:", total_gold_rate)

# Calculate total making charges
making_charges_per_gram = 845
total_making_charges = product_gram * making_charges_per_gram
print("Total Making Charges:", total_making_charges)

# Calculate total amount before discount
total_amount = total_gold_rate + total_making_charges
print("\nTOTAL AMOUNT:", total_amount)

# Determine discount percentage based on age, gender, and total purchase amount
discount_percentage = 0

if gender == 'M':
    if age > 65:
        if total_amount > 200000 and total_amount <= 300000:
            discount_percentage = 20
        elif total_amount > 300000 and total_amount <= 500000:
            discount_percentage = 30
        elif total_amount > 500000:
            discount_percentage = 35
    else:  # Age <= 65
        if total_amount > 200000 and total_amount <= 300000:
            discount_percentage = 10
        elif total_amount > 300000 and total_amount <= 500000:
            discount_percentage = 20
        elif total_amount > 500000:
            discount_percentage = 25

elif gender == 'F':
    if age > 65:
        if total_amount > 200000 and total_amount <= 300000:
            discount_percentage = 25
        elif total_amount > 300000 and total_amount <= 500000:
            discount_percentage = 35
        elif total_amount > 500000:
            discount_percentage = 40
    else:  # Age <= 65
        if total_amount > 200000 and total_amount <= 300000:
            discount_percentage = 15
        elif total_amount > 300000 and total_amount <= 500000:
            discount_percentage = 25
        elif total_amount > 500000:
            discount_percentage = 30

# Calculate discount amount and net total
discount_amount = (discount_percentage / 100) * total_amount
net_total = total_amount - discount_amount

print("\nDISCOUNT:", discount_percentage, "%")
print("DISCOUNT AMOUNT:", discount_amount)
print("\nTOTAL NET AMOUNT:", net_total)
