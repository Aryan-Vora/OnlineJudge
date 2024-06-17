import sys

MAX_CHARS = 1024
generator = 34943
input_lines = sys.stdin.read().splitlines()

for line in input_lines:
    line = line[:MAX_CHARS]

    data_length = 0
    last_character = ''

    for character in line:
        if character == '\n':
            break
        last_character = character
        data_length = ((data_length << 8) + ord(character)) % generator
    data_length = (data_length << 16) % generator
    if data_length != 0:
        data_length = generator - data_length
    if line == "#":
        break

    crc_byte2 = (data_length >> 8) & 0xFF
    crc_byte1 = data_length & 0xFF
    print(f"{crc_byte2:02X} {crc_byte1:02X}")
