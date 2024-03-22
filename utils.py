import re
import json

def load_json(file):
    with open(file, "r") as f:
        data = json.loads(f.read())
    return data

def split_para(para):
    return re.findall(r"[\w']+|[-.,!?;/\(\)\[\]]", para)

def to_dict(word_list, categories):
    return {"words": word_list, "ner": categories}

def annotate(para, class_list, name=None):
    print(para)
    word_list = split_para(para)
    categories = []
    
    for i, word in enumerate(word_list):
        c = input(f"What's the category for '{word}'? ")
        categories.append(class_list[c])
        if (i + 1) % 10 == 0:
            print()
            print(' '.join(word_list[i:]))
    if name != None:
        ner_dict = to_dict(word_list, categories)
        with open(f'individual_ner/{name}.json', 'w') as f:
            json.dump(ner_dict, f)
    return word_list, categories