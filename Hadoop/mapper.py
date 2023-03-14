import sys 

for line in sys.stdin:
	line=line.strip()
	words=line.split(',')
	print(words[0], 1)

