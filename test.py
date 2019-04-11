# test = input("Try this")
# if test == 'test':
#     print("True")

adjectives_file = "adjectives.txt"
adjectives = str(open(adjectives_file).read()).split(" ")
print(adjectives)
adjectives = [item for item in adjectives if item.isalpha()]

print(adjectives)