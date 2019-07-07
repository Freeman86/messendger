from socket import socket, AF_INET, SOCK_STREAM

import yaml

import utils


def start_server(address):
    sock = socket(AF_INET, SOCK_STREAM)
    sock.bind(address)
    sock.listen(5)
    return sock


def server_listener():
    try:
        address = (HOST, PORT)
        sock = start_server(address)
        while True:
            client, address = sock.accept()
            print(f'Соединение с клиентом {address[0]}:{address[1]}')
            c_request = client.recv(BUFFERSIZE)
            data = utils.decode_json(c_request)
            if data['action'] == 'echo':
                print(data['data'])
            else:
                print('Неизвестная команда')
            client.send(c_request)
            client.close()
    except KeyboardInterrupt:
        print('Завершение работы')


if __name__ == '__main__':
    parser = utils.cli_parser()
    args = parser.parse_args()

    default_config = {
        'host': 'localhost',
        'port': 7777,
        'buffersize': 1024,
    }

    if args.config:
        with open(args.config) as file:
            file_config = yaml.load(file, Loader=yaml.Loader)
            default_config.update(file_config)

    HOST, PORT, BUFFERSIZE = (default_config.get('host'), default_config.get('port'), default_config.get('buffersize'))

    print(f'Сервер запущен на {HOST}:{PORT}')
    server_listener()