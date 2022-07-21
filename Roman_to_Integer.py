def romanToInt(s: str):
    array = list(s)
    print(array)
    count = 0
    i = 0
    while i < len(array):
        if array[i] == "I":
            if i <= (len(array) - 2):
                if array[i+1] == "V":
                    count += 4
                    i += 2
                elif array[i+1] == "X":
                    count += 9
                    i += 2
                else:
                    count += 1
                    i += 1
            else:
                count += 1
                i += 1
        elif array[i] == "X":
            if i <= (len(array) - 2):
                if array[i+1] == "L":
                    count += 40
                    i += 2
                elif array[i+1] == "C":
                    count += 90
                    i += 2
                else:
                    count += 10
                    i += 1
            else:
                count += 10
                i += 1
        elif array[i] == "C":
            if i <= (len(array) - 2):
                if array[i+1] == "D":
                    count += 400
                    i += 2
                elif array[i+1] == "M":
                    count += 900
                    i += 2
                else:
                    count += 100
                    i += 1
            else:
                count += 100
                i += 1
        elif array[i] == "V":
            count += 5
            i += 1
        elif array[i] == "L":
            count += 50
            i += 1
        elif array[i] == "D":
            count += 500
            i += 1
        elif array[i] == "M":
            count += 1000
            i += 1
    return count

s = input()
print(s)
print(romanToInt(s))