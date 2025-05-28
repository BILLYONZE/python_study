# Takes a transaction amount and account type ("Standard" or "Premium") as input.
# If the account type is "Standard":
# Check if the amount is above 500:
# If it is, print "Transaction exceeds the limit for Standard accounts."
# If not, print "Transaction approved."
# If the account type is "Premium":
# Check if the amount is above 1,000:
# If it is, print "Transaction exceeds the limit for Premium accounts."
# If not, print "Transaction approved."
account_type = input("Enter account type (Standard/Premium): ").casefold()
if account_type == "standard":
    transaction_amount = input("Enter transaction amount: ")
    transaction_amount = int(transaction_amount)
    if transaction_amount > 500:
        print("Transaction exceeds the limit for Standard accounts.")
    else:
        print("Transaction approved.")
elif account_type == "premium":
    transaction_amount = input("Enter transaction amount: ")
    transaction_amount = int(transaction_amount)
    if transaction_amount > 1000:
        print("Transaction exceeds the limit for Premium accounts.")
    else:
        print("Transaction approved.")
else:
    print("account type you inserted is wrong")

