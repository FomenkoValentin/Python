def long_repeat(line):
    """
        length the longest substring that consists of the same char
    """
    # your code here
    count = 1
    l = []
    line_1 = line[1:] + line[:1]
    if len(line):
        for i in range(len(line)):
            if line[i] == line_1[i]:
                count += 1
            else:
                l.append(count)
                count = 1
        if len(l):
            return max(l)
        else:
            return count - 1
    else:
        return 0 

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert long_repeat('sdsffffse') == 4, "First"
    assert long_repeat('ddvvrwwwrggg') == 3, "Second"
    assert long_repeat('abababaab') == 2, "Third"
    assert long_repeat('') == 0, "Empty"
    print('"Run" is good. How is "Check"?')
