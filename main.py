__author__ = 'cclau_000'

import nltk
import random
from tkinter import *

NAME1 = [] #only title; NAME[0]
TYPE1 = [] #TYPE[0] = main type, TYPE[1] = subtype
ELEMENT1 = []  #ELEMENT[0] = main color, ELEMENT[1] = sub-color
CC1 = [] #coordinating conjunctions
IN1 = [] #prepositions/subordinating
JJ1 = [] #adjectives
JJR1 = [] #comparative adjectives
JJS1 = [] #superlative adjectives
MD1 = [] #modals
NN1 = [] #singular or mass nouns
NNS1 = [] #plural nouns
NNP1 = [] #singular proper nouns
NNPS1 = [] #plural proper nouns
PRP1 = [] #personal pronouns
RB1 = [] #adverbs
RBR1 = [] #comparative adverbs
RBS1 = [] #superlative adverbs
UH1 = [] #interjection2
VB1 = [] #verbs, base form
VBD1 = [] #verbs, past tense
VBG1 = [] #verbs, gerund or present participle
VBN1 = [] #verbs, past participle
VBP1 = [] #verbs, non-3rd-person singular present
VBZ1 = [] #verbs, 3rd-person singular present

NAME2 = [] #only title; NAME[0]
TYPE2 = [] #TYPE[0] = main type, TYPE[1] = subtype
ELEMENT2 = []  #ELEMENT[0] = main color, ELEMENT[1] = sub-color
CC2 = [] #coordinating conjunctions
IN2 = [] #prepositions/subordinating
JJ2 = [] #adjectives
JJR2 = [] #comparative adjectives
JJS2 = [] #superlative adjectives
MD2 = [] #modals
NN2 = [] #singular or mass nouns
NNS2 = [] #plural nouns
NNP2 = [] #singular proper nouns
NNPS2 = [] #plural proper nouns
PRP2 = [] #personal pronouns
RB2 = [] #adverbs
RBR2 = [] #comparative adverbs
RBS2 = [] #superlative adverbs
UH2 = [] #interjection2
VB2 = [] #verbs, base form
VBD2 = [] #verbs, past tense
VBG2 = [] #verbs, gerund or present participle
VBN2 = [] #verbs, past participle
VBP2 = [] #verbs, non-3rd-person singular present
VBZ2 = [] #verbs, 3rd-person singular present

english_vocab = set(w.lower() for w in nltk.corpus.words.words())

def categorizeWords1(w):
    tagged = nltk.pos_tag(w)
    for tag in tagged:
        if (tag[0].lower() in english_vocab) and (len(tag[0]) > 1):
            if tag[1] == 'CC':
                if tag[0].lower() not in CC1:
                    CC1.append(tag[0].lower())
                    print("found a: coordinating conjunction")
            elif tag[1] == 'IN':
                if tag[0].lower() not in IN1:
                    IN1.append(tag[0].lower())
                    print("found a: preposition or subordinating conjunction")
            elif tag[1] == 'JJ':
                if tag[0].lower() not in JJ1:
                    JJ1.append(tag[0].lower())
                    print("found an: adjective")
            elif tag[1] == 'JJR':
                if tag[0].lower() not in JJR1:
                    JJR1.append(tag[0].lower())
                    print("found a: comparative adjective")
            elif tag[1] == 'JJS':
                if tag[0].lower() not in JJS1:
                    JJS1.append(tag[0].lower())
                    print("found a: superlative adjective")
            elif tag[1] == 'MD':
                if tag[0].lower() not in MD1:
                    MD1.append(tag[0].lower())
                    print("found a: modal")
            elif tag[1] == 'NN':
                if tag[0].lower() not in NN1:
                    NN1.append(tag[0].lower())
                    print("found a: singuar or mass noun")
            elif tag[1] == 'NNS':
                if tag[0].lower() not in NNS1:
                    NNS1.append(tag[0].lower())
                    print("found a: plural noun")
            elif tag[1] == 'NNP':
                if tag[0].lower() not in NNP1:
                    NNP1.append(tag[0].lower())
                    print("found a: singular proper noun")
            elif tag[1] == 'NNPS':
                if tag[0].lower not in NNPS1:
                    NNPS1.append(tag[0].lower())
                    print("found a: plural proper noun")
            elif tag[1] == 'PRP':
                if tag[0].lower() not in PRP1:
                    PRP1.append(tag[0].lower())
                    print("found a: personal pronoun")
            elif tag[1] == 'RB':
                if tag[0].lower() not in RB1:
                    RB1.append(tag[0].lower())
                    print("found an: adverb")
            elif tag[1] == 'RBR':
                if tag[0].lower() not in RBR1:
                    RBR1.append(tag[0].lower())
                    print("found a: comparative adverb")
            elif tag[1] == 'RBS':
                if tag[0].lower() not in RBS1:
                    RBS1.append(tag[0].lower())
                    print("found a: superlative adverb")
            elif tag[1] == 'UH':
                if tag[0].lower() not in UH1:
                    UH1.append(tag[0].lower())
                    print("found an: interjection")
            elif tag[1] == 'VB':
                if tag[0].lower() not in VB1:
                    VB1.append(tag[0].lower())
                    print("found a: verb in its base form")
            elif tag[1] == 'VBD':
                if tag[0].lower() not in VBD1:
                    VBD1.append(tag[0].lower())
                    print("found a: past tense verb")
            elif tag[1] == 'VBG':
                if tag[0].lower() not in VBG1:
                    VBG1.append(tag[0].lower())
                    print("found a: present participle or gerund verb")
            elif tag[1] == 'VBN':
                if tag[0].lower() not in VBN1:
                    VBN1.append(tag[0].lower())
                    print("found a: past participle verb")
            elif tag[1] == 'VBP':
                if tag[0].lower() not in VBP1:
                    VBP1.append(tag[0].lower())
                    print("found a: non-3rd-person singular present verb")
            elif tag[1] == 'VBZ':
                if tag[0].lower() not in VBZ1:
                    VBZ1.append(tag[0].lower())
                    print("found a: 3rd person singular present verb")
    return

def categorizeWords2(w):
    tagged = nltk.pos_tag(w)
    for tag in tagged:
        if (tag[0].lower() in english_vocab) and (len(tag[0]) > 1):
            if tag[1] == 'CC':
                if tag[0].lower() not in CC2:
                    CC2.append(tag[0].lower())
                    print("found a: coordinating conjunction")
            elif tag[1] == 'IN':
                if tag[0].lower() not in IN2:
                    IN2.append(tag[0].lower())
                    print("found a: preposition or subordinating conjunction")
            elif tag[1] == 'JJ':
                if tag[0].lower() not in JJ2:
                    JJ2.append(tag[0].lower())
                    print("found an: adjective")
            elif tag[1] == 'JJR':
                if tag[0].lower() not in JJR2:
                    JJR2.append(tag[0].lower())
                    print("found a: comparative adjective")
            elif tag[1] == 'JJS':
                if tag[0].lower() not in JJS2:
                    JJS2.append(tag[0].lower())
                    print("found a: superlative adjective")
            elif tag[1] == 'MD':
                if tag[0].lower() not in MD2:
                    MD2.append(tag[0].lower())
                    print("found a: modal")
            elif tag[1] == 'NN':
                if tag[0].lower() not in NN2:
                    NN2.append(tag[0].lower())
                    print("found a: singuar or mass noun")
            elif tag[1] == 'NNS':
                if tag[0].lower() not in NNS2:
                    NNS2.append(tag[0].lower())
                    print("found a: plural noun")
            elif tag[1] == 'NNP':
                if tag[0].lower() not in NNP2:
                    NNP2.append(tag[0].lower())
                    print("found a: singular proper noun")
            elif tag[1] == 'NNPS':
                if tag[0].lower not in NNPS2:
                    NNPS2.append(tag[0].lower())
                    print("found a: plural proper noun")
            elif tag[1] == 'PRP':
                if tag[0].lower() not in PRP2:
                    PRP2.append(tag[0].lower())
                    print("found a: personal pronoun")
            elif tag[1] == 'RB':
                if tag[0].lower() not in RB2:
                    RB2.append(tag[0].lower())
                    print("found an: adverb")
            elif tag[1] == 'RBR':
                if tag[0].lower() not in RBR2:
                    RBR2.append(tag[0].lower())
                    print("found a: comparative adverb")
            elif tag[1] == 'RBS':
                if tag[0].lower() not in RBS2:
                    RBS2.append(tag[0].lower())
                    print("found a: superlative adverb")
            elif tag[1] == 'UH':
                if tag[0].lower() not in UH2:
                    UH2.append(tag[0].lower())
                    print("found an: interjection")
            elif tag[1] == 'VB':
                if tag[0].lower() not in VB2:
                    VB2.append(tag[0].lower())
                    print("found a: verb in its base form")
            elif tag[1] == 'VBD':
                if tag[0].lower() not in VBD2:
                    VBD2.append(tag[0].lower())
                    print("found a: past tense verb")
            elif tag[1] == 'VBG':
                if tag[0].lower() not in VBG2:
                    VBG2.append(tag[0].lower())
                    print("found a: present participle or gerund verb")
            elif tag[1] == 'VBN':
                if tag[0].lower() not in VBN2:
                    VBN2.append(tag[0].lower())
                    print("found a: past participle verb")
            elif tag[1] == 'VBP':
                if tag[0].lower() not in VBP2:
                    VBP2.append(tag[0].lower())
                    print("found a: non-3rd-person singular present verb")
            elif tag[1] == 'VBZ':
                if tag[0].lower() not in VBZ2:
                    VBZ2.append(tag[0].lower())
                    print("found a: 3rd person singular present verb")
    return

varied_text = {
    "Dragon": {
        "arrival_phrase": ["descends from the sky", "soars down to the field", "heavily stamps across the valley"],
        "verb": ["roars", "stomps the ground", "tramples the ground beneath it"],
        "noun": ["cry", "strength", "power"],
        "name": ["the dragon"]
    },
    "Balanced": {
        "arrival_phrase": ["confidently strides into the field", "gallantly rides into the field"],
        "verb": ["readies its position", "boldly stands", "sturdily holds"],
        "noun": ["balance", "stance", "form"],
        "name": ["the balanced", "the fearless", "the brave"]
    },
    "Physical": {
        "arrival_phrase": ["slowly stomps into the field", "gradually stomps into the field"],
        "verb": ["flexes its muscles", "poses", "stands"],
        "noun": ["sturdiness", "might", "form"],
        "name": ["the physical", "the mighty", "the forceful", "the strong"]
    },
    "Healer": {
        "arrival_phrase": ["elegantly dances onto the field", "gracefully dances onto the field"],
        "verb": ["readies its spells", "prepares its incantations"],
        "noun": ["rejuvinating power", "restorative magic"],
        "name": ["the healer"]
    },
    "Attacker": {
        "arrival_phrase": ["hastily rides onto the field", "ferociously rides onto the field", "loudly gallops onto the field"],
        "verb": ["slashes its claws through the air", "clashes its stinging blades", "courageously displays its blades"],
        "noun": ["confidence", "fury", "power", "aggression"],
        "name": ["the attacker", "the warrior", "a fighter", "a champion"]
    },
    "God": {
        "arrival_phrase": ["descends from the heavens", "magically appears in the field", "spontaneously materializes on the field"],
        "verb": ["shines", "emanates", "violently radiates"],
        "noun": ["and infinite power", ", raw power", "glory", "splendor"],
        "name": ["the gods", "the divine", "the almighty", "the eternal", "the heavens"]
    },
    "Devil": {
        "arrival_phrase": ["ascends from the depths of hell", "dauntingly emerges from the darkness", "manifests itself on the field"],
        "verb": ["frightens the crowd", "spawns its shadowy minions", "engulfs the field in shadow"],
        "noun": ["and demonic power", ", raw power", "and sinful power", "and malicious fury"],
        "name": ["the devil", "hell", "the shadows"]
    },
    "Machine": {
        "arrival_phrase": ["propels its metallic form onto the field", "jettisons itself onto the field", "arrives with disordant crash"],
        "verb": ["grinds its gears", "charges its weapons"],
        "noun": [", artificial power", ", state-of-the-art constructs", "constructs"],
        "name": ["the machine", "the future"]
    },
    "Fire": {
        "adj": ["ablaze", "aflame", "blazing"],
        "noun": ["fire", "flames", "infernos"],
        "participle": ["incinerating", "burning", "singeing", "melting", "disintegrating"],
	    "location": ["the ground beneath it", "the earth beneath it", "the land beneath it"]
    },
    "Water": {
        "adj": ["soaked", "cloaked", "awash"],
        "noun": ["waters", "streams", "torrents", "floods", "tides"],
        "participle": ["flowing from", "rushing from", "cascading from"],
	    "location": ["the ocean", "the sea", "the stormy sky"]
    },
    "Wood": {
        "adj": ["armored", "protected", "guarded"],
        "noun": ["boulders", "timbers", "earthen fissures"],
        "participle": ["tearing up from", "growing forth from"],
	    "location": ["the forest", "the earth", "the land", "the woods", "the mountains"]
    },
    "Light": {
        "adj": ["smothered", "illuminated", "engulfed"],
        "noun": ["light", "glow", "shimmer", "sheen", "luster"],
        "participle": ["shining down upon", "illuminating the entirety of", "radiating upon all"],
	    "location": ["the land", "the world", "the earth", "the field"]
    },
    "Dark": {
        "adj": ["veiled", "smothered", "cloaked", "concealed"],
        "noun": ["shadows", "darkness", "umbra", "shade"],
        "participle": ["looming over", "engulfing the entirety of"],
	    "location": ["the land", "the earth"]
    },
    "Power_Adj": ["mighty", "boisterous", "glorious", "enormous", "majestic", "tremendous", "awesome", "encompassing", "raucous", "dazzling", "grand", "brilliant"],
    "Arrival_Conjunction_Verb": ["As it arrives", "Upon entering the field", "After making its presence known", "After making its entrance", "After finding its place in the field"]
}

def rand(stuff):
    return random.choice(stuff)

def windowText():
    if len(NAME1) > 1:
        text.insert(INSERT, NAME1[1] + ", the " + NAME1[0] + ", ")
    else:
        text.insert(INSERT, NAME1[0] + " ")
    text.insert(INSERT, arrival_template_1)
    text.insert(INSERT, "\n \n")
    if len(NAME2) > 1:
        text.insert(INSERT, NAME2[1] + ", the " + NAME2[0] + ", ")
    else:
        text.insert(INSERT, NAME2[0] + " ")
    text.insert(INSERT, arrival_template_2)
    text.insert(INSERT, "\n \n")

    sentence_template_list = get_sentence_templates()
    for item in sentence_template_list:
        text.insert(INSERT, item)
        text.insert(INSERT, "\n \n")


    # text.insert(INSERT, "Name: \n")
    # text.insert(INSERT, NAME1)
    # text.insert(INSERT, '\n \n')
    # text.insert(INSERT, "Types: \n")
    # text.insert(INSERT, TYPE1)
    # text.insert(INSERT, '\n \n')
    # text.insert(INSERT, "Elements: \n")
    # text.insert(INSERT, ELEMENT1)
    # text.insert(INSERT, '\n \n')
    # text.insert(INSERT, "Coordinating Conjunctions: \n")
    # text.insert(INSERT, CC1)
    # text.insert(INSERT, '\n \n')
    # text.insert(INSERT, "Prepositions/Subordinating Conjunctions: \n")
    # text.insert(INSERT, IN1)
    # text.insert(INSERT, '\n \n')
    # text.insert(INSERT, "Adjectives: \n")
    # text.insert(INSERT, JJ1)
    # text.insert(INSERT, '\n \n')
    # text.insert(INSERT, "Comparative Adjectives: \n")
    # text.insert(INSERT, JJR1)
    # text.insert(INSERT, '\n \n')
    # text.insert(INSERT, "Superlative Adjectives: \n")
    # text.insert(INSERT, JJS1)
    # text.insert(INSERT, '\n \n')
    # text.insert(INSERT, "Modals: \n")
    # text.insert(INSERT, MD1)
    # text.insert(INSERT, '\n \n')
    # text.insert(INSERT, "Singular/Mass Nouns: \n")
    # text.insert(INSERT, NN1)
    # text.insert(INSERT, '\n \n')
    # text.insert(INSERT, "Plural Nouns: \n")
    # text.insert(INSERT, NNS1)
    # text.insert(INSERT, '\n \n')
    # text.insert(INSERT, "Singular Proper Nouns: \n")
    # text.insert(INSERT, NNP1)
    # text.insert(INSERT, '\n \n')
    # text.insert(INSERT, "Plural Proper Nouns: \n")
    # text.insert(INSERT, NNPS1)
    # text.insert(INSERT, '\n \n')
    # text.insert(INSERT, "Personal Pronouns: \n")
    # text.insert(INSERT, PRP1)
    # text.insert(INSERT, '\n \n')
    # text.insert(INSERT, "Adverbs: \n")
    # text.insert(INSERT, RB1)
    # text.insert(INSERT, '\n \n')
    # text.insert(INSERT, "Comparative Adverbs: \n")
    # text.insert(INSERT, RBR1)
    # text.insert(INSERT, '\n \n')
    # text.insert(INSERT, "Superlative Adverbs: \n")
    # text.insert(INSERT, RBS1)
    # text.insert(INSERT, '\n \n')
    # text.insert(INSERT, "Interjections: \n")
    # text.insert(INSERT, UH1)
    # text.insert(INSERT, '\n \n')
    # text.insert(INSERT, "Verbs in Base Form: \n")
    # text.insert(INSERT, VB1)
    # text.insert(INSERT, '\n \n')
    # text.insert(INSERT, "Verbs in Past Tense: \n")
    # text.insert(INSERT, VBD1)
    # text.insert(INSERT, '\n \n')
    # text.insert(INSERT, "Present Participle or Gerund Verbs: \n")
    # text.insert(INSERT, VBG1)
    # text.insert(INSERT, '\n \n')
    # text.insert(INSERT, "Past Participle Words: \n")
    # text.insert(INSERT, VBN1)
    # text.insert(INSERT, '\n \n')
    # text.insert(INSERT, "Non-3rd-Person Singular Present Verbs: \n")
    # text.insert(INSERT, VBP1)
    # text.insert(INSERT, '\n \n')
    # text.insert(INSERT, "3rd-Person Singular Present Verbs: \n")
    # text.insert(INSERT, VBZ1)
    # text.insert(INSERT, '\n \n')
    # text.insert(INSERT, "-----------------------------------------------------------------------------")
    # text.insert(INSERT, "Name: \n")
    # text.insert(INSERT, NAME2)
    # text.insert(INSERT, '\n \n')
    # text.insert(INSERT, "Types: \n")
    # text.insert(INSERT, TYPE2)
    # text.insert(INSERT, '\n \n')
    # text.insert(INSERT, "Elements: \n")
    # text.insert(INSERT, ELEMENT2)
    # text.insert(INSERT, '\n \n')
    # text.insert(INSERT, "Coordinating Conjunctions: \n")
    # text.insert(INSERT, CC2)
    # text.insert(INSERT, '\n \n')
    # text.insert(INSERT, "Prepositions/Subordinating Conjunctions: \n")
    # text.insert(INSERT, IN2)
    # text.insert(INSERT, '\n \n')
    # text.insert(INSERT, "Adjectives: \n")
    # text.insert(INSERT, JJ2)
    # text.insert(INSERT, '\n \n')
    # text.insert(INSERT, "Comparative Adjectives: \n")
    # text.insert(INSERT, JJR2)
    # text.insert(INSERT, '\n \n')
    # text.insert(INSERT, "Superlative Adjectives: \n")
    # text.insert(INSERT, JJS2)
    # text.insert(INSERT, '\n \n')
    # text.insert(INSERT, "Modals: \n")
    # text.insert(INSERT, MD2)
    # text.insert(INSERT, '\n \n')
    # text.insert(INSERT, "Singular/Mass Nouns: \n")
    # text.insert(INSERT, NN2)
    # text.insert(INSERT, '\n \n')
    # text.insert(INSERT, "Plural Nouns: \n")
    # text.insert(INSERT, NNS2)
    # text.insert(INSERT, '\n \n')
    # text.insert(INSERT, "Singular Proper Nouns: \n")
    # text.insert(INSERT, NNP2)
    # text.insert(INSERT, '\n \n')
    # text.insert(INSERT, "Plural Proper Nouns: \n")
    # text.insert(INSERT, NNPS2)
    # text.insert(INSERT, '\n \n')
    # text.insert(INSERT, "Personal Pronouns: \n")
    # text.insert(INSERT, PRP2)
    # text.insert(INSERT, '\n \n')
    # text.insert(INSERT, "Adverbs: \n")
    # text.insert(INSERT, RB2)
    # text.insert(INSERT, '\n \n')
    # text.insert(INSERT, "Comparative Adverbs: \n")
    # text.insert(INSERT, RBR2)
    # text.insert(INSERT, '\n \n')
    # text.insert(INSERT, "Superlative Adverbs: \n")
    # text.insert(INSERT, RBS2)
    # text.insert(INSERT, '\n \n')
    # text.insert(INSERT, "Interjections: \n")
    # text.insert(INSERT, UH2)
    # text.insert(INSERT, '\n \n')
    # text.insert(INSERT, "Verbs in Base Form: \n")
    # text.insert(INSERT, VB2)
    # text.insert(INSERT, '\n \n')
    # text.insert(INSERT, "Verbs in Past Tense: \n")
    # text.insert(INSERT, VBD2)
    # text.insert(INSERT, '\n \n')
    # text.insert(INSERT, "Present Participle or Gerund Verbs: \n")
    # text.insert(INSERT, VBG2)
    # text.insert(INSERT, '\n \n')
    # text.insert(INSERT, "Past Participle Words: \n")
    # text.insert(INSERT, VBN2)
    # text.insert(INSERT, '\n \n')
    # text.insert(INSERT, "Non-3rd-Person Singular Present Verbs: \n")
    # text.insert(INSERT, VBP2)
    # text.insert(INSERT, '\n \n')
    # text.insert(INSERT, "3rd-Person Singular Present Verbs: \n")
    # text.insert(INSERT, VBZ2)
    # text.insert(INSERT, '\n \n')
    return

root = Tk()
frame = Frame(root)
scrollbar = Scrollbar(root)
text = Text(root, yscrollcommand=scrollbar.set)
frame.pack()
scrollbar.pack(side=RIGHT, fill=Y)

file = open("monster1.txt", 'r', errors='ignore')
for line in file:
    line = line.strip(' ')
    if line and (line != '\n'):
        if len(line) < 1000:
            if line.find("Name:", 0, 5) != -1:
                templine = line.replace("Name:", "")
                templine = templine.replace("\n", "")
                NAME1 = templine.split(",")
            if line.find("Type:", 0, 5) != -1:
                templine = line.replace("Type:", "")
                templine = templine.replace("\n", "")
                templine = templine.replace("/", "")
                TYPE1 = templine.split()
            if line.find("Element:", 0, 8) != -1:
                templine = line.replace("Element:", "")
                templine = templine.replace("\n", "")
                templine = templine.replace("/", "")
                ELEMENT1 = templine.split()
            sentence = nltk.sent_tokenize(line)
            for doc in sentence:
                words = nltk.word_tokenize(doc)
                categorizeWords1(words)
file.close()

file = open("monster2.txt", 'r', errors='ignore')
for line in file:
    line = line.strip(' ')
    if line and (line != '\n'):
        if len(line) < 1000:
            if line.find("Name:", 0, 5) != -1:
                templine = line.replace("Name:", "")
                templine = templine.replace("\n", "")
                NAME2 = templine.split(",")
            if line.find("Type:", 0, 5) != -1:
                templine = line.replace("Type:", "")
                templine = templine.replace("\n", "")
                templine = templine.replace("/", "")
                TYPE2 = templine.split()
            if line.find("Element:", 0, 8) != -1:
                templine = line.replace("Element:", "")
                templine = templine.replace("\n", "")
                templine = templine.replace("/", "")
                ELEMENT2 = templine.split()
            sentence = nltk.sent_tokenize(line)
            for doc in sentence:
                words = nltk.word_tokenize(doc)
                categorizeWords2(words)

def onReturnKey(event):
    sentence_template_list = get_sentence_templates()
    for template in sentence_template_list:
        text.insert(INSERT, template)
        text.insert(INSERT, "\n \n")
    text.see(END)

root.bind("<Return>", onReturnKey)

file.close()

first_char_name = None
second_char_name = None
if len(NAME1) > 1:
    first_char_name = NAME1[1]
else:
    first_char_name = NAME1[0]
if len(NAME2) > 1:
    second_char_name = NAME2[1]
else:
    second_char_name = NAME2[0]

arrival_template_1 = rand(varied_text[TYPE1[0]]["arrival_phrase"]) + ", " + rand(varied_text[ELEMENT1[0]]["adj"]) + " in its " + rand(varied_text["Power_Adj"]) + " " + rand(varied_text[ELEMENT1[0]]["noun"]) + " with its " + rand(varied_text["Power_Adj"]) + " " + rand(varied_text[ELEMENT1[1]]["noun"]) + " " + rand(varied_text[ELEMENT1[1]]["participle"]) + " " + rand(varied_text[ELEMENT1[1]]["location"]) + ". " + rand(varied_text["Arrival_Conjunction_Verb"]) + ", it " + rand(varied_text[TYPE1[1]]["verb"]) + " with the " + rand(varied_text["Power_Adj"]) + " " + rand(varied_text[TYPE1[1]]["noun"]) + " of " + rand(varied_text[TYPE1[1]]["name"]) + "."
arrival_template_2 = rand(varied_text[TYPE2[0]]["arrival_phrase"]) + ", " + rand(varied_text[ELEMENT2[0]]["adj"]) + " in its " + rand(varied_text["Power_Adj"]) + " " + rand(varied_text[ELEMENT2[0]]["noun"]) + " with its " + rand(varied_text["Power_Adj"]) + " " + rand(varied_text[ELEMENT2[1]]["noun"]) + " " + rand(varied_text[ELEMENT2[1]]["participle"]) + " " + rand(varied_text[ELEMENT2[1]]["location"]) + ". " + rand(varied_text["Arrival_Conjunction_Verb"]) + ", it " + rand(varied_text[TYPE2[1]]["verb"]) + " with the " + rand(varied_text["Power_Adj"]) + " " + rand(varied_text[TYPE2[1]]["noun"]) + " of " + rand(varied_text[TYPE2[1]]["name"]) + "."


def get_sentence_templates():
    sentence_templates = []
    sentence_templates.append("First Character~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    try:
        template11 = first_char_name + " " + rand(VBZ1) + " " + rand(JJR1) + " " + rand(IN1) + " the " + rand(NNP1).capitalize() + "."
        sentence_templates.append(template11)
    except IndexError:
        sentence_templates.append("THIS PAGE DOES NOT CONTAIN ONE OF THE PARTS OF SPEECH REQUIRED FOR THIS TEMPLATE.")
    try:
        template12 = rand(PRP1).capitalize() + " " + rand(RB1) + " " + rand(VB1) + " " + rand(RB1) + " " + rand(RBR1) + " " + rand(IN1) + " the " + rand(NNP1).capitalize() + "."
        sentence_templates.append(template12)
    except IndexError:
        sentence_templates.append("THIS PAGE DOES NOT CONTAIN ONE OF THE PARTS OF SPEECH REQUIRED FOR THIS TEMPLATE.")
    try:
        template13 = first_char_name + " " + rand(VBD1) + " " + rand(JJ1) + ", " + rand(CC1) + " " + second_char_name + " " + rand(VBZ2) + " " + rand(VBG2) + " " + rand(RB2) + "."
        sentence_templates.append(template13)
    except IndexError:
        sentence_templates.append("THIS PAGE DOES NOT CONTAIN ONE OF THE PARTS OF SPEECH REQUIRED FOR THIS TEMPLATE.")
    sentence_templates.append("Second Character~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    try:
        template21 = second_char_name + " " + rand(VBZ2) + " " + rand(JJR2) + " " + rand(IN2) + " the " + rand(NNP2).capitalize() + "."
        sentence_templates.append(template21)
    except IndexError:
        sentence_templates.append("THIS PAGE DOES NOT CONTAIN ONE OF THE PARTS OF SPEECH REQUIRED FOR THIS TEMPLATE.")
    try:
        template22 = rand(PRP2).capitalize() + " " + rand(RB2) + " " + rand(VB2) + " " + rand(RB2) + " " + rand(RBR2) + " " + rand(IN2) + " the " + rand(NNP2).capitalize() + "."
        sentence_templates.append(template22)
    except IndexError:
        sentence_templates.append("THIS PAGE DOES NOT CONTAIN ONE OF THE PARTS OF SPEECH REQUIRED FOR THIS TEMPLATE.")
    try:
        template23 = second_char_name + " " + rand(VBD2) + " " + rand(JJ2) + ", " + rand(CC2) + " " + first_char_name + " " + rand(VBZ1) + " " + rand(VBG1) + " " + rand(RB1) + "."
        sentence_templates.append(template23)
    except IndexError:
        sentence_templates.append("THIS PAGE DOES NOT CONTAIN ONE OF THE PARTS OF SPEECH REQUIRED FOR THIS TEMPLATE.")

    return sentence_templates

windowText()
text.insert(END, "")
text.pack()
scrollbar.config(command=text.yview)

root.mainloop()