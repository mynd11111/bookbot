def get_num_words(path):
    return len(path.split())
         
def get_chars_dict(text):
    chars = {}
    for c in text:
        lowered = c.lower()
        if lowered in chars:
            chars[lowered] += 1
        else:
            chars[lowered] = 1
    return chars
    
def get_sorted_list(chars):
    sorted_list = []
    for char, count in chars.items():
        if char.isalpha():
            sorted_list.append({"char": char, "num": count})
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list
        
def sort_on(item):
    return item["num"]
