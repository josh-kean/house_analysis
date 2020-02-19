from fpdf import FPDF
import os


class Reports:
    def __init__(self):
        pass

    def text_report(self, house, fo):
        price = house[0]
        rooms = house[1]
        rent = house[2]
        addr = house[3]
        mcost = fo.mortgage+fo.home_insurance/12+rent*fo.management_fee
        ccost = fo.closing_costs
        coc = fo.coc
        loan = fo.loan_amount
        amr = fo.ammoritization
        dp = fo.down_payment
        year5 = house[0]*(1.05)**(5)-amr[60]
        year10 = house[0]*(1.05)**(10)-amr[120]
        s1 = f'{addr} is a {rooms} bedroom home listed for a price of {price}.'
        s2 = f'A 20% down payment of {round(dp,2)} will be required and the closing costs are estimated'
        s3 = f'to be {round(ccost,2)}. The monthly costs are estimated to be {round(mcost,2)}'
        s4 = f'and the market rate for this unit is {rent}, provding a monthly income of'
        s5 = f'{round(rent-mcost, 2)}. The cash on cash return for this unit is estimated to be {round(coc*100,2)}%.'
        return f'{s1} {s2} {s3} {s4} {s5}'


    def create_report(self, house, fo):
        fo = fo
        fo.down_unfinanced()
        name = house[3]
        report_name = os.path.join('homes', name, f'{name}.pdf')
        pdf = FPDF(unit='in', format='letter')
        pdf.add_page()
        pdf.set_font('Arial', size=12)
        pdf.cell(8,1, txt=f'Report on {name}', ln=1, align='C')
        pdf.image(os.path.join('homes',name,'graphs', 'amoritization.png'), x=1, y=1, w=6.5, h=6.5)
        pdf.ln(6.5)
        pdf.multi_cell(8, .2, txt=self.text_report(house, fo), align='L')
        pdf.output(report_name)
