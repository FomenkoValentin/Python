from typing import List

def checkio(game_result: List[str]) -> str:
    import collections as col
    list_of_rows = []
    for y in range(3):
        list_of_rows.append({x for x in game_result[y]})
        list_of_rows.append({x[y] for x in game_result})
    list_of_rows.append({x[i] for i,x in enumerate(game_result)})
    list_of_rows.append({x[len(game_result)-i -1] for i,x in enumerate(game_result)})
    list_of_win = list(filter(lambda x: len(x)==1,list_of_rows))
    if {'.'} in list_of_win:
        list_of_win.remove({'.'})
    if list_of_win and list_of_win[0] != {'.'}:
        for z in range(len(list_of_win)):
            result = "".join([x for x in list_of_win[z]])
        return col.Counter(result).most_common(3)[0][0]
    return str("D")

if __name__ == '__main__':
    print("Example:")
    print(checkio(["X.O",
                   "XX.",
                   "XOO"]))

    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio([
        "X.O",
        "XX.",
        "XOO"]) == "X", "Xs wins"
    assert checkio([
        "OO.",
        "XOX",
        "XOX"]) == "O", "Os wins"
    assert checkio([
        "OOX",
        "XXO",
        "OXX"]) == "D", "Draw"
    assert checkio([
        "O.X",
        "XX.",
        "XOO"]) == "X", "Xs wins again"
    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")
    
