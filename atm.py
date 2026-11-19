balance = 5000 
amount = int(input("How much do you want to withdraw? "))

if amount <= 0:
    print("Invalid amount.")

elif amount > balance:
    print("Insufficient funds.")

else:
    balance -= amount
    print(f"Transaction successful. Your new balance is: {balance}")
