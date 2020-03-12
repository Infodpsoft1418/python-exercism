from string import ascii_lowercase

BLOCKSIZE = 5
translate_ = str.maketrans(ascii_lowercase, ascii_lowercase[::-1])


def _transform(text):
    return "".join([l for l in text if l.isalnum()]).lower().translate(translate_)


def encode(plain_text):
    cipher = _transform(plain_text)
    return " ".join(
        [cipher[i : i + BLOCKSIZE] for i in range(0, len(cipher), BLOCKSIZE)]
    )


def decode(ciphered_text):
    return _transform(ciphered_text)
