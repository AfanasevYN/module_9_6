
def all_variants(text):

    for r in range(len(text)):
        for l in range(len(text) - r):
            sub = text[l:l + r + 1]
            yield sub


a = all_variants("abc")
for i in a:
    print(i)
