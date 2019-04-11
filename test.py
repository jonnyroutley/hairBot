# coding=utf-8
# test = input("Try this")
# if test == 'test':
#     print("True")

adjectives_file = "adjectives.txt"
adjectives = str(open(adjectives_file).read()).split('\n')
comparatives = []
superlatives = []
counter1 = 1
counter2 = 2
for i in range(len(adjectives)):
    if counter1 % 3 == 0:
        superlatives.append(adjectives[i])
    if counter2 % 3 == 0:
        comparatives.append(adjectives[i])
    counter1 += 1
    counter2 += 1

print(comparatives, superlatives)