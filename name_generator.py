# Make a dumb hair product name generator 

import urllib.request
import random

word_file = "words.txt"
words = open(word_file).read().splitlines()
countries_file = "countries.txt"
countries = open(countries_file).read().splitlines()
adjectives_file = "adjectives.txt"
adjectives = str(open(adjectives_file).read()).split(u'Â\xa0')
adjectives = [item.strip() for item in adjectives]
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

body_parts_file = "anatomy.txt"
body_parts = open(body_parts_file).read().splitlines()


# word_url = "http://svnweb.freebsd.org/csrg/share/dict/words?view=co&content-type=text/plain"
    # response = urllib.request.urlopen(word_url)
    # long_txt = response.read().decode()
    # words = long_txt.splitlines()

    # print(response)
    # print(long_txt)
    # print(len(words))

firstnames = ('Baby Oil', 'Bad News', 'Big Burps', "Bill 'Beenie-Weenie'",
     "Bob 'Stinkbug'", 'Bowel Noises', 'Boxelder', 'Bruiser', "Bud 'Lite' ",
     'Butterbean', 'Buttermilk', 'Buttocks', 'Chad', 'Chesterfield',
     'Chewy', 'Chigger', 'Cinnabuns', 'Cleet', 'Cornbread', 'Crab Meat',
     'Crapps', 'Dark Skies', 'Dennis Clawhammer', 'Dicman', 'Elphonso', 'Engelbert',
     'Fancypants', 'Figgs', 'Foncy', 'Gootsy', 'Greasy Jim', 'Huckleberry',
     'Huggy', 'Ignatious', 'Jimbo', "Joe 'Pottin Soil'", 'Johnny',
     'Lemongrass', 'Lil Debil', 'Longbranch', '"Lunch Money"', 'Mergatroid',
     '"Mr Peabody"','Mr Bobson "Babies"', 'Oil-Can', 'Oinks', 'Old Scratch', 'Ovaltine',
     'Pennywhistle', 'Pitchfork Ben', 'Potato Bug', 'Pushmeet',
     'Rock Candy', 'Schlomo', 'Scratchensniff', 'Scut',
     "Sid 'The Squirts'", 'Skidmark', 'Slaps', 'Snakes', 'Snoobs',
     'Snorki', 'Soupcan Sam', 'Spitzitout', 'Squids', 'Stinky',
     'Storyboard', 'Sweet Tea', 'TeeTee', 'Wheezy Joe',
     "Winston 'Jazz Hands'", 'Worms')

lastnames = ('Appleyard', 'Bigmeat', 'Bloominshine', 'Boogerbottom',
    'Breedslovetrout', 'Butterbaugh', 'Cheeseman', 'Clovenhoof', 'Clutterbuck',
    'Cocktoasten', 'Endicott', 'Fewhairs', 'Gooberdapple', 'Goodensmith',
    'Goodpasture', 'Guster', 'Henderson', 'Hooperbag', 'Hoosenater',
    'Hootkins', 'Humperdink', 'Jefferson', 'Jenkins', 'Jingley-Schmidt', 'Johnson',
    'Kingfish', 'Listenbee', "M'Bembo", 'McFadden', 'Moonshine', 'Nettles',
    'Noseworthy', 'Olivetti', 'Outerbridge', 'Overpeck', 'Overturf',
    'Oxhandler', 'Pealike', 'Pennywhistle', 'Peterson', 'Pieplow',
    'Pinkerton', 'Porkins', 'Putney', 'Quakenbush', 'Rainwater',
    'Rosenthal', 'Rubbins', 'Sackrider', 'Snuggleshine', 'Splern',
    'Stevens', 'Stroganoff', 'Sugar-Gold', 'Swackhamer', 'Tippins',
    'Turnipseed', 'Vinaigrette', 'Walkingstick', 'Wallbanger', 'Weewax',
    'Weiners', 'Whipkey', 'Wigglesworth', 'Wimplesnatch', 'Winterkorn',
    'Woolysocks')

standard_product_names = ['Mousse', 'Gel', 'Pomade', 'Clay', 'Wax', 'Paste', 'Cream', 'Putty', 'Hair Spray']
other_product_names = ['Olive Oil', 'Cocoa Butter', 'Mixed Herb Butter', 'Lard', 'Peanut Oil', 'Chicken Fat', 'Mayonnaise', 'Lotion', 'Gunk', '']
#herb butter type thing might be fun
#how much hold and how much shine

effects = ['Hair', 'Hold', 'Shine', 'Gloss', 'Texture', 'Look', 'Appearance', 'Scalp', 'Dandruff', 'Follicles', 'Split Ends', 'Sheen', 'Musk', 'Smell']

upper_words = [word for word in words if word[0].isupper()]
name_words  = [word for word in upper_words if not word.isupper()]


"""
Options: 
- [Very Funny Name]'s [regular hair product]
- [Normal Name]'s [bad hair product]
- New! [regular hair product] for [weird effect] 
- special combo of all the weirds
- [] + [country]'s 'superlative'!
"""


def main():
    flag = True
    print("Welcome to the Stupid Hair Product Name Generator v0.2!")
    print("Looking for a new hair product? You should use: ")
    while flag == True:
        switch = random.randint(1,6)
        one_name = ' '.join([name_words[random.randint(0, len(name_words))] for i in range(2)])
        one_bad_name = random.choice(firstnames) + " " + random.choice(lastnames)
        
        if switch == 1:
            print(one_bad_name+ "'s " + random.choice(standard_product_names))

        if switch == 2:
            print(one_name+ "'s " + random.choice(other_product_names))

        if switch == 3:
            print("New! " + random.choice(standard_product_names+other_product_names) + " for " + random.choice(comparatives).capitalize()+ " " +random.choice(effects))

        if switch == 4:
            print('"'+ one_name +" " + random.choice(standard_product_names) + '"' + ": " + random.choice(countries)+"'s " + random.choice(superlatives).capitalize() )

        if switch == 5:
            print(one_bad_name + "'s " + random.choice(other_product_names))
        
        if switch == 6:
            print(one_name+ "'s " + random.choice(other_product_names) + ". Side Effects may include: " + random.choice(comparatives).capitalize() +" " +random.choice(body_parts).capitalize())
        
        while True:
            print("\n")
            repeat = str(input("Would you like another recommendation? y/n? "))
            if repeat == 'y':
                break
            elif repeat == 'n':
                print("Come again soon!")
                flag = False
                break
            else:
                print("Please enter either 'y' or 'n'")

print(main())
    
