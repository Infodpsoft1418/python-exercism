from string import ascii_lowercase, ascii_uppercase


def rotate(text, key):
    result = ""
    for letter in text:
        if letter.islower():
            letter = ascii_lowercase[(ascii_lowercase.index(letter) + key) % 26]
        elif letter.isupper():
            letter = ascii_uppercase[(ascii_uppercase.index(letter) + key) % 26]
        result += letter
    return result
