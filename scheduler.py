import pandas as pd
from itertools import compress

def get_day(i, daysi, daysname):
	""" return the day of week, given a column index """
	k = 0
	for ind, name in zip(daysi[::-1], daysname[::-1]):
		if i >= ind:
			return name

df = pd.read_excel("Doodle_final.xls",skiprows=4)

# extract time-related labels and then strip them from the dataframe
daysi = list(compress(range(len(df.columns)),[not x.startswith('U') for x in df.columns]))
daysname = list(compress(df.columns,[not x.startswith('U') for x in df.columns]))
times = df.iloc[0]
df = df.iloc[1:-1]

# give the columns nice, numeric names
df.columns = range(len(df.columns))
df = df.fillna(0).replace('OK',1)


best = -1
# this gives me all best choices so that I can inspect and add human judgement to the result
good_times = []

for i in range(1, df.shape[1]):
	for j in range(i+1, df.shape[1]):

		# this is imo the most import constraint
		if get_day(i,daysi,daysname) == get_day(j,daysi,daysname):
			continue

		total = sum([max(x,y) for x,y in zip(df[i],df[j])])
		if total > best:
			good_times = [(i,j)]
			best = total
		elif total == best:
			good_times.append((i,j))

print ("# students: %d" % best)
for i,j in good_times:
	day1 = get_day(i, daysi, daysname)
	day2 = get_day(j, daysi, daysname)
	print (day1 + ": " + times[i] + " " + day2 + ": " + times[j])

