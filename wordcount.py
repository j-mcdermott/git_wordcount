import sys
from collections import Counter

with open(sys.argv[1], 'r') as file:
    lines = []
    for line in file:
        line = line.strip()
        line = line.lower()
        line = line.replace(",", "")
        line = line.replace("!", "")
        lines.append(line)

line1 = lines[0]
line2 = lines[1]
line3 = lines[2]
line4 = lines[3]

words1 = line1.split(" ")
words2 = line2.split(" ")
words3 = line3.split(" ")
words4 = line4.split(" ")

counts = Counter(words1)
counts2 = Counter(words2)
counts3 = Counter(words3)
counts4 = Counter(words4)

userinput = int(sys.argv[2])
dupwords = ""
dupwords2 = ""
dupwords3 = ""
dupwords4 = ""
dupcount = 0
dupcount2 = 0
dupcount3 = 0
dupcount4 = 0

if userinput == 1:
    print("LINE 1", "\n", "Total words: ", int(len(words1)), "\n")
    print("LINE 2", "\n", "Total words: ", int(len(words2)), "\n")
    print("LINE 3", "\n", "Total words: ", int(len(words3)), "\n")
    print("LINE 4", "\n", "Total words: ", int(len(words4)), "\n")
elif userinput == 2:
    dupwords = [key for key, value in counts.items() if value >= 2]
    dupwords2 = [key for key, value in counts2.items() if value >= 2]
    dupwords3 = [key for key, value in counts3.items() if value >= 2]
    dupwords4 = [key for key, value in counts4.items() if value >= 2]
    dupcount = int(len(dupwords))
    dupcount2 = int(len(dupwords2))
    dupcount3 = int(len(dupwords3))
    dupcount4 = int(len(dupwords4))
    print("LINE 1", "\n" "The duplicate words are: ", dupwords, "\n", "Total duplicates: ", dupcount, "\n")
    print("LINE 2", "\n" "The duplicate words are: ", dupwords2, "\n", "Total duplicates: ", dupcount2, "\n")
    print("LINE 3", "\n" "The duplicate words are: ", dupwords3, "\n", "Total duplicates: ", dupcount3, "\n")
    print("LINE 4", "\n" "The duplicate words are: ", dupwords4, "\n", "Total duplicates: ", dupcount4, "\n")
elif userinput == 3:
    dupwords = [key for key, value in counts.items() if value >= 3]
    dupwords2 = [key for key, value in counts2.items() if value >= 3]
    dupwords3 = [key for key, value in counts3.items() if value >= 3]
    dupwords4 = [key for key, value in counts4.items() if value >= 3]
    dupcount = int(len(dupwords))
    dupcount2 = int(len(dupwords2))
    dupcount3 = int(len(dupwords3))
    dupcount4 = int(len(dupwords4))
    print("LINE 1", "\n" "The triplicate words are: ", dupwords, "\n", "Total triplicate: ", dupcount, "\n")
    print("LINE 2", "\n" "The triplicate words are: ", dupwords2, "\n", "Total triplicate: ", dupcount2, "\n")
    print("LINE 3", "\n" "The triplicate words are: ", dupwords3, "\n", "Total triplicate: ", dupcount3, "\n")
    print("LINE 4", "\n" "The triplicate words are: ", dupwords4, "\n", "Total triplicate: ", dupcount4, "\n")
else:
    print("Try a number between 1 and 3... ")

