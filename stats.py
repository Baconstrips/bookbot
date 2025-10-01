def get_num_words(text):
    words = text.split()
    return len(words)


def letters_count(text):
    letters_count = {}
    
    words = text.split()

    for word in text.split():
        for letter in word.lower():
            if letter not in letters_count:
                letters_count[letter] = 1
            else:
                letters_count[letter] += 1

    return letters_count
def get_value(pair):
    return pair[1]

def sorted_list(count):
    items = list(count.items())
    items.sort(key=get_value, reverse=True)
    return items
