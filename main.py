from mohasebe1 import *
from mohasebe2 import *

def main():

    principal = float(input("enter loan amount : "))
    annual_interest_rate = float(input("enter annual interest rate amount : "))
    duration = int(input("enter loan duration in year : "))

    print("loan amount :", principal , "interest rate", annual_interest_rate )

    z = mpmbv(principal,annual_interest_rate,duration)
    
    for i in range (1,1+duration) :

        print("duarion(years) : ", duration, "monthly payment : ", mpmbv(principal,annual_interest_rate,duration))
        print("year : ", i, "balance : ", mmbyv(principal,annual_interest_rate,duration,(i*12)), "total payment : ", int(z*i*12))


main()
