def group_by_first_letter(words: list):
    groups = {}
    for word in words:

        first_letter = word[0]

        if first_letter not in groups:
            groups[first_letter] = []
        
        groups[first_letter].append(word)

    return groups

words = ["python", "lake", "mountains", "lift", "penguin"]

print(group_by_first_letter(words))
