


def cut_func(frontcut=int, backcut=int):
    text = "dc=produktion,dc=vorproduktion"
    text_split = text.split(",")
    print(text, text_split)

    for words in text_split:
        words_len = len(words)
        backcut_result = words_len - backcut
        print(words[frontcut:backcut_result])


cut_func(0, 0)
