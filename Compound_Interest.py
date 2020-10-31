import math


def compound_interest_calc(starting_amt, years, rate_as_decimal, compound_times_per_year):
    """Calculates Compound Interest

    Args:
      starting_amt (float): Starting amount
      years (int): the time
      rate_as_decimal (float): the interest rate written as a decimal (0..1)
      compound_times_per_year (int): how many times per year we are compounding interest

    Returns:
      Amount of money after compounding interest

    Raises:
      Exception: If starting amount is negative
      Exception: If years is less than 1
      Exception: If compound frequency is 0 or less
      Exception: If interest rate is less than 0
    """
    years = math.floor(years)
    if starting_amt < 0:
        raise Exception("Invalid starting amount: %s" % starting_amt)
    if compound_times_per_year <= 0:
        raise Exception("Invalid compound frequency: %s" % compound_times_per_year)
    if rate_as_decimal < 0:
        raise Exception("Invalid interest rate: %s" % rate_as_decimal)
    if years < 1:
        raise Exception("Years to grow must be 1 or more. Invalid: %s" % years)
    end_money = starting_amt * (1 + rate_as_decimal/compound_times_per_year)**(compound_times_per_year*years)
    return round(end_money, 2)
