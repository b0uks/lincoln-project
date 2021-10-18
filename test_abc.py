upper_letter_range = []
lower_letter_range = []
for i in range(65, 91):
    upper_letter_range.append(i)
for i in range(97, 123):
    lower_letter_range.append(i)
print(len(lower_letter_range))
print(len(upper_letter_range))


def recurse(letter_index, letter_combo, max_letter_count):
    if len(letter_combo) > max_letter_count:
        return letter_combo

    print('letter index: ', letter_index)
    for i, letter in enumerate(lower_letter_range[letter_index:]):
        letter_combo.append(letter)
        print('combo: ', letter_combo)
        recurse(i, letter_combo, max_letter_count)


x = recurse(0, [], 2)

print(x)

