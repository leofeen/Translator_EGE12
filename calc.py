string = '34' + '+' + '266'

while not string.find('+0') != -1:
    string = string.replace('9+', 'А+', 1)
    string = string.replace('8+', '9+', 1)
    string = string.replace('7+', '8+', 1)
    string = string.replace('6+', '7+', 1)
    string = string.replace('5+', '6+', 1)
    string = string.replace('4+', '5+', 1)
    string = string.replace('3+', '4+', 1)
    string = string.replace('2+', '3+', 1)
    string = string.replace('1+', '2+', 1)
    string = string.replace('0+', '1+', 1)
    while string.find('0А') != -1 or string.find('1А') != -1 or string.find('2А') != -1 or string.find('3А') != -1 or string.find('4А') != -1 or string.find('5А') != -1 or string.find('6А') != -1 or string.find('7А') != -1 or string.find('8А') != -1 or string.find('9А') != -1:
        string = string.replace('0А', '10', 1)
        string = string.replace('1А', '20', 1)
        string = string.replace('2А', '30', 1)
        string = string.replace('3А', '40', 1)
        string = string.replace('4А', '50', 1)
        string = string.replace('5А', '60', 1)
        string = string.replace('6А', '70', 1)
        string = string.replace('7А', '80', 1)
        string = string.replace('8А', '90', 1)
        string = string.replace('9А', 'А0', 1)
        
    string = string.replace('А', '10', 1)
    string = string.replace('+', '+$', 1)
    while string.find('$0') != -1 or string.find('$1') != -1 or string.find('$2') != -1 or string.find('$3') != -1 or string.find('$4') != -1 or string.find('$5') != -1 or string.find('$6') != -1 or string.find('$7') != -1 or string.find('$8') != -1 or string.find('$9') != -1:
        string = string.replace('$0', '0$', 1)
        string = string.replace('$1', '1$', 1)
        string = string.replace('$2', '2$', 1)
        string = string.replace('$3', '3$', 1)
        string = string.replace('$4', '4$', 1)
        string = string.replace('$5', '5$', 1)
        string = string.replace('$6', '6$', 1)
        string = string.replace('$7', '7$', 1)
        string = string.replace('$8', '8$', 1)
        string = string.replace('$9', '9$', 1)
        
    while string.find('$') != -1:
        string = string.replace('0$', '$9', 1)
        string = string.replace('1$', '0', 1)
        string = string.replace('2$', '1', 1)
        string = string.replace('3$', '2', 1)
        string = string.replace('4$', '3', 1)
        string = string.replace('5$', '4', 1)
        string = string.replace('6$', '5', 1)
        string = string.replace('7$', '6', 1)
        string = string.replace('8$', '7', 1)
        string = string.replace('9$', '8', 1)
        
    while string.find('+00') != -1:
        string = string.replace('+00', '+0', 1)
        
    if string.find('+01') != -1:
        string = string.replace('+01', '+1', 1)
        
    if string.find('+02') != -1:
        string = string.replace('+02', '+2', 1)
        
    if string.find('+03') != -1:
        string = string.replace('+03', '+3', 1)
        
    if string.find('+04') != -1:
        string = string.replace('+04', '+4', 1)
        
    if string.find('+05') != -1:
        string = string.replace('+05', '+5', 1)
        
    if string.find('+06') != -1:
        string = string.replace('+06', '+6', 1)
        
    if string.find('+07') != -1:
        string = string.replace('+07', '+7', 1)
        
    if string.find('+08') != -1:
        string = string.replace('+08', '+8', 1)
        
    if string.find('+09') != -1:
        string = string.replace('+09', '+9', 1)
        
    
string = string.replace('+0', '', 1)
print(string)
