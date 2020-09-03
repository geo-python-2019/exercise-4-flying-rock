""""Script file to store temperature functions

Contains two functions for converting and classifying temperatures

Author: 
    Jorjito the magnificent
"""

"""Converts farenheit temperatures into celsius

Parameters:
    requires temperature values in fahrenheit
    
Returns:
    temperature value in celsius   
"""
def fahr_to_celsius(temp_fahrenheit): # code takes a single variable, can be a float or an integer
    converted_temp = (temp_fahrenheit - 32)/1.8
    return converted_temp # returns a number 


""" Classifies temperatures into one of four values

Takes temperature in celsius as its only parameter

Returns an integer based on the value of the temperature input
"""
def temp_classifier(temp_celsius): # define your functions name and input parameter
    # set the ranges of values which specify how they are classified
    if temp_celsius < -2: 
        category = 0 
    elif temp_celsius >= -2 and temp_celsius < 2: # cannot use the '&' symbol for some reason
        category = 1
    elif temp_celsius >= 2 and temp_celsius < 15:
        category = 2
    elif temp_celsius >= 15:
        category = 3
    return category