import sys
text = sys.stdin.read()
result = []
open_quote = True

for char in text:
    if char == '"':
        if open_quote:
            result.append("``")
        else:
            result.append("''")
        open_quote = not open_quote
    else:
        result.append(char)

print(''.join(result), end='')

