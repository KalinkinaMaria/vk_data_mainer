import sys
import time
import argparse
from datetime import datetime

import schedule

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


def start(input_file):
    group_links = read_groups(input_file)

    for group_link in group_links:
        if not manager.group_mining(group_link):
            print(f"error with {group_link} link")


if __name__ == '__main__':
    arg_parser = create_parser()
    option = arg_parser.parse_args(sys.argv[1:])

    if option.input:
        input_file = option.input[0]
    else:
        arg_parser.print_help()
        exit(1)
    
    now = datetime.now()
    now_hour = now.hour
    now_minute = now.minute
    
    schedule.every().day.at(f"{now_hour}:{now_minute + 2}").do(start, input_file=input_file)

    while True:
        schedule.run_pending()
        time.sleep(60)
