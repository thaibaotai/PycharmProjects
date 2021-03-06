import sys

available_formatters = ['plain', 'bold', 'italic', 'header', 'link', 'inline-code',
                        'new-line', 'ordered-list', 'unordered-list']
special_commands = ['!help', '!done']
output = ''
formatter = ''


def help_print():
    print('Available formatters: ' + ' '.join(available_formatters))
    print('Special commands: ' + ' '.join(special_commands))


def done():
    with open('output.md', 'w') as op:
        op.write(output)
    sys.exit()


def check_input():
    while True:
        global formatter
        formatter = input('Choose a formatter: ')
        if formatter not in available_formatters + special_commands:
            print('Unknown formatting type or command')
        if formatter == '!help':
            help_print()
        if formatter == '!done':
            done()
        else:
            break


def format_text():
    if formatter == 'header': return header()
    if formatter == 'plain': return plain()
    if formatter == 'bold': return bold()
    if formatter == 'italic': return italic()
    if formatter == 'new-line': return new_line()
    if formatter == 'link': return link()
    if formatter == 'inline-code': return inline_code()
    if formatter == 'ordered-list': return ordered_list(1)
    if formatter == 'unordered-list': return ordered_list(0)


def header():
    level = int(input('Level: '))
    while level not in range(1, 7):
        print('The level should be within the range of 1 to 6')
        level = int(input('Level: '))
    else:
        text = input('Text: ')
    if output == '':
        return '#' * level + ' ' + text + '\n'
    else:
        return '\n' + '#' * level + ' ' + text + '\n'


def plain():
    text = input('Text: ')
    return text


def bold():
    text = input('Text: ')
    return '**' + text + '**'


def italic():
    text = input('Text: ')
    return '*' + text + '*'


def new_line():
    return '\n'


def link():
    label = input('Label: ')
    url = input('URL: ')
    return f'[{label}]({url})'


def inline_code():
    text = input('Text: ')
    return '`' + text + '`'


def ordered_list(_type):
    text_list = []
    rows = int(input('Number of rows: '))
    while rows <= 0:
        print('The number of rows should be greater than zero')
        rows = int(input('Number of rows: '))
    for i in range(rows):
        text_list.append(input(f'Row #{i + 1}: '))
    if _type:
        prefix = [f'{x + 1}. ' for x in range(rows)]
    else:
        prefix = [f'* ' for _ in range(rows)]
    output_list = list(map(lambda x, y: x + y, prefix, text_list))
    return '\n'.join(output_list) + '\n'


while True:
    check_input()
    output += format_text()
    print(output)
