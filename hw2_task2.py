import csv
import sys
import dateutil
import pandas as pd

##################################################
##################################################
def first_ride(reader):
    '''
    Please change this function for task 2 of HW2.
    Currently, it only output the first record.
    '''
    first_day = None
    for row in reader:
        day1 = dateutil.parser.parse(row['starttime']).day
        if day1 != first_day:
            first_day = day1
            yield row
##################################################
##################################################

if __name__=='__main__':
    if len(sys.argv)<2:
        sys.stderr.write('USAGE: python %s <INPUT_CSV>\n' % sys.argv[0])
        sys.exit(1)
    
    with open(sys.argv[1], 'r') as fi:
        reader = csv.DictReader(fi)
        for row in first_ride(reader):
            print ','.join(map(row.get, reader.fieldnames))
