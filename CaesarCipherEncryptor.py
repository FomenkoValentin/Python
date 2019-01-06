def to_encrypt(text, delta):
    l = []
    for i in text.split():
        for j in i:
            if ord(j) + delta < ord('a'):
                j = chr(ord('z') + 1 - (-delta -  (ord(j) - ord('a'))))
            elif ord(j) + delta > ord('z'):
                j = chr(ord('a') - 1 + (delta -(ord('z') - ord(j))))
            else:
                j = chr(ord(j) + delta)
            l.append(j)
        l.append(" ")
    result = "".join(l[:-1])
    return result

if __name__ == '__main__':
    print("Example:")
    print(to_encrypt('abc', 10))

    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert to_encrypt("a b c", 3) == "d e f"
    assert to_encrypt("a b c", -3) == "x y z"
    assert to_encrypt("simple text", 16) == "iycfbu junj"
    assert to_encrypt("important text", 10) == "swzybdkxd dohd"
    assert to_encrypt("state secret", -13) == "fgngr frperg"
    print("Coding complete? Click 'Check' to earn cool rewards!")
