# Simple Python Income calculator, Based on inpoutted tax

tax = input("Enter your income tax:")

ValidValue = False

try:
    tax = float(tax)

except ValueError:
    ValidValue = True
    print("Invalid amount!")

if tax < 0:
    print("Invalid amount!")

else:
    # If the tax paid is 0, the assumed annual income is 12,500
    if tax == 0.00:
        annualincome = 12500.00
    
    elif tax <= 10000.00 and tax > 0.00:
        annualincome = -12500.00
        annualincome = round(tax/0.2, 2)
        annualincome += 12500.00

    elif tax <= 60000.00 and tax > 10000.00:
        tax -= 7500.00
        annualincome = round(tax/0.4, 2)
        annualincome += 37500.00 + 12500.00

    elif tax > 60000.00:
        tax -= 47500.00
        annualincome = round(tax/0.45, 2)
        annualincome += 12500.00 + 37500.00 + 100000.00

print(f'Your estimated income, based on the amount of tax you pay is: £{annualincome:.2f}')
