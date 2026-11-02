principal = float(input("Enter principal amount: "))
rate = float(input("Enter annual interest rate (%): "))
time = float(input("Enter time in years: "))

interest = principal * rate * time / 100
total = principal + interest

print(f"Simple interest: {interest:.2f}")
print(f"Total amount: {total:.2f}")