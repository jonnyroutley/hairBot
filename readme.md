
Traceback (most recent call last):
  File "name_generator.py", line 129, in <module>
    print(main())
  File "name_generator.py", line 106, in main
    print("New! " + random.choice(standard_product_names+other_product_names) + " for " + random.choice(comparative
s).capitalize()+ " " +random.choice(effects))
  File "/usr/lib/python3.6/random.py", line 260, in choice
    raise IndexError('Cannot choose from an empty sequence') from None
IndexError: Cannot choose from an empty sequence


