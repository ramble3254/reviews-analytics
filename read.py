data = []
count = 0
with open('reviews.txt', 'r') as f:
	for line in f:
		data.append(line)
		count += 1
		if count % 100000 ==0:
			print(len(data))
print('讀取完畢,共有:', len(data), '筆資料')
sum_len = 0
for d in data:
	sum_len += len(d)
print('留言平均長度為', sum_len/len(data))
new = []
for a in data:
	if len(a) < 100:
		new.append(a)
print ('共有', len(new),	 '筆留言長度小於100')
print(new[0])
