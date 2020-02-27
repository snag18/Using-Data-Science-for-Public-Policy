
from collections import Counter
import spacy
from fuzzywuzzy import fuzz
from fuzzywuzzy import process
import en_core_web_sm

# in the terminal
# pip install spacy
# pip install python-Levenshtein
# pip install python -m spacy en_core_web_sm OR
# python -m spacy download en
# opens in Spyder or PyCharm

# if the text is in English use this
nlp = spacy.load('en')

with open("file path") as file:
    text = file.read()

n = nlp(text) # nlp is the name of the code that runs spacy's english language model

create_text = [(X.text, X.label_) for X in n.ents] # creates specific text words and their labels based on different categories

create_label = [x.label_ for x in n.ents] # generates NER label for each quantity in b

category_no = Counter(create_label) # output gives the number of terms in each NER category


entity = [x.text for x in n.ents] # generates actual entities in above categories


entity_no = Counter(entity) # allows us to find the exact number of times an entity occured


people = [] # empty list where entities from one category can be added for a further fuzzy matching process
for x in create_text:
   if x[1] == 'PERSON':
        people.append(x[0])
uniq_ppl = set(people)

organizations = []
for x in create_text:
  if x[1] == 'ORG':
      organizations.append(x[0])
uniq_orgs = set(organizations)

places = []
for x in create_text:
   if x[1] == 'GPE':
        places.append(x[0])
uniq_plc = set(places)


groups = []
for x in create_text:
   if x[1] == 'NORP':
        groups.append(x[0])
uniq_grp = set(groups)

# fuzzy matching process for specific entities in above-mentioned categories
# fuzz.ratio - compares names of entities
# fuzz.partial_ratio - measures specific characters
# fuzz.token_set_ratio - sorts alphabetically and removes stop words
# finds matches of the key word in the same category list or another category list
# no indicates matches found

interest_word_a = process.extract("a", uniq_ppl, limit=100, scorer=fuzz.ratio)

interest_word_b = process.extract("b", uniq_plc, limit=100, scorer=fuzz.partial_ratio)

interest_word_c = process.extract("c", uniq_orgs, limit=100, scorer=fuzz.token_set_ratio)

interest_word_bbc = process.extract("BBC News", uniq_ppl, limit=100, scorer=fuzz.ratio) #imp - bbc matched across people list

interest_word_bbc = process.extract("BBC News", uniq_grp, limit=100, scorer=fuzz.ratio) #imp - bbc matched across group list

interest_word_fox = process.extract("Fox News", uniq_ppl, limit=100, scorer=fuzz.ratio) #imp - fox news matched across people list

interest_word_fox = process.extract("Fox News", uniq_grp, limit=100, scorer=fuzz.ratio) #imp - fox news matched across group list

interest_word_cnn = process.extract("cnn", uniq_ppl, limit=100, scorer=fuzz.ratio) #imp - cnn matched across people list

interest_word_terror = process.extract("Terror Attacks", uniq_orgs, limit=100, scorer=fuzz.ratio) #imp - terror matched across organizations list

interest_word_terror = process.extract("Terror Attacks", uniq_grp, limit=100, scorer=fuzz.ratio) #imp - terror matched across group list

interest_word_isis = process.extract("ISIS", uniq_ppl, limit=100, scorer=fuzz.ratio) #imp - ISIS matched across people list

interest_word_isis = process.extract("ISIS", uniq_grp, limit=100, scorer=fuzz.ratio) #imp - ISIS matched across group list

interest_word_rep = process.extract("Republican", uniq_ppl, limit=100, scorer=fuzz.ratio) #imp - republican matched across people list

interest_word_dem = process.extract("Democrats", uniq_ppl, limit=100, scorer=fuzz.ratio) #imp - democrats matched across people list

interest_word_russia = process.extract("the Russian Federation", uniq_orgs, limit=100, scorer=fuzz.ratio) #imp - russia matched across organizations list

interest_word_iran = process.extract("Iran", uniq_ppl, limit=100, scorer=fuzz.ratio) #imp - iran matched with people list

interest_word_HG = process.extract("Hate Group", uniq_ppl, limit=100, scorer=fuzz.ratio) #imp - hate group matched with people list







