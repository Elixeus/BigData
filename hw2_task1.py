import pandas as pd
import csv
import sys

'''
author: Xia Wang
'''

def count_year(reader):
	for row in reader:
		if row['usertype'] == 'Subscriber':
			year = row['birth_year']
			yield year


if __name__ == '__main__':
	# deal with exceptions
	if len(sys.argv)<2:
		sys.stderr.write('USAGE: python %s <INPUT_CSV>\n' % sys.argv[0])
		sys.exit(1)
	# first create an generator
	with open(sys.argv[1], 'r') as fi:
		reader = csv.DictReader(fi)
		g = count_year(reader)

		# use dictionary to count the number of appearance for each year of birth
		years = {}
		for byear in g:
			years[byear] = years.get(byear, 0) + 1

		# create a dataframe with the dictionary
		df = pd.DataFrame.from_dict(years, orient='index')
		# sort the dataframe
		df.sort_index(inplace = True)
		# get rid of the data without birth year
		# try:
		# 	df.drop('', axis=0, inplace = True)
		# except ValueError:
		# 	print 'There is no value whose year is not specified.'
		# calculate the median year
		total = df[0].sum()
		CumSum = 0
		med = None
		for k, v in sorted(years.iteritems()):
			CumSum += v
			if CumSum >= total/2.0:
				med = k
				break
		# convert year to age
		print '%d' %(2016 - int(med))
		#print 'The median age of Subscribers is: %d' %(2016 - int(med))