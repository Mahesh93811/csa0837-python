import sys


word_count = 0


for line in sys.stdin:
    
    words = line.split()
    
    word_count += len(words)


print(word_count)