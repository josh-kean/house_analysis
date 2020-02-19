from graphs import Graphs
from prop import House, FinancialObject
from database import Table
from reports import Reports
import argparse
import csv
import os
import pickle

#parser=argparse.ArgumentParser(description="make $$$ with real estate")
#parser.add_argument('--add_homes', 


#want a function to import houses and enter all data into database
#function to run through each sql row and input minimum required rent
#prune all rents that are too low for profit
#order based on difference between min rent and actual rent
#create presentation documents

#function to open the csv table of house values
def populate_database(file_name):
    table = Table()
    houses = open(file_name, 'r')
    houses = csv.reader(houses)
    houses = list(houses)
    for house in houses:
        table.add_home(house)


def actuals(house, appreciate=1.05):
    if appreciate !=1.05:
        h = House(house[0], house[1], house[2], house[3], appreciate)
    else:
        h = House(house[0], house[1], house[2], house[3])
    fo = FinancialObject(h)
    fo.down_unfinanced()
    return fo.min_rent, fo.coc

def determine_actuals():
    #go through every item in homes table and iterate as home
    table = Table()
    homes = table.get_table()
    for home in homes:
        rent, coc = actuals(home)
        table.add_min_rent(rent, home[3])
        table.add_cash_on_cash(coc, home[3])

def create_folder(name): #input address as name
    #if folder exists, do nothing, else, create new folder
    folder_name = os.path.join('homes', name)
    if os.path.exists(folder_name) != True:
        os.makedirs(os.path.join(folder_name))
    if os.path.exists(os.path.join(folder_name, 'graphs')) != True:
        os.makedirs(os.path.join(folder_name, 'graphs'))

def create_graphs(name, fo):
    #create and save graphs to graphs folder
    folder_name = os.path.join('homes', name)
    folder = os.path.join(folder_name, 'graphs')
    graphs = Graphs(fo)
    #graphs.price_breakdown(folder)
    graphs.amoritization(folder, fo)

def pickle_home(name, financial_object):
    folder_name = os.path.join('homes', name)
    pkl = os.path.join(folder_name, f'{name}.pkl')
    F = open(pkl, 'wb')
    pickle.dump(financial_object, F)
    F.close()

def save_homes():
    table = Table()
    homes = table.get_table()
    for home in homes:
        house = House(home[0], home[1], home[2], home[3])
        fo = FinancialObject(house)
        create_folder(home[3])
        pickle_home(home[3], fo)
        create_graphs(home[3], fo)


def create_reports():
    table = Table()
    homes = table.get_table()
    for home in homes:
        house = House(home[0], home[1], home[2], home[3])
        fo = FinancialObject(house)
        report = Reports()
        report.create_report(home, fo)
