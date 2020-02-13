import pytest
from main import House, Mortgage


def test_20_down():
    house = House(100_000, 1000, 3, '132 bridge street')
    mortgage = Mortgage(house)
    mortgage.mortgage(0.0455)
    assert int(mortgage.monthly_payment) in range(407, 409)


def test_0_down():
    house = House(100_000, 1000, 3, '132 bridge street')
    mortgage = Mortgage(house, 0)
    mortgage.mortgage(0.0455)
    assert int(mortgage.monthly_payment) in range(509, 511)

def test_loan_payoff_20_down():
    house = House(100_000, 1000, 3, '132 bridge street')
    mortgage = Mortgage(house)
    mortgage.mortgage(0.0455)
    mortgage.loan_payment_schedule()
    payments = mortgage.pay_schedule
    assert payments[0] in range(79_894, 79_896)
    assert payments[1] in range(79_790, 79_792)
    assert payments[-2] in range(405, 407)
    assert payments[-1] in range(-1, 1)

def test_cash_on_cash():
    #cash on cash is the annual pre tax income divided by the initial investment
    #this test is ignoring extra fees, such as insurance
    house = House(100_000, 1000, 3, '132 bridge street')
    mortgage = Mortgage(house)
    mortgage.mortgage(0.0455)
    mortgage.cash_on_cash()
    assert mortgage.coc == .355


def test_coc_qualify():
    house = House(100_000, 1000, 3, '132 bridge street')
    mortgage = Mortgage(house)
    mortgage.mortgage(0.0455)
    mortgage.cash_on_cash()
    assert mortgage.qualify_coc()

def test_home_value_increase():
    #assuming 5.5% average appreciation over a 10 year period
    #0 is the zeroth year, so nothing exciting happens until year 1
    house = House(100_000, 1000, 3, '132 bridge street')
    mortgage = Mortgage(house)
    mortgage.mortgage(0.0455)
    mortgage.future_value()
    assert int(mortgage.future_growth[0]) == 100_000
    assert int(mortgage.future_growth[12]) == 104_550
    assert int(mortgage.future_growth[60]) == 124_916

