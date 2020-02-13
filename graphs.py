import numpy as np
import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt

plt.style.use('seaborn-whitegrid')

class Graphs:
    def __init__(self, ama, value_increase, mortgage, house, dp_payoff=None):
        self.ama = ama
        self.value_increase = value_increase
        self.mortgage = mortgage
        self.dp_payoff = dp_payoff
        self.house = house

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

    def monthly_return(self, rent, mortgage, tax, insurance, excess_costs):
        pass
