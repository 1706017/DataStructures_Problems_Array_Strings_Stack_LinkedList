def word_count_string():
    str = "My name is Amrit and Amrit is a good Boy He is a good person also "
    lst = str.split()
    d = {}
    for i in lst:
        if i not in d.keys():
            d[i] = 0
        d[i] = d[i] + 1
    print(d)

print(word_count_string())


Input: My name is Amrit and Amrit is a good Boy He is a good person also
Output: {'My': 1, 'name': 1, 'is': 3, 'Amrit': 2, 'and': 1, 'a': 2, 'good': 2, 'Boy': 1, 'He': 1, 'person': 1, 'also': 1}
