noun_one = input("Noun: ")
noun_two = input("Noun: ")
noun_three = input("Noun: ")
adjective_one = input("Adjective: ")
adjective_two = input("Adjective: ")
adjective_three = input("Adjective: ")
verb_one = input("Verb: ")
verb_two = input("Verb: ")
verb_three = input("Verb: ")

words_for_madlib = (
    noun_one, 
    noun_two, 
    noun_three, 
    adjective_one, 
    adjective_two, 
    adjective_three, 
    verb_one, 
    verb_two, 
    verb_three
    )

print(f"WORDS FOR MADLIBS TYPE: {type(words_for_madlib)}")