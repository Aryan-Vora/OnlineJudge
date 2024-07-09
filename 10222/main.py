import sys

keyboard_map = {
    'e': 'q', 'r': 'w', 't': 'e', 'y': 'r', 'u': 't', 'i': 'y', 'o': 'u', 'p': 'i', '[': 'o', ']': 'p', '\\': '[',
    'd': 'a', 'f': 's', 'g': 'd', 'h': 'f', 'j': 'g', 'k': 'h', 'l': 'j', ';': 'k', "'": 'l', 
    'c': 'z', 'v': 'x', 'b': 'c', 'n': 'v', 'm': 'b', ',': 'n', '.': 'm', '/': ',',
    's': 'a', 'x': 'z',
    'w': 'q',
    'a': '`', 'z': '`',
    ' ': ' ',
    'E': 'Q', 'R': 'W', 'T': 'E', 'Y': 'R', 'U': 'T', 'I': 'Y', 'O': 'U', 'P': 'I', '{': 'O', '}': 'P', '|': '{',
    'D': 'A', 'F': 'S', 'G': 'D', 'H': 'F', 'J': 'G', 'K': 'H', 'L': 'J', ':': 'K', '"': 'L', 
    'C': 'Z', 'V': 'X', 'B': 'C', 'N': 'V', 'M': 'B', '<': 'N', '>': 'M', '?': '<',
    'S': 'A', 'X': 'Z',
    'W': 'Q', 'A': '`', 'Z': '`',
    '1': '1', '2': '2', '3': '3', '4': '4', '5': '5', '6': '6', '7': '7', '8': '8', '9': '9', '0': '0', 
    '-': '-', '=': '=', '!': '!', '@': '@', '#': '#', '$': '$', '%': '%', '^': '^', '&': '&', '*': '*', '(': '(', ')': ')', '_': '_', '+': '+',
    '\n': '\n', '\t': '\t', '\r': '\r'
}

def decode_message(encoded_message):
    decoded_message = []
    for char in encoded_message:
        if char in keyboard_map:
            decoded_message.append(keyboard_map[char])
        else:
            decoded_message.append(char) 
    return ''.join(decoded_message)

encoded_message = sys.stdin.read().strip()

decoded_message = decode_message(encoded_message)

print(decoded_message.lower()) 
