import socket
import time
import configparser


class Server:
    def __init__(self, settings='settings.ini'):
        self.time_mistake = Server._get_time_mistake(settings)
        self.ip = 'localhost'
        self.port = 123
        self._count_read = 1024
        self._time_out = 0.1

    @staticmethod
    def _get_time_mistake(filename='settings.ini'):
        _config = configparser.ConfigParser(default_section='')
        _config.optionxform = str
        _config.read(filename, encoding='utf8')
        return int(_config['DELTA']['seconds'])

    def start(self):
        with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as sock:
            sock.bind((self.ip, self.port))
            sock.settimeout(self._time_out)
            while True:
                try:
                    request, address = sock.recvfrom(self._count_read)
                    response = time.time() + self.time_mistake
                    sock.sendto(str(response).encode(), address)
                except socket.timeout:
                    pass


if __name__ == '__main__':
    Server().start()
