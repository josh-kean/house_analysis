import numpy as np
import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt

plt.style.use('seaborn-whitegrid')

class Graphs:
    def __init__(self, mortgage):
        self.mo = mortgage


    def iter_through_items(self, row, width, items):
        for i in range(len(items)):
            if i > 0:
                plt.bar(row, items[i], width, bottom=items[i-1])
            else:
                plt.bar(row, items[i], width)

    def price_breakdown(self):
        width=.25
        breakdown = [max(self.mo.payments), mo.home_insurance, mo.management_fee, mo.finance_payment]
        rent = plt.bar(0, mo.min_rent, width)

        self.iter_through_items(1, width, breakdown)
        if max(self.mo.payments) != min(self.mo.payments):
            breakdown[0] = min(self.mo.payments)
            self.iter_through_items(2, width, breakdown)

        plt.title('rent breakdown')
        plt.yticks('rent', 'breakdown')
        plt.xticks(np.arange(0, mo.min_rent, 100))
        plt.show()

    def amoritization(self):
        fig = plt.figure()
        ama_data = np.array([[x, self.ama[x]] for x in range(len(self.ama))])
        value_data = np.array([[x, self.value_increase[x]] for x in range(len(self.value_increase))])
        x1, y1 = ama_data.T
        x2, y2 = value_data.T
        plt.plot(x1, y1, 'bo', linewidth=1, linestyle='solid', color='blue', markersize=0)
        plt.plot(x1, y2, 'r+', linewidth=1, linestyle='solid', color='red', markersize=0)
        plt.fill_between(x1, y2, y1, color='yellow')
        plt.xlim(0, len(self.ama)+20)
        plt.xticks(np.arange(min(x1), max(x1), 12))
        plt.ylim(0, int(self.value_increase[-1]*1.05))
        plt.title('amoritization-schedule')
        plt.xlabel('years')
        plt.ylabel('remaining-balance')
        plt.show()
