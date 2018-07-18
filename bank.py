##################### Bank Account Application #####################
accountNumber = 0
userDetails, accountNumberList = [], []

# Welcome menu option for the banking system
def main():
    # System will run until we quit the application
    while True:
        value = menu()
        print("\t")
        if value == 1:
            print("{0:#^51}\n{1}" .format(" Creating new account ", "Please enter the individuals"))
            print("{0:7}" .format(" "), end = "")
            # Input the first Name
            firstName = input("First Name: ").title()
            print("{0:7}" .format(" "), end = "")
            # Input the last name
            lastName = input("Last Name: ").title()
            print("{0:7}" .format(" "), end = "")
            # Input the initial balance
            beginingBalance = eval(input("Begining Balance (USD): "))
            (firstName, lastName, accountNumber) = createNewAccount(firstName, lastName, beginingBalance)
            print("New account created for {0} {1} (Account# {2})" .format(firstName, lastName, accountNumber))
        elif value == 2:
            creditOrDebit()
        elif value == 3:
            accountListing()
        elif value == 4:
            accountHistory()
        elif value == 5:
            totalAmount = bankTotalBalance()
            print("The total amount in the bank: ${0:,.2f}".format(totalAmount))
        elif value == 6:
            print("{0:#^51}".format(" Thank You "), end = "\n\n")
            exit()
        else:
            print("Menu not available!!! Select the available options")

def menu():
        # Create a list for menus
        menuList = ["1)", "Create new account",
                    "2)", "Credit/Debit an account",
                    "3)", "List all accounts",
                    "4)", "List account history",
                    "5)", "Bank total balance",
                    "6)", "Quit"]
        print("\t")
        print("{0:#^51}".format(" Welcome to my Bank "))
        # Display the options available
        for i in range(0, (len(menuList) - 1), 2):
            print("{0:^6s}{1}" .format(menuList[i], menuList[i + 1]))
        # Select the option
        value = int(input("What would you like to do (Enter any option between 1 to 6): "))
        return value

# Creating a new account
def createNewAccount(firstName, lastName, balanceToSimulate):
    global accountNumber, userDetails
    beginingBalance = balanceToSimulate
    # Automatically assign account number for every account creation
    accountNumber += 1
    # print("New account created for {0} {1} (Account# {2}) {3}" .format(firstName, lastName, accountNumber, beginingBalance))
    # Create the list of list to track the details of user
    userDetails.append([accountNumber, firstName, lastName, beginingBalance, beginingBalance])
    # Create the list of list to track the initial balance
    # intialBalance.append([accountNumber, firstName, lastName, beginingBalance])
    return (firstName, lastName, accountNumber)

# Crediting/Debiting an account
def creditOrDebit():
    print("{0:#^51}".format(" Crediting/Debiting an account "))
    # Input account number for which the amount should be credited or debited
    accountNum = int(input("Please enter the account number: "))
    # Call usValid() to check the given number is valid or not
    for userDetail in userDetails:
        accountNumberList.append(userDetail[0])
    if accountNum not in accountNumberList:
        print("Enter valid account number!!!")
    else:
        # Look the details of account number entered to credit or debit the available balance
        for userDetail in userDetails:
            if accountNum == userDetail[0]:
                # Input the amount
                amount = eval(input("Please enter the amount: "))
                # Append the amount credited or debited to track the transaction history
                userDetail.append(amount)
                previousAmount = userDetail[3]
                userDetail[3] += amount
                # Determine whether the amount is credited or debited
                if userDetail[3] < previousAmount:
                    creditOrDebit = "debited"
                else:
                    creditOrDebit = "credited"
                # Display the result
                print("{0} {1} (Account# {2}) {3} ${4:,.2f}\nNew balance: ${5:,.2f}" .format(userDetail[1], userDetail[2], userDetail[0], creditOrDebit, abs(amount), userDetail[3]))
                break

# Listing of all accounts
def accountListing():
    print("{0:#^51}".format(" Accounts list "))
    # Create Header
    print("{0:<10}{1:15}{2:16}{3:>9}" .format("Account#", "FirstName", "LastName", "Balance"))
    for userDetail in userDetails:
        print("{0:<10}{1:15}{2:15}${3:>9,.2f}" .format(userDetail[0], userDetail[1], userDetail[2], userDetail[3]))

# Listing transaction history for a given account number
def accountHistory():
    print("{0:#^51}".format(" Transaction history "))
    accountNum = int(input("Please enter the account number: "))
    # Check the given number is valid or not
    for userDetail in userDetails:
        accountNumberList.append(userDetail[0])
    if accountNum not in accountNumberList:
        print("Enter valid account number!!!")
    else:
        # Display account number and name for given account number
        for userInfo in userDetails:
            if accountNum == userInfo[0]:
                print("#{0:<6}{1} {2}" .format(accountNum, userInfo[1], userInfo[2]))
                break
        # Create a list for transaction history
        if len(userInfo) > 5:
                transactionHistory = userInfo[5:]
                availableBalance = userDetails[accountNum-1][4]
                for value in transactionHistory:
                    if value > 0:
                        sign = "+"
                    else:
                        sign = "-"
                    # Format the result to display
                    print("${0:>9,.2f}{2:>6}${1:>9,.2f}" .format(availableBalance, abs(value), sign))
                    availableBalance += value
                print("${0:>9,.2f}" .format(userInfo[3]))
        else:
            print("${0:,.2f}" .format(userInfo[3]))

# Calculate the total amount the bank currently holds
def bankTotalBalance():
    total = 0
    for userDetail in userDetails:
        total += userDetail[3]
    return total

# Function to clear the lists
def clearAccounts():
    global userDetails
    userDetails = []


# Call main()
# main()
