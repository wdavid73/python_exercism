def is_valid(isbn):
    isbn = isbn.replace("-","")
    coef = 10
    sum = 0
    if len(isbn) != 10:
        return False
    for x in isbn:
        if x.isdigit() or x is "X":
            if x is "X":
                x = 10
                sum += int(x) * coef
                coef -= 1
            else:
                sum += int(x) * coef
                coef -= 1
        else:
            return False
    if sum % 11 == 0:
        print("true")
        return True
    else:
        return False
