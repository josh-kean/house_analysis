import copy
import numpy as np
import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt
import os

plt.style.use('seaborn-whitegrid')

class Graphs:
    def __init__(self):
        pass

    def expense_breakdown(self, save_loc, fo):
        fo = copy.deepcopy(fo)
        fo.down_unfinanced()
        labels = ['mortgage', 'home\ninsurance', 'management\nfee', 'property tax', 'profit']
        costs = [fo.mortgage, fo.home_insurance/12, fo.home.rent*fo.management_fee, fo.home.tax]
        costs.append(fo.home.rent-sum(costs))
        explode=(0.1, 0.1, 0.1, 0.1, 0.1)
        fig1, ax1 = plt.subplots()
        def func(pct, allvals):
            absolute = int(pct/100.*np.sum(allvals))
            return "{:.1f}%\n{:d}$".format(pct, absolute)
        ax1.pie(costs, explode=explode, labels=labels, autopct=lambda pct: func(pct, costs), shadow=True, startangle=90)
        ax1.axis('equal')
        plt.savefig(os.path.join(save_loc, 'cost_dist.png'))
        plt.close()

    def various_rates(self, save_loc, fo):
        rates = [3,4,5,6,7,8]
        rates_formatted = [f'{x}%' for x in rates]
        profits = []
        for rate in rates:
            temp_fo = copy.deepcopy(fo)
            temp_fo.mo_rate = rate/100
            temp_fo.down_unfinanced()
            profit = temp_fo.home.rent-sum([temp_fo.mortgage, temp_fo.home_insurance, temp_fo.home.rent*temp_fo.management_fee, temp_fo.home.tax])
            profits.append(int(profit))
        rates_formatted.append('loc')
        y_pos = np.arange(len(rates_formatted))
        final_fo = copy.deepcopy(fo)
        profits.append(int(final_fo.payment_calculation(final_fo.down_payment, 0.08, 60)))
        plt.bar(y_pos, profits);
        plt.xticks(y_pos, rates_formatted)
        plt.xlabel = ('profit')
        plt.ylabel = ('annual rate')
        plt.title('Profit v Interest Rate')
        plt.savefig(os.path.join(save_loc, 'profit-rates.png'))


    def amoritization(self, save_loc, fo):
        temp_f = copy.deepcopy(fo)
        fo.down_unfinanced()
        fig = plt.figure()
        ama_data = np.array([[x, fo.ammoritization[x]] for x in range(len(fo.ammoritization))])
        value_data = np.array([[x, fo.home.price*(1.05)**(x/12)] for x in range(len(fo.ammoritization))])
        x1, y1 = ama_data.T
        x2, y2 = value_data.T
        plt.plot(x1, y1, 'bo', linewidth=1, linestyle='solid', color='blue', markersize=0)
        plt.plot(x1, y2, 'r+', linewidth=1, linestyle='solid', color='red', markersize=0)
        plt.fill_between(x1, y2, y1, color='yellow')
        plt.xlim(0, len(fo.ammoritization)+20)
        plt.xticks(np.arange(min(x1), max(x1), 12), range(1,31))
        plt.ylim(0, int(value_data[-1][1]), 10)
        #plt.ylim(0, int(fo.home.price*2), 10)
        plt.title('amoritization-schedule')
        plt.xlabel('years')
        plt.ylabel('remaining-balance')
        plt.savefig(os.path.join(save_loc,'amoritization.png'))
        plt.close()
