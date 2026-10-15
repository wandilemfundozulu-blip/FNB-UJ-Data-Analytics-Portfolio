#Smart ATM Withdrawal Simulator

#Fixed Balance
balance = 500

#withdraw
withdrawal = float(input("Enter how much you wish to withdraw (R)"))

#if statement
if withdrawal <= 0:
    print("Invalid Amount. You must withdraw more than R0. ")

#elif statements
elif withdrawal <= balance:
     balance = balance - withdrawal
     print(f"Withdrawal successfull! Remaining balance: R{balance:.2f}")

#else staement 
else:
     print("Declined. Insufficient Fund")


