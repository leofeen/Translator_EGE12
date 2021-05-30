import argparse

parser = argparse.ArgumentParser(description='Translates .psdred or .txt into .py')
parser.add_argument('infile', help='Input .psdred or .txt file name', metavar='input')
parser.add_argument('-o', '--output', help='Output .py file name. Defaults to input file name', default=None)

args = parser.parse_args()

input_file_name = args.infile
if input_file_name[-4:] != '.txt' and input_file_name[-7:] != '.psdred':
    raise ValueError('Incorrect input file extention')
output_file_name = args.output
if output_file_name == None:
    dot_position = input_file_name.find('.')
    output_file_name = input_file_name[:dot_position] + '.py'
elif output_file_name[-3:] != '.py':
    raise ValueError('Incorrect output file extention')

with open(input_file_name, encoding='utf-8') as input_file, open(output_file_name, 'w', encoding='utf-8') as output_file:
    input_data = input_file.readlines()
    try:
        assert input_data[-1].strip().strip('\t') == 'КОНЕЦ'
    except AssertionError:
        raise SyntaxError('Invalid syntaxis')

    input_string = ''
    first_input = True
    while input_data[0].find('НАЧАЛО') == -1:
        input_string_line = input_data[0]
        input_string_line = input_string_line.strip().strip('\t')
        if input_string_line != '':    
            _, string_element, number_of_repetition = input_string_line.split()
            if first_input:
                first_input = False
            else:
                input_string += ' + '
            if int(number_of_repetition) != 1:
                input_string += f'\'{string_element}\'*{number_of_repetition}'
            else:
                input_string += f'\'{string_element}\''
        del input_data[0]
    output_file.write(f'string = {input_string}\n')
    output_file.write('\n')

    try:
        assert len(input_data) >= 2
    except AssertionError:
        raise SyntaxError('Invalid syntaxis')

    number_of_spaces = 0
    in_while = 0
    in_if = 0
    while input_data[0] != 'КОНЕЦ':
        line = input_data[0]
        line = line.strip().strip('\t')
        output_file.write(' '*number_of_spaces)

        if line == 'НАЧАЛО':
            pass
        elif line.startswith('//'):
            output_file.write('#' + line[2:] + '\n')
        elif line == 'КОНЕЦ ПОКА':
            number_of_spaces -= 4
            assert in_while != 0
            in_while -= 1
            if in_if == 0:
                output_file.write('\n')
        elif line == 'КОНЕЦ ЕСЛИ':
            number_of_spaces -= 4
            assert in_if != 0
            in_if -= 1
            if in_while == 0:
                output_file.write('\n')
        elif line.startswith('ПОКА'):
            number_of_spaces += 4
            in_while += 1
            output_file.write('while')
            conditions = line[4:].split()
            for condition in conditions:
                assert (condition.startswith('нашлось') or condition.upper() == 'ИЛИ'
                        or condition.upper() == 'И' or condition.upper() == 'НЕ')
                if condition.upper() == 'ИЛИ':
                    output_file.write(' or')
                elif condition.upper() == 'И':
                    output_file.write(' and')
                elif condition.upper() == 'НЕ':
                    output_file.write(' not')
                else:
                    arg = condition[8:-1]
                    output_file.write(f' string.find(\'{arg}\') != -1')
            output_file.write(':\n')
        elif line.startswith('ЕСЛИ'):
            number_of_spaces += 4
            in_if += 1
            output_file.write('if')
            conditions = line[4:].split()
            for condition in conditions:
                assert (condition.startswith('нашлось') or condition.upper() == 'ИЛИ'
                        or condition.upper() == 'И' or condition.upper() == 'НЕ')
                if condition.upper() == 'ИЛИ':
                    output_file.write(' or')
                elif condition.upper() == 'И':
                    output_file.write(' and')
                elif condition.upper() == 'НЕ':
                    output_file.write(' not')
                else:
                    arg = condition[8:-1]
                    output_file.write(f' string.find(\'{arg}\') != -1')
            output_file.write(':\n')
        elif line.startswith('ТО'):
            if input_data[1].find('ИНАЧЕ') != -1:
                number_of_spaces -= 4
            command = line[3:]
            assert command.startswith('заменить')
            args = command[9:-1].split(', ')
            assert len(args) == 2
            output_file.write(f'string = string.replace(\'{args[0]}\', \'{args[1]}\', 1)\n')
        elif line.startswith('ИНАЧЕ'):
            number_of_spaces += 4
            output_file.write('else:\n' + ' '*number_of_spaces)
            command = line[6:]
            assert command.startswith('заменить')
            args = command[9:-1].split(', ')
            assert len(args) == 2
            output_file.write(f'string = string.replace(\'{args[0]}\', \'{args[1]}\', 1)\n')
        elif line.startswith('заменить'):
            args = line[9:-1].split(', ')
            assert len(args) == 2
            output_file.write(f'string = string.replace(\'{args[0]}\', \'{args[1]}\', 1)\n')
        elif line == 'ВЫВОД СТРОКИ':
            output_file.write('print(string)\n')
        elif line == 'ВЫВОД ДЛИНЫ':
            output_file.write('print(len(string))\n')
        elif line == 'ВЫВОД СУММЫ':
            output_file.write('summ = 0\n')
            output_file.write(' '*number_of_spaces + 'for element in string:\n')
            output_file.write(' '*(number_of_spaces + 4) + 'if element.isnumeric(): summ += int(element)\n')
            output_file.write(' '*number_of_spaces + 'print(summ)\n')

        del input_data[0]