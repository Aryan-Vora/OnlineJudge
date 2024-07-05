import sys

def pig_latin(word):
    vowels = "aeiouAEIOU"
    if word[0] in vowels:
        return word + "ay"
    else:
        return word[1:] + word[0] + "ay"

def convert_line_to_pig_latin(line):
    words = []
    current_word = []
    for char in line:
        if char.isalpha():
            current_word.append(char)
        else:
            if current_word:
                words.append("".join(current_word))
                current_word = []
            words.append(char)
    if current_word:
        words.append("".join(current_word))
    
    pig_latin_words = []
    for word in words:
        if word.isalpha():
            pig_latin_words.append(pig_latin(word))
        else:
            pig_latin_words.append(word)
    
    return "".join(pig_latin_words)

def convert_text_to_pig_latin(text):
    lines = text.split('\n')
    pig_latin_lines = [convert_line_to_pig_latin(line) for line in lines]
    return '\n'.join(pig_latin_lines)

input_text = sys.stdin.read()
print(convert_text_to_pig_latin(input_text), end='')
