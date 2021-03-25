def getValue(input, type):
    if type == 'absolute':
        if input == [1,2,3,4]:
            return 4
        if input == [2,1,3,4]:
            return 1.8
        if input == [2,4,3,1]:
            return 2
        if input == [3,4,1,2]:
            return 2.6
        if input == [1,2,4,3]:
            return 1.8
        if input == [1,3,4,2]:
            return 2
        if input == [3,1,2,4]:
            return 2
        if input == [4,3,1,2]:
            return 2.6
        if input == [1,4,3,2]:
            return 1.8
        if input == [1,4,2,3]:
            return 2
        if input == [2,3,1,4]:
            return 2
        if input == [2,3,4,1]:
            return 2.6
        if input == [1,3,2,4]:
            return 1.8
        if input == [4,2,1,3]:
            return 2
        if input == [2,1,4,3]:
            return 2.6
        if input == [3,4,2,1]:
            return 3.3
        if input == [3,2,1,4]:
            return 1.8
        if input == [3,2,4,1]:
            return 2
        if input == [4,1,2,3]:
            return 2.6
        if input == [2,4,1,3]:
            return 2.6
        if input == [4,2,3,1]:
            return 1.8
        if input == [4,1,3,2]:
            return 2
        if input == [3,1,4,2]:
            return 2.6
        if input == [4,3,2,1]:
            return 2.6
        return 0
    elif type == 'relative':
        if input == [1,2,3,4]:
            return 4
        if input == [2,1,3,4]:
            return 1.1
        if input == [2,4,3,1]:
            return 1.2
        if input == [3,4,1,2]:
            return 2.2
        if input == [1,2,4,3]:
            return 1.1
        if input == [1,3,4,2]:
            return 1.2
        if input == [3,1,2,4]:
            return 1.2
        if input == [4,3,1,2]:
            return 2.4
        if input == [1,4,3,2]:
            return 1.1
        if input == [1,4,2,3]:
            return 1.2
        if input == [2,3,1,4]:
            return 1.2
        if input == [2,3,4,1]:
            return 1.5
        if input == [1,3,2,4]:
            return 1.1
        if input == [4,2,1,3]:
            return 1.2
        if input == [2,1,4,3]:
            return 2.4
        if input == [3,4,2,1]:
            return 3.2
        if input == [3,2,1,4]:
            return 1.1
        if input == [3,2,4,1]:
            return 1.2
        if input == [4,1,2,3]:
            return 2.1
        if input == [2,4,1,3]:
            return 2.4
        if input == [4,2,3,1]:
            return 1.1
        if input == [4,1,3,2]:
            return 1.2
        if input == [3,1,4,2]:
            return 2.2
        if input == [4,3,2,1]:
            return 2.4
        return 0
    return 0


