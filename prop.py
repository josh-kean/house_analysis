from graphs import Graphs 

#this program calculates the monthly payments on a house,
#explores various financing scenarios, and determines the cash flow opportunity of a home

#todo
#calculate mortgage payments
#calculate amoritization rate
#calculate downpayment
#find extra loan for downpayment rate
#create 5 and 10 year cash out scenario

class House:
    def __init__(self, price, rooms, address, appreciation=1.05):
        self.price = price
        self.rooms = rooms
        self.address = address
        self.appreciation = appreciation

    def home_value(self, duration):
        #returns a list of home value increase over duration (in years)
        return [self.price*(1.05)**(x/12) for x in range(duration*12)] 


#only down_financed and down_unfinanced should ever be called from the outside
class FinancialObject:
    def __init__(self, home, tax=None, home_insurance=0.015, closing_costs = 0.075, management_fee=0.05):
        self.home = home
        self.loan_amount = None
        self.closing_costs = closing_costs
        self.mortgage = None
        self.finance_payment = None
        self.down_payment = None
        self.loan_insurance_payment = None
        self.min_rent = None
        self.home_insurance= home_insurance
        self.management_fee = management_fee
        self.ammoritization = []
        self.payments = []

    def final_costs(self):
        self.home_insurance = self.home.price*self.home_insurance
        self.closing_costs = self.loan_amount*self.closing_costs

    #assuming a 30 year payment schedule unless otherwise stated
    def payment_calculation(self, loan, rate, period=360):
        return ((rate/12)*(loan))/(1-(1+rate/12)**-period)

    def pay_down(self, rate, period, loan, payment, m):
            return (((1+rate/12)**m)*loan)-(((1+rate/12)**m)-1)*payment/(rate/12)

    def min_rent_calc(self):
        #want to return minimum rental rate to achieve 10% cash on cash
        #rent = down_payment*.1+payment
        self.min_rent = ((self.closing_costs+self.down_payment)*.1+(self.payments[0]+self.home_insurance/12+self.home_insurance))/(1-self.management_fee)

    def amoritize(self, rate, period, loan, rate2=None, period2=None, loan2=None):
        self.amoritization = []
        for m in range(1,period+1): #need to have first month start as 1 and end month equal period
            paydown = self.pay_down(rate, period, loan, self.mortgage, m)
            if loan2 and m < period2+1:
                paydown += self.pay_down(rate2, period2, loan2, self.finance_payment, m)
            self.amoritization.append(paydown)

    def loan_insurance(self, rate, period):
        #apply loan insurance to payments if down_payment is less than 20% of purchase price
        #assuming a .5% annual rate, or (.005%12)% monthly rate
        insurance_rate = .005/12
        self.loan_insurance_payment = self.loan_amount*insurance_rate
        remaining_loan = self.loan_amount
        i = 0
        while remaining_loan/self.home.price > .8:
            self.payments[i] += self.loan_amount*insurance_rate
            remaining_loan = self.pay_down(rate, period, self.loan_amount, self.mortgage, i)
            i +=1

    #assuming a 5% rate for all calculations unless provided otherwise
    #assuming 20% down, can change
    def down_unfinanced(self, dp=0.2, rate=0.05, period=360): 
        self.down_payment = self.home.price*(dp)
        self.loan_amount = self.home.price - self.down_payment
        self.finance_payment = None
        self.mortgage = self.payment_calculation(self.home.price-self.down_payment, rate, period)
        self.payments = [self.mortgage for x in range(period)]
        if dp < .2:
            self.loan_insurance(rate, period)
        self.amoritize(rate, period, self.loan_amount)
        self.final_costs()
        self.min_rent_calc()

    #assuming 5% rate for all calculations unless provdied otherwise
    #assuming 20% down, can change
    #assuming 15% apr for down payment financing
    def down_financed(self, dp_rate=0.15, dp_period=60, dp=0.2, rate=.05, period=360):
        self.down_payment = self.home.price*dp
        self.loan_amount = self.home.price - self.down_payment
        self.mortgage = self.payment_calculation(self.home.price-self.down_payment, rate, period)
        self.finance_payment = self.payment_calculation(self.down_payment, dp_rate, dp_period)
        self.payments = [self.mortgage for x in range(period)]
        for x in range(dp_period):
            self.payments[x] += self.finance_payment
        if dp < .2:
            self.loan_insurance(rate, period)
        self.amoritize(rate, period, self.loan_amount, dp_rate, dp_period, self.down_payment)
        self.final_costs()
        self.min_rent_calc()
