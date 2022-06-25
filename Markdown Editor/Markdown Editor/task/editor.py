import sys

available_formatters = ['plain', 'bold', 'italic', 'header', 'link', 'inline-code',
                        'new-line']
special_commands = ['!help', '!done']


def help_print():
    print('Available formatters: ' + ' '.join(available_formatters))
    print('Special commands: ' + ' '.join(special_commands))


def done():
    sys.exit()


def check_input():
    if formatter not in available_formatters + special_commands:
        print('Unknown formatting type or command')
    if formatter == '!help':
        help_print()
    if formatter == '!done':
        done()


def format_text():
    header() if formatter == 'header'




def header():
    level = int(input('Level: '))
    text = input()
    print('#' * level + text)


def plain():
    text = input()
    print(text)

def bold():
    text = input()
    print('**' + text + '**')


def italic():
    text = input()
    print('*' + text + '*')


def new_line():
    print()


def link():
    label = input('Label: ')
    url = input('URL: ')
    print(f'[{label}]({url})')


def inline_code():
    text = input()
    print('>' + text)

while True:
    formatter = input('Choose a formatter: ')
    check_input()
