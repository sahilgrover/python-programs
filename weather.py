import math, re
weather = []
with open('w_data.dat') as f:
	for line in f:
		L = line.split()
		if len(L) > 0 and L[0].isnumeric():
			weather.append(L)
num = 0
mindiff = math.inf
for (ind, day) in enumerate(weather):
	# print(day)
	maxtemp = int(re.sub("[^0-9]", "", day[1]))
	mintemp = int(re.sub("[^0-9]", "", day[2]))
	if(maxtemp -mintemp < mindiff):
		num = ind
		mindiff = maxtemp - mintemp

print("Minimum temperaturee difference is on day " + weather[num][0] + " with a Max of " + weather[num][1] + " and a Min of " + weather[num][2])