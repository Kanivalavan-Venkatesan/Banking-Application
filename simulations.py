# Import the required functions from random and bank modules
from random import normalvariate
from bank import createNewAccount, bankTotalBalance, clearAccounts
'''
Dictionary abbreviation
CSP = College Student Plan
SCP = Senior Citizens Plan
ECA = Expected Customer Acquisition
ECA-SD = Expected Customer Acquisition Standard Deviation
EB = Expected Balance
EB-SD = Expected Balance Standard Deviation
'''
# Create dictionary for bank plans
planDetails = {"CSP":{"marketingSpend":25000, "ECA":100000, "ECA-SD":15000, "EB":3000, "EB-SD":750},
               "SCP":{"marketingSpend":25000, "ECA":60000, "ECA-SD":7500, "EB":10000, "EB-SD":2500}}
# Hearder list
headerTitle = ["Marketing Spend (in $)",
               "Exp. Customer Acquisition",
               "Exp. Customer Acquisition SD",
               "Exp. Balance (in $)",
               "Exp. Balance SD (in $)",
               "Exp. Total Deposits (in $)",
               "Exp. ROI (in $)"]

def main():
    planDetails = expectedTotalDeposit()
    planDetails = expectedROI(planDetails)
    displayStatistics(planDetails)

# Calculate the expected totol balance by simulating the bank applicaton
def expectedTotalDeposit():
    totalDepositCSP, totalDepositSCP = 0, 0
    firstName = "Account"
    lastName = "Holder"
    numberOfTrails = 1000
    # Compute the average expected total balance for two plans
    for trail in range(numberOfTrails):
        numberOfAccountsCSP = int(simulation('CSP', 'ECA', 'ECA-SD'))
        numberOfAccountsSCP = int(simulation('SCP', 'ECA', 'ECA-SD'))
        for account in range(numberOfAccountsCSP):
            balanceToSimulate = simulation('CSP', 'EB', 'EB-SD')
            createNewAccount(firstName, lastName +'_'+ 'CSP', balanceToSimulate)
        totalAmount = bankTotalBalance()
        totalDepositCSP += totalAmount
        clearAccounts()
        for account in range(numberOfAccountsSCP):
            balanceToSimulate = simulation('SCP', 'EB', 'EB-SD')
            createNewAccount(firstName, lastName +'_'+ 'SCP', balanceToSimulate)
        totalAmount = bankTotalBalance()
        totalDepositSCP += totalAmount
        clearAccounts()
    planDetails['CSP']['totalBalance'] = round(totalDepositCSP / numberOfTrails)
    planDetails['SCP']['totalBalance'] = round(totalDepositSCP / numberOfTrails)
    return planDetails

# Calculate the return on investment for the two plans
def expectedROI(planDetails):
    for plan in planDetails:
        roi = ((planDetails[plan]["totalBalance"]) * 0.10) - (planDetails[plan]["marketingSpend"])
        planDetails[plan]["expectedROI"] = round(roi)
    return planDetails

# Display the result
def displayStatistics(planDetails):
        planDetailList = []
        # Dsplay the Header
        print("{0:-^85}\n{1:30}{2:^30}{3:^30}\n{0:-^85}".format("-", "Statistic", "College Students Plan", "Senior Citizens Plan"))
        # Display the statistics
        listView = list(planDetails.values())
        for listvalue in listView:
            planDetailList.append(list(listvalue.values()))
        planDetailList.insert(0, headerTitle)
        for position in range(7):
            print("{0:30}{1:>25,}{2:>30,}".format(planDetailList[0][position], planDetailList[1][position], planDetailList[2][position]))
        print("{0:-^85}".format('-'))

# Simulate the balance and number of accounts
def simulation(plan, mean, standardDeviation):
    simulate = normalvariate(planDetails[plan][mean], planDetails[plan][standardDeviation])
    return simulate

# Call main()
main()
