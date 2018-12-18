from nltk.corpus import wordnet as wn


def find_all_variants(word: str, seen_set: set, path: list, alphabet: str='abcdefghijklmnopqrstuvwxyz') -> list:
    word_as_list = list(word)
    variants = list()
    for idx, char in enumerate(word_as_list):
        for idy, letter in enumerate(alphabet):
            if letter != char:
                new_word = ''.join(word_as_list[:idx] + [letter] + word_as_list[idx+1:])
                if new_word in wn.all_lemma_names() and new_word not in seen_set:
                    variants.append(new_word)
    return list(zip([path + [word]] * len(variants), variants))


def riddle(variants: list, end: str, seen: set, depth: int):
    print("Depth: ", depth)
    print("Len variants: ", len(variants))
    for var_path, var_word in variants:
        if var_word == end:
            return var_path + [end]
    seen |= set([value for key, value in variants])
    new_variants = list()
    for var_path, variant in variants:
        new_variants += find_all_variants(variant, seen_set=seen, path=var_path)

    return riddle(new_variants, end, seen, depth + 1)


start_word = 'bride'
end_word = 'groom'
seen_set = {start_word}

print(riddle(find_all_variants(start_word, seen_set, []), end_word, seen_set, 1))
