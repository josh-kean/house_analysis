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
    def __init__(self, price, rent, rooms, address):
        self.price = price
        self.rent = rent
        self.rooms = rooms
        self.address = address


class Mortgage:
    def __init__(self, home, downpayment=.2):
        self.home = home
        self.downpayment = downpayment*self.home.price 
        self.loan_ammount=self.home.price*(1-downpayment)
        self.pay_schedule = []
        self.rate = None
        self.monthly_payment = None
        self.future_growth = None
        self.dp_payoff = None
        self.coc = None

    def mortgage(self, rate):
        self.rate = rate/12 #input rate is annual rate, divided by 12 to show monthly rate
        self.monthly_payment = (self.rate*self.loan_ammount)/(1-(1+self.rate)**(-12*30))
        
    def loan_payment_schedule(self):
        #return list of months (all 360) and amount of loan paid to principal
        #amoritization is 
        self.pay_schedule = []
        loan_value = self.loan_ammount
        for m in range(360):
            pay_down = self.monthly_payment-loan_value*self.rate
            loan_value -= pay_down
            self.pay_schedule.append(int(loan_value))

    def cash_on_cash(self):
        self.coc = (self.home.rent-self.monthly_payment)*12.0/self.downpayment
        self.coc = round(self.coc, 3)

    def qualify_coc(self):
        return self.coc > .09

    def future_value(self):
        future_growth = []
        rate = self.rate*12
        for m in range(360):
            growth_rate = (1+rate)**(m/12)
            future_growth.append(self.home.price*growth_rate)
        self.future_growth = future_growth

    def down_payment_payoff(self, rate, years):
        #this is to calculate the additional cost of borrowing for a downpayment
        #usually this will be paid off at a higher interest rate but also over a shorter time period
        rate = rate/12
        self.dp_payoff = (rate*self.downpayment)/(1-(1+rate)**(12*years))
        effect = (self.sp_payoff + self.monthly_payment)/self.home.rent
        if effect => 1:
            return False
        return True

    def amoritize_graph(self):
        graphs = Graphs(self.pay_schedule, self.future_growth)
        graphs.amoritization()


if __name__ == '__main__':
    house = House(1_000_000, 1000, 3, '132 jefferson')
    mortgage = Mortgage(house)
    mortgage.mortgage(0.0455)
    mortgage.loan_payment_schedule()
    mortgage.future_value()
    mortgage.amoritize_graph()






