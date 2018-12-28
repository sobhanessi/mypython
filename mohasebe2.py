
def mmbyv(principal, annual_interest_rate, duration , number_of_payments):

    principal = float(principal)
    
    annual_interest_rate = float(annual_interest_rate)

    r = float( (annual_interest_rate / 100) / 12)

    n = int(duration * 12)

    p = int(number_of_payments)

    if(r == 0):

        remaining_loaon_balance =  float(principal* (1 - (p/n)))

    else:

        remaining_loan_balance = float( principal * ( (((1+r)**n) - ((1+r)**p)) / (((1+r)**n)-1) ))

    return remaining_loan_balance
