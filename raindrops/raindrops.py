def convert(number):
    raindrop = ""

    if number % 3 == 0:
        raindrop += "Pling"

    if number % 5 == 0:
        raindrop += "Plang"

    if number % 7 == 0:
        raindrop += "Plong"

    if raindrop == "":
        raindrop = str(number)

    return raindrop
