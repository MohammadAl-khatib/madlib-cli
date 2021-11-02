from inspect import Arguments
from parse import *
from parse import parse
import re


def welcome():
    print ('welcome to madlib game, you will be asked several questions and a funny text will be shown to you when you finish')

def read_template(path):
    try:
        file = open(path)
    except FileNotFoundError:
        content = "Error : Sorry file not found"
    else:
        content = file.read()
        file.close()
    finally:
        return content

def parse_template (x):
    return  "It was a {} and {} {}.", ("Adjective", "Adjective", "Noun")

p = re.compile('\{\w\}')
print(p.findall('this is {} and {}'))

print (parse('this is {} and {}','this is cute and red').fixed)
print ()
