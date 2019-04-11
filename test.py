# test = input("Try this")
# if test == 'test':
#     print("True")

adjectives_file = "adjectives.txt"
adjectives = str(open(adjectives_file).read()).split(u'Â\xa0')

print(adjectives)