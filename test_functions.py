import pytest
from main import House, FinancialObject

house = House(100_000, 3, '123 sesame street')

def test_20_unfinanced():
    fo = FinancialObject(house)
    fo.down_unfinanced()
    assert fo.down_payment == 20_000
    assert fo.loan_amount == 80_000
    assert int(fo.mortgage) in range(428, 430)
    assert int(fo.amoritization[0]) in range(79_902, 79_904)
    assert int(fo.amoritization[-1]) == 0
    assert fo.payments[0] == fo.mortgage


def test_0_unfinanced():
    fo = FinancialObject(house)
    fo.down_unfinanced(0)
    assert fo.down_payment == 0
    assert fo.loan_amount == 100_000
    assert int(fo.mortgage) in range(536, 538)
    assert int(fo.loan_insurance_payment) == int(100_000*.005/12)
    assert fo.payments[0] == fo.mortgage + fo.loan_insurance_payment
    assert fo.payments[-1] == fo.mortgage


def test_20_financed():
    #test at 15% financing and 5 year payback period for 20% down
    fo = FinancialObject(house)
    fo.down_financed()
    assert fo.down_payment == 20_000
    assert fo.loan_amount == 80_000
    assert int(fo.mortgage) in range(428, 430)
    assert fo.payments[0] == fo.mortgage+fo.finance_payment
    assert fo.amoritization[-1] == 0
    assert int(fo.amoritization[0]) in range(99_677, 99_679)
