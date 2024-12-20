def faro_shuffle(num):
    deck = list(range(1, num+1))
    print(deck)
    shuffled = deck.copy()
    shuffles = 0
    equal = False
    while not equal:
        shuffles += 1
        first_half = shuffled[:num // 2]
        second_half = shuffled[num // 2:]
        shuffled = []
        for f, s in  zip(first_half, second_half):
            shuffled.append(f)
            shuffled.append(s)
        if shuffled == deck:
            equal = True
    return shuffles


print(faro_shuffle(52))