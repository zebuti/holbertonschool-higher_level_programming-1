#!/usr/bin/python3
"""
"""
def text_indentation(text):
    """
    prints a text with 2 new lines after each of these characters: ., ? and :
    """
    if type(text) != str:
        raise TypeError("text must be a string")
    toCatAfter = ['.', '?', ':']

    # Removes the space after special chars
    idx = 0
    for items in text:
        if items in toCatAfter:
            if text[idx + 1] == " ":
                text = text[:idx + 1] + text[idx + 2:]
        else:
            idx += 1

    # Cats '\n\n' after the special char with removed space
    idx = 0
    for items in text:
        if items in toCatAfter:
            text = text[:idx + 1] + '\n\n' + text[idx + 1:]
            idx += 3
        else:
            idx += 1

    print(text, end='')
