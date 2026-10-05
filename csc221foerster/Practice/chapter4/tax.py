income = float(input("Enter your income. Don't lie!: "))
tokens = round(income, 2)
tax = 0.00

if 0 < tokens < 22111.00:
    tax = round((tokens * 0.18) - 156.02)
elif tokens > 22111.00:
    tax = round((tokens * 0.62) + 8102.02)
else:
    tax = 0

print(f"The tax is: {tax} tokens")
