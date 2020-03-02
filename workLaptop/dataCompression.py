def freqTable(text):
	wordDic = {}
	for word in text:
		if word in wordDic:
			wordDic[word] = wordDic[word] + 1
		else:
			wordDic[word] = 1 
	return wordDic

text = f"Hello world"
wordDic = freqTable(text)
for key, value in reversed(sorted(wordDic.items(), key = lambda item: item[1])):
	print(f"'{key}': {value}", end = ";    ")