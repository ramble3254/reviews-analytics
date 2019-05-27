data = []
count = 0
with open('reviews.txt', 'r') as f:
	for line in f:
		data.append(line)
		count += 1
		if count % 100000 == 	0:
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
good = []
for g in data:
	if 'good' in g:
		good.append(g)
print('一共有', len(good), '筆留言提到good')

#文字計數
word_count = {}
for d in data:
	words = d.split()
	for word in words:
		if word in word_count:
			word_count[word] += 1
		else:
			word_count[word] = 1

for word in word_count:
	if word_count[word] > 1000000:
		print(word, word_count[word])
while True:
	word = input('請問你想查什麼字: ')
	if word == 'q':
		print('感謝使用')
		break
	if word in word_count:
		print(word, '這個字出現了', word_count[word], '次')
	else:
		print('這個字沒有出現過')



#good = [g forgd in good if 'good' in g] 快寫,同上面4行
#good = ['good in g' forgd in good] 則會選出true or false