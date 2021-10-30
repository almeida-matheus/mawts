class Color:
    white = '\033[1;97m'
    red = '\033[0;91m'
    green = '\033[38;5;77m'
    yellow = '\033[38;5;227'
    purple = '\033[38;5;147m'
    blue = '\033[38;5;81m'
    end = '\033[0m'
    
class Help:
    def show(self):
        print('')
        print('MAWTS'.center(70))
        print(' '+'—' * 68 + ' ')
        print('│ CLI to manage AWS credentials ease and automate tasks'.ljust(68), '│')
        print(' '+'—' * 68 + ' ')
        print('│ positional'.ljust(15), ' '.ljust(52), '│')
        # print('│'.ljust(68), '│')
        print('│ profile_name'.ljust(15), '│ AWS profile to use '.ljust(52), '│')
        print(' '+'—' * 68 + ' ')
        print('│ optional'.ljust(15), ' '.ljust(52), '│')
        # print('│'.ljust(68), '│')
        print('│ -e, --export'.ljust(15), '│ Export temporary credentials in default file '.ljust(52), '│')
        print('│ -h, --help'.ljust(15), '│ Show this help message '.ljust(52), '│')
        print('│ -l, --list'.ljust(15), '│ List all available profiles '.ljust(52), '│')
        print('│ -p, --profile'.ljust(15), '│ AWS profile to use '.ljust(52), '│')
        print('│ -r, --rotate'.ljust(15), '│ Rotate your credentials keys '.ljust(52), '│')
        print('│ -v, --version'.ljust(15), '│ Show mawts version '.ljust(52), '│')
        print('│ -w, --whoami'.ljust(15), '│ Show AWS user info '.ljust(52), '│')
        print(' '+'—' * 68 + ' ')
        print('0.0.1\n'.rjust(70))