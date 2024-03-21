import re
import json

def split_para(para):
    return re.findall(r"[\w']+|[-.,!?;\(\)\[\]]", para)

def to_dict(word_list, categories):
    return {"words": word_list, "ner": categories}

def annotate(para, name=None):
    print(para)
    word_list = split_para(para)
    categories = []
    
    for word in word_list:
        c = input(f"What's the category for '{word}'? ")
        categories.append(c)
        if word == '.':
            print()
            print(para)
    if name != None:
        ner_dict = to_dict(word_list, categories)
        with open(f'{name}.json', 'w') as f:
            json.dump(ner_dict, f)
    return word_list, categories