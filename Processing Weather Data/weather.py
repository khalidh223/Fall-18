'''
    weather.py
    Jeff Ondich, 2 October 2018

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

def get_weather_data(csv_file_name):
    ''' Returns a list of lists representing the lines of the
        specified comma-separated values (CSV) file. See notes
        above for further information. '''
    weather_data = []
    with open(csv_file_name) as csv_file:
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
    return max_temperature_ever, year

def main():
    weather_data = get_weather_data('weather.csv')
    highest_temperature, year = get_highest_temperature(weather_data)
    print('The highest temperature ever: {0:.2f} ({1})'.format(highest_temperature, year))

main()

