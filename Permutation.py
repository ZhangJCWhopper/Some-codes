#problems: list copy
globalPool = list()
def place(candids, result):
	if len(candids) == 1:
		final = result + candids
		globalPool.append(final)
		return
	else:
		for i in range(len(candids)):
			temp = result[:]
			temp.append(candids[i])
			newCandids = list()
			newCandids = candids[0:i] + candids[i+1:]
			#print temp
			#print newCandids
			place(newCandids, temp)

pool = [1,2,3,4,5]
start = []
for i in range(len(pool)):
	first = pool[i]
	for j in range(i+1, len(pool)):
		second = pool[j]
		newPool = pool[0:i] + pool[i+1:j] + pool[j+1:]
		newPool.append([first, second])
		place(newPool, start)

finalPool = list()
for li in globalPool:
	suit = 1
	
	if type(li[2]) == list:
		if li[2][0] == 2 or li[2][0] == 3 or li[2][1] == 2 or li[2][1] == 3:
			suit = 0
	else:
		if li[2] == 2 or li[2] == 3:
			suit = 0
	for one in li:
		if one == [4,5]:
			suit = 0
	if suit == 1:
		finalPool.append(li)

print len(finalPool)
print finalPool
