import math

def cipher_text(plain_text):
    norm_text = "".join(filter(str.isalnum, plain_text)).lower()
    size = len(norm_text)
    cols = math.ceil(math.sqrt(size))
    
    if cols == 0:
        return ""

    pad = (cols - size) % cols
    norm_text += " " * pad
    chunks = [""  for i in range(cols)]
    
    for idx, c in enumerate(norm_text):
        idx = idx % cols
        chunks[idx] += c
    


    return " ".join(chunks)

