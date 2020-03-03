def three(hour,minutes):
    a = hour / 12 * 360 + minutes / 60 * 30
    b = minutes / 60 * 360
    if abs(a - b) == 180:
        return 180
    else:
        if abs(a - b) > 180:
            return 360 - int(abs(a - b))
        else:
            return int(abs(a - b))


print(three(12,30))

def three1(hour,minutes):
    a = hour / 12 * 360 + minutes / 60 * 30
    b = minutes / 60 * 360
    if a-b>0 and a-b>180:
        return int(360-a+b)
