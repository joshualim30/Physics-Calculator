# formatting.py - Formating Functions File
# By: Joshua Lim
# Date: 10/08/2022
# Version 0 Optimized

# imports
import decimal

# function to format a number to a certain number of decimal places
def formatDecimal(float, decimalPlaces): # ".0000" is 4 decimal places
    return decimal.Decimal(float).quantize(decimal.Decimal(decimalPlaces), rounding=decimal.ROUND_HALF_UP)
