import sys
import argparse

import manager


def create_parser():
    parser = argparse.ArgumentParser(description='Clicker')
    parser.add_argument('--input', action='store', type=str, nargs=1)

    return parser


def read_groups(file_path):
    result = []
    with open(file_path, 'r') as f:
        line = f.readline()
        while line:
            result.append(line.strip())
            line = f.readline()
    
    return result


if __name__ == '__main__':
    arg_parser = create_parser()
    option = arg_parser.parse_args(sys.argv[1:])

    if option.input:
        input_file = option.input[0]
    else:
        arg_parser.print_help()
        exit(1)
    
    group_links = read_groups(input_file)

    for group_link in group_links:
        if not manager.group_mining(group_link):
            print(f"error with {group_link} link")
