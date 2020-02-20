from fpdf import FPDF
import os


class Reports:
    def __init__(self, house, fo):
        self.pdf = FPDF(unit='in', format='letter')
        self.report_title = os.path.join('homes', house.address, f'{house.address}.pdf')
        self.house = house
        self.fo = fo
        self.fo.down_unfinanced()

    def initialize_report(self):
        self.pdf.set_font('Arial', size=12)


    def ammoritization(self):
        self.pdf.add_page()
        self.pdf.cell(8,.5, txt=f'Amoritization Schedule', ln=1, align='C')
        self.pdf.image(os.path.join('homes',self.house.address,'graphs', 'amoritization.png'), x=1, y=1.5, w=6)
        self.pdf.ln(6)
        amr = self.fo.ammoritization
        year5 = self.house.price*(1.05)**(5)-amr[60]
        year5 = round(year5,2)
        year10 = self.house.price*(1.05)**(10)-amr[120]
        year10 = round(year10,2)
        s1=f'On the assumption that the home value increases an average of 5% a year, the value of the home compared to the remaining balance on the loan will be {year5}.'
        s2=f'On the same assumption, the value compared to the remaining loan balance after 10 years will be {year10}. Industry trends will all but guarentee a net gain in value after'
        s3=f'a ten year period. If profitable, the investment exit plan will be to sell the home at the 5 year mark, but if future economic conditions are unfavorable to a sale at that time'
        s4=f'the exit strategy will wait up to the ten year mark to tell the property'
        self.pdf.multi_cell(8, .2, txt=f'{s1} {s2} {s3} {s4}', align='L')

    def monthly_breakdown(self):
        self.pdf.add_page()
        self.pdf.cell(8,.5, txt=f'Monthly Expenses', ln=1, align='C')
        self.pdf.image(os.path.join('homes',self.house.address,'graphs', 'cost_dist.png'), x=1, y=1.5, w=6)
        self.pdf.ln(6)
        rent = self.house.rent
        rooms = self.house.rooms
        ccost = self.fo.closing_costs
        coc = self.fo.coc
        apr = self.fo.mo_rate
        loan = self.fo.loan_amount
        taxes = self.fo.home.tax
        mcost = self.fo.mortgage+self.fo.home_insurance/12+rent*self.fo.management_fee+self.fo.home.tax
        mcost = round(mcost, 2)

        s1 = f'The market rate rent for this {rooms} bedroom home is {rent}$ a month. The total monthly costs are estimated to be {mcost}, and the total monthly cashflow is estimated to be {rent-mcost}'
        self.pdf.multi_cell(8, .2, txt=f'{s1}', align='L')


    def summary(self):
        self.pdf.add_page()
        name = self.house.address
        self.pdf.ln(1)
        self.pdf.cell(8, 0.5, txt=f'Summary for {name}', ln=1, align='C')
        mcost = self.fo.mortgage+self.fo.home_insurance/12+self.house.rent*self.fo.management_fee+self.fo.home.tax
        s1 = f'{self.house.address} is a {self.house.rooms} bedroom single family home on sale for a purchase price of {self.house.price}$. This report shows the cash flow opportunities when purchasing this property with a 20% down payment of {round(self.fo.down_payment, 2)} and a {self.fo.mo_rate*100}% APR loan of {self.fo.loan_amount}. At a market rate rent of {self.house.rent} and monthly costs of {round(mcost, 2)}, this property is expected to produce a monthly cashflow of {round(self.house.rent-mcost, 2)} and produce an annual cash on cash return of {round(self.fo.coc, 2)}.'
        self.pdf.multi_cell(8, .2, txt=s1, align='L')

    def save_report(self):
        name = self.house.address
        report_name = os.path.join('homes', name, f'{name}.pdf')
        self.pdf.output(report_name)


    def create_report(self):
        self.initialize_report()
        self.summary()
        self.monthly_breakdown()
        self.ammoritization()
        self.save_report()

