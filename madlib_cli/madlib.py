from logging import exception, raiseExceptions

def welcome(questions,text):
    print ('welcome to madlib game, you will be asked several questions and a funny text will be shown to you when you finish')
    answers=[]
    for question in questions:
        print(f"enter a {question}")
        answers.append(input('> '))
    return merge (text,answers)

def read_template(path):
    try:
        file = open(path)
    except FileNotFoundError:
        raise FileNotFoundError
    else:
        content = file.read()
        file.close()
        return content


def parse_template (text):
    parsed_content=''
    parsed_words =[]
    status=0
    word=''
    for char in text:
        if char == '{':
            status=1
            parsed_content+=char
            continue
        if char == '}':
            status = 0
            # parsed_content+=char
            parsed_words.append(word)
            word=''
        if status == 1:
            word+=char
        if status ==0 :
            parsed_content+=char
            
    return parsed_content,tuple (parsed_words)

def merge(text,inputs):
    return text.format(*inputs)

content = read_template("assets/dark_and_stormy_night_template.txt")
text,questions=parse_template(content)
result=welcome(questions,text)

with open('assets/copy.txt', 'w') as f:
        f.write(result)