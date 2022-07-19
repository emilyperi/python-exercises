import re

def encode(plain_text, a, b):
    inverse(a)
    chunks = chunkify(plain_text)
    return ' '.join([rotate(chunk, a, b) for chunk in chunks])


def decode(ciphered_text, a, b):
    a_inv = inverse(a)
    chunks = ciphered_text.split()
    return ''.join([rotate(chunk, a_inv, -1 * b * a_inv) for chunk in chunks])


def rotate(chunk, a, b):
    rotated_chunk = []
    for char in chunk:
        if char.isalpha():
            rotated_chunk.append(to_char((a * to_int(char) +  b) % 26))
        else:
            rotated_chunk.append(char)
    return ''.join(rotated_chunk)


def chunkify(text):
    clean_text = re.sub(r'\W+', r'', text)
    chunks = []
    size = len(clean_text)
    start = 0
    stop = 5
    
    while stop < size:
        chunks.append(clean_text[start:stop])
        start = stop
        stop += 5

    chunks.append(clean_text[start:size])
    return chunks

def to_int(c):
    return ord(str.lower(c)) - ord('a')

def to_char(i):
    return chr(i + ord('a'))

def inverse(a):
    for i in range(0, 26):
        if (a * i) % 26 == 1:
            return i
    raise ValueError("key must be co-prime with 26")
