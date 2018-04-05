#!/usr/bin/env python3

import sys
from datetime import datetime
from cmc_mongo import get

coin = sys.argv[1].lower()
start_date = ''
end_date = ''
if len(sys.argv) > 2:
    start_date = sys.argv[2]
    
    if len(sys.argv) > 3:
        end_date = sys.argv[3]

date_formats = [ '%Y-%m-%d', '%Y-%m', '%Y' ]
def report_malformed_date(date):
    print('Could not parse date: "' + date + '"')
    print('Use the format YYYY-MM-DD, YYYY-MM, or YYYY')

def format_date(date_str):
    formatted = ''
    for df in date_formats:
        try:
            return datetime.strptime(date_str, df)
        except Exception as e:
            #print(e)
            pass

    report_malformed_date(date_str)
    return ''

start_date_formatted = '' 
end_date_formatted = ''
if start_date:
    start_date_formatted = format_date(start_date)

if end_date:
    end_date_formatted = format_date(end_date)

print('Gathering data for {} between {} and {}'.format(coin, start_date_formatted, end_date_formatted))
result = get(coin, start_date_formatted, end_date_formatted)

