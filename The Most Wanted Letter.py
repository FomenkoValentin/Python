def checkio(text: str) -> str:
    import string
    l = []
    d = {x : str.lower(text).count(x) for x in str.lower(text) if x in string.ascii_letters}
    max_value = max(d.values())
    for k,v in d.items():
        if v == max_value:
            l.append(k)
    result = sorted(l)[0]
    return result

if __name__ == '__main__':
    print("Example:")
    print(checkio("Hello World!"))

    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio("Hello World!") == "l", "Hello test"
    assert checkio("How do you do?") == "o", "O is most wanted"
    assert checkio("One") == "e", "All letter only once."
    assert checkio("Oops!") == "o", "Don't forget about lower case."
    assert checkio("AAaooo!!!!") == "a", "Only letters."
    assert checkio("abe") == "a", "The First."
    print("Start the long test")
    assert checkio("a" * 9000 + "b" * 1000) == "a", "Long."
    print("The local tests are done.")
