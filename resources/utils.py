class Color:
    white = '\033[1;97m'
    red = '\033[0;91m'
    green = '\033[38;5;77m'
    yellow = '\033[38;5;227'
    purple = '\033[38;5;147m'
    blue = '\033[38;5;81m'
    end = '\033[0m'
    
class Help:
    print('')
    print('MAWTS'.center(70))
    print(' '+'—' * 68 + ' ')
    print('│ Command line tool to manage aws credentials and automate tasks'.ljust(68), '│')
    print(' '+'—' * 68 + ' ')
    print('│ How to use: mawts --profile name'.ljust(68), '│')
    print(' '+'—' * 68 + ' ')
    print('│ --export, -e '.ljust(14), '│ Export temporary credentials in default file '.ljust(53), '│')
    print('│ --list, -l '.ljust(14), '│ List all available profiles '.ljust(53), '│')
    print('│ --profile, -p '.ljust(14), '│ AWS profile to use '.ljust(53), '│')
    print('│ --rotate, -r '.ljust(14), '│ Rotate your credentials keys '.ljust(53), '│')
    print('│ --version, -v '.ljust(14), '│ Show mawts version '.ljust(53), '│')
    print('│ --whoami, -w '.ljust(14), '│ Show AWS user info '.ljust(53), '│')
    print(' '+'—' * 68 + ' ')
    print('0.0.1\n'.rjust(70))