def sun_angle(time):
    sun_day =  43200 # from 06:00 to 18:00
    s = int(time.split(':')[0])*3600 + int(time.split(':')[1])*60 - sun_day/2 
    if s in range(sun_day + 1):
        return s/240
    else:
        return "I don't see the sun!"

if __name__ == '__main__':
    print("Example:")
    print(sun_angle("07:00"))

    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert sun_angle("07:00") == 15
    assert sun_angle("01:23") == "I don't see the sun!"
    print("Coding complete? Click 'Check' to earn cool rewards!")
