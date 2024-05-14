import sys
input = sys.stdin.read
data = input().splitlines()

n = int(data[0]) 
blocks = {i: [i] for i in range(n)} 

def find_block(block):
    for pos, stack in blocks.items():
        if block in stack:
            return pos, stack
    return None, None

for command in data[1:]:
    if command == "quit":
        break

    parts = command.split()
    if len(parts) != 4:
        continue

    cmd, a, preposition, b = parts
    a, b = int(a), int(b)
    if a == b:
        continue

    pos_a, stack_a = find_block(a)
    pos_b, stack_b = find_block(b)
    if pos_a == pos_b:
        continue

    index_a = stack_a.index(a)
    index_b = stack_b.index(b)

    if cmd == "move" and preposition == "onto":
        for block in stack_a[index_a + 1:]:
            blocks[block] = [block]
        for block in stack_b[index_b + 1:]:
            blocks[block] = [block]

        stack_a = stack_a[:index_a]
        stack_b = stack_b[:index_b + 1] + [a]

    elif cmd == "move" and preposition == "over":
        for block in stack_a[index_a + 1:]:
            blocks[block] = [block]

        stack_a = stack_a[:index_a]
        stack_b.append(a)

    elif cmd == "pile" and preposition == "onto":
        for block in stack_b[index_b + 1:]:
            blocks[block] = [block]
        stack_b = stack_b[:index_b + 1] + stack_a[index_a:]
        stack_a = stack_a[:index_a]

    elif cmd == "pile" and preposition == "over":
        stack_b.extend(stack_a[index_a:])
        stack_a = stack_a[:index_a]
    blocks[pos_a] = stack_a
    blocks[pos_b] = stack_b
for i in range(n):
    if blocks[i]:  
        print(f"{i}: {' '.join(map(str, blocks[i]))}")
    else:
        print(f"{i}:")
