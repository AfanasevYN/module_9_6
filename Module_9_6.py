
def all_variants(text):
    if not text:
        yield ""
        return

    for i in range(len(text)):
        for l in range(len(text) - i):
            sub = text[l:l + i + 1]
            yield sub


a = all_variants("abc")
for i in a:
    print(i)