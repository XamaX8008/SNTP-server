import datetime
import struct

TIME = datetime.datetime(1900, 1, 1)


class PackageGenerator:
    """Генерирует данные о времени отправки SNTP-пакета."""
    @staticmethod
    def get_sntp_packet(delay: int, packet: bytes, receive_time: struct) -> struct:
        """Генерирует ответный пакет SNTP."""
        return struct.pack('!B', 28) + struct.pack('!B', 1) \
            + struct.pack('!b', 0) + struct.pack('!b', -20) + struct.pack('!i',0) \
            + struct.pack('!i', 0) + struct.pack('!i', 0) \
            + PackageGenerator.get_time(delay) + packet[40:48] + receive_time

    @staticmethod
    def get_time(delay: int) -> struct:
        """Возвращает текущее время с заданной задержкой."""
        time = (datetime.datetime.utcnow() - TIME).total_seconds() + delay
        seconds, milliseconds = [int(x) for x in str(time).split('.')]
        return struct.pack('!II', seconds, milliseconds)
