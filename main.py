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


def actuals(home, appreciate=1.05):
    if appreciate !=1.05:
        h = House(home[0], home[2], home[3], home[4], home[6], appreciate)
    else:
        h = House(home[0], home[2], home[3], home[4], home[6])
    fo = FinancialObject(h)
    fo.down_unfinanced()
    return fo.min_rent, fo.coc

def determine_actuals():
    #go through every item in homes table and iterate as home
    table = Table()
    homes = table.get_table()
    for home in homes:
        rent, coc = actuals(home)
        table.add_min_rent(rent, home[4])
        table.add_cash_on_cash(coc, home[4])

def create_folder(name): #input address as name
    #if folder exists, do nothing, else, create new folder
    folder_name = os.path.join('homes', name)
    if os.path.exists('homes') != True:
        os.makedirs('homes')
    if os.path.exists(folder_name) != True:
        os.makedirs(os.path.join(folder_name))
    if os.path.exists(os.path.join(folder_name, 'graphs')) != True:
        os.makedirs(os.path.join(folder_name, 'graphs'))

def create_graphs(name, fo, test=False):
    #create and save graphs to graphs folder
    check = lambda x: 'test-' if test else ''
    folder_name = os.path.join(f'{check(test)}homes', name)
    folder = os.path.join(folder_name, 'graphs')
    graphs = Graphs()
    fo = fo
    graphs.amoritization(folder, fo)
    graphs.expense_breakdown(folder, fo)
    graphs.various_rates(folder, fo)

def pickle_home(name, financial_object, test=False):
    check = lambda x: 'test-' if test else ''
    folder_name = os.path.join('homes', name)
    pkl = os.path.join(folder_name, f'{name}.pkl')
    F = open(pkl, 'wb')
    pickle.dump(financial_object, F)
    F.close()

def save_homes(test=False):
    table = Table()
    homes = table.get_table()
    for home in homes: #address is item 4
        house = House(home[0], home[2], home[3], home[4], home[6])
        fo = FinancialObject(house)
        create_folder(home[4], test)
        pickle_home(home[4], fo, test)
        create_graphs(home[4], fo, test)

def sorted_table():
    table = Table()
    table.filter_by_coc()
    table.filter_by_price()
    homes = table.sort_by_coc()
    csv_file = open(os.path.join('tables', 'houses.csv'), 'w')
    csv_writet = csv.writer(csv_file)
    for home in homes:
        csv_writer.writerow(home)


def create_reports():
    table = Table()
    homes = table.get_table()
    for home in homes:
        house = House(home[0], home[2], home[3], home[4], home[6])
        fo = FinancialObject(house)
        report = Reports(house, fo)
        report.create_report()


def city_table(city):
    table = Table()
    table.filter_by_coc()
    table.filter_by_price()
    homes = table.filter_by_city(city)
    csv_file = open(f'{city}_sorted.csv','w')
    csv_writer = csv.writer(csv_file)
    for home in homes:
        csv_writer.writerow(home)

def filter_main(table_name, city=None, coc=None, finance=None):
    table = Table()
    homes = table.filter_all(city=city, coc=coc, finance=finance)
    cityName = lambda x: f'{x}' if x else ''
    cocName = lambda x: f'coc_{x}' if x else ''
    financeName = lambda x: f'
    csv_file = open(f'{city}



def test_new_features():
    #this only calculates info for first house in list
    table = Table()
    home = table.get_table()[4]
    house = House(home[0], home[2], home[3], home[4], home[6])
    fo = FinancialObject(house)
    title = f'test-{home[4]}'
    create_folder(title)
    create_graphs(title, fo)
    report = Reports(house, fo)
    report.create_report(True)
