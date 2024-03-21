import re

def split_para(para):
    return re.findall(r"[\w']+|[-.,!?;\(\)\[\]]", para)

def annotate(para):
    print(para)
    word_list = split_para(para)
    categories = []
    
    for word in word_list:
        c = input(f"What's the category for '{word}'? ")
        categories.append(c)
    return word_list, categories