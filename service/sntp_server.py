import socket
from multiprocessing.pool import ThreadPool
from packets import PackageGenerator
import prepare_args


class SntpServer:
    """Создает сокет SNTP-сервера, и начинает прослушивание."""
    def __init__(self, delay: int, port: int):
        """Инициализируйте сервер с указанной задержкой и портом."""
        self.delay = delay
        self.port = port
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.sock.bind(('localhost', self.port))
        self.thread_pool = ThreadPool(processes=10)

    def start_server(self) -> None:
        """Начинает прослушивать запросы клиентов и обрабатывать их."""
        print(f'Server started on port {self.port}')
        while True:
            data, address = self.sock.recvfrom(1024)
            self.thread_pool.apply_async(self.handle_request,
                                         args=(data, address))

    def handle_request(self, data: bytes, address: str) -> None:
        """Генерирует пакет временного ответа и отправляет обратно клиенту."""
        print(f'Client connected from {address[0]}')
        time = PackageGenerator.get_time(self.delay)
        response = PackageGenerator.get_sntp_packet(self.delay, data, time)
        self.sock.sendto(response + PackageGenerator.get_time(self.delay), address)


if __name__ == '__main__':
    args = prepare_args.prepare_args()
    sntp_Server = SntpServer(args.delay, args.port)
    sntp_Server.start_server()
