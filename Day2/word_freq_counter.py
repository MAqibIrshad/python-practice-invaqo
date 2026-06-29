def word_freq_counter(text):
    freq = {}

    for word in text.lower().split():
        word = word.strip(".,!?;:")
        freq[word] = freq.get(word, 0) + 1

    return freq

print(word_freq_counter("My name is Aqib. I have completed my BSCS from Minhaj University Lahore"))