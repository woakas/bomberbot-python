# -*- coding: utf-8 -*-
import socket


class BomberStandar():
    """ Bomberbot client Standart
    """

    def __init__(self, user, token, host, port):
        """
        Arguments:
        - `user`:
        - `token`:
        """
        self.sck = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.user = user
        self.token = token
        self._host = host
        self._port = port

    def login(self):
        self.sck.connect((self._host, self._port))
        if self.sck.recv(4096).endswith("Ingrese usuario y token:\r\n"):
            self.sck.send("%s,%s" % (self.user, self.token))
            return True
        else:
            return False

    def play(self):
        self.login()
        while True:
            pass


if __name__ == '__main__':
    b = BomberStandar()
    b.play()
