from socket import socket, AF_INET, SOCK_STREAM

import yaml

import utils


def start_client(address):
    sock = socket(AF_INET, SOCK_STREAM)
    sock.connect(address)
    return sock


def client_message():
    address = (HOST, PORT,)
    sock = start_client(address)
    cmd = input('Введите команду: ')
    msg = input('Введите сообщение: ')
    data = {'action': cmd, 'data': msg}
    sock.send(utils.encode_json(data))
    print(f'Отправлены данные: {data}')
    s_response = sock.recv(BUFFERSIZE)
    print(utils.decode_json(s_response))


if __name__ == '__main__':
    parser = utils.cli_parser()
    args = parser.parse_args()

    default_config = {
        'host': 'localhost',
        'port': 8000,
        'buffersize': 1024,
    }

    if args.config:
        with open(args.config) as file:
            file_config = yaml.load(file, Loader=yaml.Loader)
            default_config.update(file_config)

    HOST, PORT, BUFFERSIZE = (default_config.get('host'), default_config.get('port'), default_config.get('buffersize'))

    print(f'Клиент запущен на {HOST}:{PORT}')
    client_message()