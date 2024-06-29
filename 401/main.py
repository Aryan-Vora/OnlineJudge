import sys

lines = sys.stdin.read().splitlines()

mirror_map = {
    'A': 'A', 'E': '3', 'H': 'H', 'I': 'I', 'J': 'L', 'L': 'J', 'M': 'M',
    'O': 'O', 'S': '2', 'T': 'T', 'U': 'U', 'V': 'V', 'W': 'W', 'X': 'X',
    'Y': 'Y', 'Z': '5', '1': '1', '2': 'S', '3': 'E', '5': 'Z', '8': '8'
}

def is_palindrome(s):
    return s == s[::-1]

def is_mirrored(s):
    mirrored = ''.join(mirror_map.get(c, '') for c in reversed(s))
    return mirrored == s


for line in lines:
    palindrome = is_palindrome(line)
    mirrored = is_mirrored(line)

    if palindrome and mirrored:
        print(f"{line} -- is a mirrored palindrome.")
    elif palindrome:
        print(f"{line} -- is a regular palindrome.")
    elif mirrored:
        print(f"{line} -- is a mirrored string.")
    else:
        print(f"{line} -- is not a palindrome.")
    print() 
