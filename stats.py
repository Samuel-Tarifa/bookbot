def get_num_words(text):
    return len(text.split())


def get_char_count(text):
    counter = {}
    for char in text:
        c = char.lower()
        if c not in counter:
            counter[c] = 1
        else:
            counter[c] += 1
    return counter


def dic_list(char_count):
    res = []
    for k, v in char_count.items():
        if k.isalpha():
            res.append({"char": k, "count": v})
    res.sort(key=lambda x: x["count"], reverse=True)
    return res
