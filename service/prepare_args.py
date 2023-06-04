import argparse


def prepare_args() -> argparse.Namespace:
    """
    Подготавливает и парсит аргументы командной строки.

    Возвращает:
    --------
    argparse.Namespace
        Объект, содержащий значения аргументов командной строки.
    """
    arg_parser = argparse.ArgumentParser(
        prog='Сheating SNTP-server',
        description='SNTP server which replies to client request packets with delay'
    )
    arg_parser.add_argument('-d', dest='delay', type=int, default=0,
                            help='Delay relative to real time')
    arg_parser.add_argument('-p', '--port', dest='port', type=int, default=123,
                            help='Port for starting the server')

    return arg_parser.parse_args()