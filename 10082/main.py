import sys

keyboard_map = {
    'w': 'q', 'e': 'w', 'r': 'e', 't': 'r', 'y': 't', 'u': 'y', 'i': 'u', 'o': 'i', 'p': 'o', '[': 'p', ']': '[', '\\': ']',
    's': 'a', 'd': 's', 'f': 'd', 'g': 'f', 'h': 'g', 'j': 'h', 'k': 'j', 'l': 'k', ';': 'l', "'": ';', 
    'x': 'z', 'c': 'x', 'v': 'c', 'b': 'v', 'n': 'b', 'm': 'n', ',': 'm', '.': ',', '/': '.',
    'a': 'a', 'z': 'z',
    'q': 'q',
    ' ': ' ',
    'W': 'Q', 'E': 'W', 'R': 'E', 'T': 'R', 'Y': 'T', 'U': 'Y', 'I': 'U', 'O': 'I', 'P': 'O', '{': 'P', '}': '{', '|': '}',
    'S': 'A', 'D': 'S', 'F': 'D', 'G': 'F', 'H': 'G', 'J': 'H', 'K': 'J', 'L': 'K', ':': 'L', '"': ':', 
    'X': 'Z', 'C': 'X', 'V': 'C', 'B': 'V', 'N': 'B', 'M': 'N', '<': 'M', '>': '<', '?': '>',
    'A': 'A', 'Z': 'Z',
    'Q': 'Q',
    '1': '`', '2': '1', '3': '2', '4': '3', '5': '4', '6': '5', '7': '6', '8': '7', '9': '8', '0': '9', '-': '0', '=': '-',
    '!': '`', '@': '1', '#': '2', '$': '3', '%': '4', '^': '5', '&': '6', '*': '7', '(': '8', ')': '9', '_': '0', '+': '-',
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

print(decoded_message.upper()) 
