
def mpmbv(principal,annual_interest_rate,duration):

    principal = float(principal)
    
    annual_interest_rate = float(annual_interest_rate)

    r = float( (annual_interest_rate / 100) / 12)

    n = int(duration * 12)

    if(r == 0):

        monthly_payment = float(principal / n)
        
    else:
        
        r = float( (annual_interest_rate / 100) / 12)
        
        monthly_payment = float( principal * (r * ( ( 1 + r ) ** n ) / ( ( ( 1 + r ) ** n) - 1 ) ) )

    return monthly_payment
