#

def main():
    print("Change Counter, by Khalid Hussain", "\n")

    price = float(input("Price?: "))
    amount_tendered = float(input("Amount tendered?: "))
    change_due = round(amount_tendered - price, 2)

    price_for_me = int(price * 100)
    amount_tendered_for_me = int(amount_tendered * 100)
    change_for_me = int(amount_tendered_for_me - price_for_me)

    print("\n", "Report", "\n", "==========")
    print("Purchase Price: ", price)
    print("Amount Tendered: ", amount_tendered, "\n")
    print("Change: ", change_due)

    one_dollar_bills = int(change_for_me / 100)
    print(one_dollar_bills, "one-dollar bills")
    change_for_me = change_for_me%100
    print(change_for_me// 25, "quarters")
    change_for_me = change_for_me%25
    print(change_for_me//10, "dimes")
    change_for_me = change_for_me%10
    print(change_for_me//5, "nickles")
    change_for_me = change_for_me%5
    print(change_for_me//1 , "pennies")

main()
