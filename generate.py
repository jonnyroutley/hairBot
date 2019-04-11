# Make a dumb hair product name generator 
# coding=utf-8
import random

word_file = "words.txt"
words = open(word_file).read().splitlines()
countries_file = "countries.txt"
countries = open(countries_file).read().splitlines()
adjectives_file = "adjectives.txt"
adjectives = str(open(adjectives_file).read()).split(" ")
adjectives = [item for item in adjectives if item.isalpha()]
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

# print(words, countries, adjectives, comparatives, superlatives, body_parts)

firstnames = ('Baby Oil', 'Bad News', 'Big Bird', 'Big Burps', "Bill 'Beenie-Weenie'",
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

standard_product_names = ['Mousse', 'Gel', 'Pomade', 'Clay', 'Wax', 'Paste', 'Cream', 'Putty', 'Hair Spray', 'Shampoo', 'Conditioner']
other_product_names = ['Olive Oil', 'Cocoa Butter', 'Mixed Herb Butter', 'Lard', 'Peanut Oil', 'Chicken Fat', 'Mayonnaise', 'Lotion', 'Gunk', 'Special Sauce']


effects = ['Hair', 'Hold', 'Shine', 'Gloss', 'Texture', 'Look', 'Appearance', 'Scalp', 'Dandruff', 'Follicles', 'Split Ends', 'Sheen', 'Musk', 'Smell']

upper_words = [word for word in words if word[0].isupper()]
name_words  = [word for word in upper_words if not word.isupper()]


def main():
    flag = True
    while flag == True:
        switch = random.randint(1,6)
        one_name = ' '.join([name_words[random.randint(0, len(name_words))] for i in range(2)])
        one_bad_name = random.choice(firstnames) + " " + random.choice(lastnames)
        
        if switch == 1:
            return(one_bad_name+ "'s " + random.choice(standard_product_names))

        if switch == 2:
            return(one_name+ "'s " + random.choice(other_product_names))

        if switch == 3:
            return("New Hair Product Alert! " + random.choice(standard_product_names+other_product_names) + " for " + random.choice(comparatives).capitalize()+ " " +random.choice(effects))

        if switch == 4:
            return('"'+ one_name +" " + random.choice(standard_product_names) + '"' + ": " + random.choice(countries)+"'s " + random.choice(superlatives).capitalize() )

        if switch == 5:
            return(one_bad_name + "'s " + random.choice(other_product_names))
        
        if switch == 6:
            return(one_name+ "'s " + random.choice(other_product_names) + ". Side Effects may include: " + random.choice(comparatives).capitalize() +" " +random.choice(body_parts).capitalize())
        
for i in range(20):
    print(main())
    
