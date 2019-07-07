import json
from argparse import ArgumentParser


def encode_json(msg):
    data = json.dumps(msg)
    message = data.encode('utf-8')
    return message


def decode_json(msg):
    data = msg.decode('utf-8')
    message = json.loads(data)
    return message


def cli_parser():
    parser = ArgumentParser()
    parser.add_argument('-c', '--config', type=str, required=False, help='Путь к файлу с настройками')
    return parser