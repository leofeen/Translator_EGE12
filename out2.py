while string.find('63') != -1 or string.find('664') != -1 or string.find('6665') != -1:
    if string.find('63') != -1:
        string = string.replace('63', '4', 1)
    else:
        if string.find('664') != -1:
            string = string.replace('664', '65', 1)
        else:
            if string.find('6665') != -1:
                string = string.replace('6665', '63', 1)

