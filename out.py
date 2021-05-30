string = '>' + '1'*20 + '3'*40 + '2'*15 + '<'

# Комментарий
while not string.find('><') != -1:
    string = string.replace('>1', '3>', 1)
    string = string.replace('>2', '2>', 1)
    string = string.replace('>3', '1>', 1)
    string = string.replace('3<', '<1', 1)
    string = string.replace('2<', '<3', 1)
    string = string.replace('1<', '<2', 1)
    
print(string)
summ = 0
for element in string:
    if element.isnumeric(): summ += int(element)
print(summ)
