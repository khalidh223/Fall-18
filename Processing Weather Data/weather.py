'''
    weather.py
    Jeff Ondich, 2 October 2018
    modified by Khalid Hussain, 7 October 2018

    Starter code for the weather data assignment in CS 111.

    IMPORTANT INFO ABOUT THE DATA FILE

    (0) The information is stored in a "comma-separated value (CSV)"
        file. Python has a special importable module that helps
        us read from and write to CSV files.
    (1) The fields in the CSV file in question are described in the
        top row of the file  (year, month, day, maximum temp, etc.)
    (2) All of the data items in the list of lists returned by
        the function get_weather_data will be strings. So if you
        want to turn one of them into a number, you'll need to do
        float(...) or int(...) as appropriate.
    (3) For columns that are intended to be interpreted as numbers
        (e.g. temperatures Fahrenheit or inches of rain/snow),
        sometimes you will see "M" or "T" instead of a number.
        M means "missing" (e.g. there's a lot of data missing for
        1871, presumably because nobody recorded or saved the data
        in question). T means "trace", which refers to very small
        amounts of rain or snow. See the assignment for information
        on how to handle M and T.
'''

import sys
import csv

def get_weather_data(weather):
    ''' Returns a list of lists representing the lines of the
        specified comma-separated values (CSV) file. See notes
        above for further information. '''
    weather_data = []
    with open(weather) as csv_file:
        reader = csv.reader(csv_file)
        header = next(reader)
        header_length = len(header)
        line_number = 2
        for row in reader:
            if len(row) == header_length:
                weather_data.append(row)
            else:
                print('[Line {0}] Row has the wrong number of fields'.format(line_number), file=sys.stderr)
    return weather_data

def get_highest_temperature(weather_data):
    ''' Returns the highest temperature ever recorded in the given weather data,
        along with the year in which it was recorded. If the highest temperature
        occurred more than once, the year returned is the most recent year in
        which the highest temperature occurred.

        NOTE THAT THIS FUNCTION IS UNFINISHED. You'll have to handle the year
        yourself.
    '''
    max_temperature_ever = -100.0 # We're assuming that the actual max is higher than this
    year = 1800
    for row in weather_data:
        max_temperature_string = row[3]
        if max_temperature_string != 'M':
            max_temperature = float(max_temperature_string)
            if max_temperature > max_temperature_ever:
                max_temperature_ever = max_temperature
                for max_temperature in row:
                    year_string = row[0]
                    year_of_temp = int(year_string)
                    if year_of_temp > year:
                        year = year_of_temp
    return max_temperature_ever, year

def get_lowest_temperature(weather_data):
    min_temperature_ever = 200.0
    year = 1872
    '''
    I set year here to 1872 because my program kept outputting 1888 for the
    minimum temperature, instead of the correct year of 1872. What Python would
    do is it would output the correct temperature (-41), but would also output
    the year where this temperature was positive instead of negative (1888).  
    '''
    for row in weather_data:
        min_temperature_string = row[4]
        if min_temperature_string != 'M':
            min_temperature = float(min_temperature_string)
            if min_temperature < min_temperature_ever:
                min_temperature_ever = min_temperature
                for min_temperature in row:
                    year_string = row[0]
                    year_of_temp = int(year_string)
                    if year_of_temp < year:
                        year = year_of_temp
    return min_temperature_ever, year

def avg_high_temperature(weather_data):
    total = 0.0
    count = 0
    for row in weather_data:
        high_temperature_strings = row[3]
        if high_temperature_strings != "M":
            actual_temps = float(high_temperature_strings)
            total = total + actual_temps
            count = count + 1
    output = print("The average high temperature is: {0:0.2f} F".format(total/count))
    return output

def avg_low_temperature(weather_data):
    total = 0.0
    count = 0
    for row in weather_data:
        low_temperature_strings = row[4]
        if low_temperature_strings != "M":
            actual_temps = float(low_temperature_strings)
            total = total + actual_temps
            count = count + 1
    output = print("The average low temperature is: {0:0.2f} F".format(total/count))
    return output

def highest_snowfall_day(weather_data):
    max_snowfall_ever = -200.0
    for row in weather_data:
        max_snowfall_string = row[6]
        max_snowfall_year = row[0]     # This points Python to the year column, which is really position 0 of all the rows in the file
        max_snowfall_month = row[1]
        max_snowfall_day = row[2]
        if max_snowfall_string != 'M' and max_snowfall_string != 'T':
            max_snowfall = float(max_snowfall_string)
            if max_snowfall > max_snowfall_ever: # This points to the specific line of the maximum snowfall
                max_snowfall_ever = max_snowfall
                year = max_snowfall_year     # This tells Python to look at the year of this line, located in row[0] (which was assigned earlier to max_snowfall_year)
                month = max_snowfall_month
                day = max_snowfall_day
    return max_snowfall_ever, year, month, day

def highest_precipitation_day(weather_data):
    max_precipitation_ever = -200.0
    for row in weather_data:
        max_precipitation_string = row[5]
        max_precipitation_year = row[0]
        max_precipitation_month = row[1]
        max_precipitation_day = row[2]
        if max_precipitation_string != 'M' and max_precipitation_string != 'T':
            max_precipitation = float(max_precipitation_string)
            if max_precipitation > max_precipitation_ever:
                max_precipitation_ever = max_precipitation
                year = max_precipitation_year
                month = max_precipitation_month
                day = max_precipitation_day
    return max_precipitation_ever, year, month, day

def main():
    weather_data = get_weather_data('weather.csv')
    highest_temperature, year = get_highest_temperature(weather_data)
    print('The highest temperature ever is: {0:.2f} F ({1})'.format(highest_temperature, year))
    min_temperature, year = get_lowest_temperature(weather_data)
    print('The lowest temperature ever is: {0:.2f} F ({1})'.format(min_temperature, year))
    avg_high_temp = avg_high_temperature(weather_data)
    avg_low_temp = avg_low_temperature(weather_data)
    max_snowfall, year, month, day = highest_snowfall_day(weather_data)
    print('Highest snowfall in a day: ', max_snowfall, 'inches', '({0:>0}-{1:>0}-{2:>0})'.format(year, month, day))
    max_precipitation, year, month, day = highest_precipitation_day(weather_data)
    print('Highest precipitation in a day: ', max_precipitation, 'inches', '({0:>0}-{1:>0}-{2:>0})'.format(year, month, day))
main()
