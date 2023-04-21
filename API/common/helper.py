import sys
from datetime import datetime
import re
from typing import List, Set, Dict, Tuple
from copy import deepcopy

def now_as_string():
    now = datetime.now().strftime("%Y-%m-%d-%H.%M")
    return now

def jsonize(row, columns):
    return {column: row[index] for index, column in enumerate(columns)}

def argument_parser(just_key=False):
    arguments = {}
    passed_arguments = sys.argv[1:]
    for index, arg in enumerate(passed_arguments):
        if index < len(passed_arguments) - 1:
            a, b = arg, passed_arguments[index]
        else:
            a, b = arg, None
        if just_key:
            key = a.replace('--', '')
            arguments[key] = True
        if a.startswith('--') and '=' in a:
            key, val = a.split('=')
            key = key.replace('--', '')
            val = parse_bool_string(val)
            arguments[key] = val
    return arguments

def parse_bool_string(val):
    if val == "True":
        return True
    elif val == "False":
        return False
    return val

def round_number(number, decimals):
    multiplier = 10 ** decimals
    if number in [float("inf"), float("-inf")]:
        return number
    return round(number * multiplier) / multiplier


def error_message(ex):
    template = "An exception of type {0} occurred. Arguments:\n{1!r}"
    message = template.format(type(ex).__name__, ex.args)
    return message

def error_type(ex):
    return type(ex).__name__



def convert_to_type(value, type):
    if type in (float, int):
        if value == float('nan'):
            return 0
    return type(value)


def group_by(array, key, field):
    map = {}
    for item in array:
        map[item[key]] = []
    for item in array:
        map[item[key]].append(item[field])
    return map

def replace_non_latin_tokens_in_text(text):
    subbed =  re.sub(r'[^a-zA-Z\s]', ' ', text)
    clean = remove_spaces(subbed)
    return clean

def remove_spaces(text):
    splited = [word for word in text.split(' ') if len(word) >= 1]
    return ' '.join(splited)


def product_ranges(num_clusters_dict, current_level):
    levels = [key for key in num_clusters_dict.keys()]
    levels_dict = {level: range(num_clusters_dict[level]) for level in levels[:current_level+1]}
    print(f"For loop will run with these ranges {levels_dict}")
    ranges = [levels_dict[k] for k in levels_dict.keys()]
    return ranges

def indexes_of(array, item):
    return [index for index, x in enumerate(array) if x == item]

def flatten(list_of_lists):
    return [item for sublist in list_of_lists for item in sublist]

def remove_special_characters(text):
    removed = re.sub('(http[s]?|[\W\s_]+)', ' ', text)
    return ' '.join(re.split('[\s]+', removed)).strip(' ')


def remove_prefix(text, prefix):
    if text.startswith(prefix):
        return text[len(prefix):]
    return text

def remove_extra_characters(text: str) -> str:
    removed = re.sub('[^\w\s,.\']+', ' ', text)
    return ' '.join(re.split('[\s]+', removed)).strip(' ')

def remove_ending_punct(text: str) -> str:
    return text.rstrip(".")

def capitalize_first_letter(text: str) -> str:
    return text[0].upper() + text[1:]

def union(lsts: List[Set]) -> List:
    return list(set().union(lsts))

def intersection(a: List, b: List) -> List:
    return list(set(a).intersection(b))



