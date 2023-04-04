def magick(date):
    date = date.split('.')
    number = int(date[0])
    month = int(date[1])
    year = int(date[2][1:])
    if number * month == year:
        return True
    else:
        return False


print(magick(input()))