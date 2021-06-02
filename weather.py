# I am using api openweathermap.org
import argparse
import requests

DEFAULT_CITY = r'London'

DEFAULT_API_LINK = r''


def open_file(filepath: str):
    with open(file=filepath, mode='r', encoding='utf-8') as file:
        return file.read()

def mean(town: str, strng: str):
    pass


def variance(town: str, strng: str):
    pass

def set_parser(parser: argparse.ArgumentParser):
    parser.add_argument('-k', '--apikey',
    help='This is the access key to the web resource api', type=str)
    parser.add_argument('-c', '--city', help='City for which weather information is collected',
    type=str, default=DEFAULT_CITY)

def main():
    parser = argparse.ArgumentParser(
        description='This is a CLI application for getting weather data through the api of the climate data storage service',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter
    )
    # set_parser(parser)
    args = parser.parse_args()


    # print(open_file(filepath=path))

if __name__ == '__main__':
    main()