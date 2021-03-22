def getValue(input, type):
    if type == 'absolute':
        if input[0] == 1:
            if input[1] == 2:
                if input[2] == 3 and input[3] == 4:
                    return 4
                elif input[2] == 4 and input[3] == 3:
                    return 1.8
                else:
                    return 0
            elif input[1] == 3:
                if input[2] == 2 and input[3] == 4:
                    return 1.8
                elif input[2] == 4 and input[3] == 2:
                    return 2
                else:
                    return 0
            elif input[1] == 4:
                if input[2] == 2 and input[3] == 3:
                    return 2
                elif input[2] == 3 and input[3] == 2:
                    return 1.8
                else:
                    return 0
            else:
                return 0
        elif input[0] == 2:
            if input[1] == 1:
                if input[2] == 3 and input[3] == 4:
                    return 1.8
                elif input[2] == 4 and input[3] == 3:
                    return 2.6
                else:
                    return 0
            elif input[1] == 3:
                if input[2] == 1 and input[3] == 4:
                    return 2
                elif input[2] == 4 and input[3] == 1:
                    return 2.6
                else:
                    return 0
            elif input[1] == 4:
                if input[2] == 2 and input[3] == 3:
                    return 2.6
                elif input[2] == 3 and input[3] == 2:
                    return 2
                else:
                    return 0
            else:
                return 0
        elif input[0] == 3:
            if input[1] == 1:
                if input[2] == 2 and input[3] == 4:
                    return 2
                elif input[2] == 4 and input[3] == 2:
                    return 2.6
                else:
                    return 0
            elif input[1] == 2:
                if input[2] == 1 and input[3] == 4:
                    return 1.8
                elif input[2] == 4 and input[3] == 1:
                    return 2
                else:
                    return 0
            elif input[1] == 4:
                if input[2] == 1 and input[3] == 2:
                    return 2.6
                elif input[2] == 2 and input[3] == 1:
                    return 3.3
                else:
                    return 0
            else:
                return 0
        elif input[0] == 4:
            if input[1] == 1:
                if input[2] == 2 and input[3] == 3:
                    return 2.6
                elif input[2] == 3 and input[3] == 2:
                    return 2
                else:
                    return 0
            elif input[1] == 2:
                if input[2] == 1 and input[3] == 3:
                    return 2.0
                elif input[2] == 3 and input[3] == 1:
                    return 1.8
                else:
                    return 0
            elif input[1] == 4:
                if input[2] == 1 and input[3] == 2:
                    return 2.6
                if input[2] == 2 and input[3] == 1:
                    return 2.6
                else:
                    return 0
            else:
                return 0
        else:
            return 0
    elif type == 'relative':
        if input[0] == 1:
            if input[1] == 2:
                if input[2] == 3:
                    return 4
                else:
                    return 1.1
            elif input[1] == 3:
                if input[2] == 2:
                    return 1.1
                else:
                    return 1.2
            else:
                if input[2] == 2:
                    return 1.2
                else:
                    return 1.1
        elif input[0] == 2:
            if input[1] == 1:
                if input[2] == 3:
                    return 1.1
                else:
                    return 2.4
            elif input[1] == 3:
                if input[2] == 1:
                    return 1.2
                else:
                    return 1.5
            else:
                if input[2] == 1:
                    return 2.4
                else:
                    return 1.2
        elif input[0] == 3:
            if input[1] == 1:
                if input[2] == 2:
                    return 1.2
                else:
                    return 2.2
            elif input[1] == 2:
                if input[2] == 1:
                    return 1.1
                else:
                    return 1.1
            else:
                if input[2] == 1:
                    return 2.2
                else:
                    return 3.2
        else:
            if input[1] == 1:
                if input[2] == 2:
                    return 2.1
                else:
                    return 1.2
            elif input[1] == 2:
                if input[2] == 1:
                    return 1.2
                else:
                    return 1.1
            else:
                if input[2] == 1:
                    return 2.4
                else:
                    return 2.4
    else:
        return 0

