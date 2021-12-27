#python3

# Closely follows the tutorial at
# https://iximiuz.com/ru/posts/writing-python-web-server-part-3/
# No copyright infringment intended :)
# I add some comments / references to make things look more clear

import socket # low-level networking interface (as per documentation)
import sys    # to run the script with parameters (sys.args[])

MAX_LINE = 64*1024

class MyHTTPServer:

    def __init__(self, host, port, server_name):
        self._host = host
        self._port = port
        self._server_name = server_name

    def serve_forever(self):
        serv_sock = socket.socket(
            socket.AF_INET,     # IPv4
            socket.SOCK_STREAM, # TCP
            proto = 0)
        try:
            serv_sock.bind((self._host, self._port)) #method accepts tuple, not str (https://stackoverflow.com/questions/48651321/)
            serv_sock.listen()
            while True:
 #               conn, _ = serv_sock.accept()    # tutorial ignores second return parameter
                conn, addr = serv_sock.accept() # as per documentation second return parameter is 'client address'
                print(addr)                     # let's check
                try:
                    self.serve_client(conn) # custom class method, see below
                except Exception as e:
                    print("Client serving failed", e)
        finally: # this is to close the connection if something goes wrong 
            serv_sock.close()

    def serve_client(self, conn):
        try:
            req = self.parse_request(conn)
            resp = self.handle_request(conn)
            self.send_reponse(conn, resp)
        except ConnectionResetError: # 'connection reset by peer' ??
            conn = None
        except Exception as e:
            self.send_error(conn, e)

    def parse_request(self, conn):
        rfile = conn.makefile('rb') # r - read mode, b - binary format
        raw = rfile.readline(MAX_LINE + 1) # first line of the request
        if len(raw) > MAX_LINE:
            raise Exception('Line is too long')

        req_line = str(raw, 'iso-8859-1')  # extended ASCII format
        req_line = req_line.rstrip('\r\n') # remove CR LF characters (line break as per HTTP spec)
        words = req_line.split() # list of words separated by blank fields
        if len(words) != 3: # has to include exactly (1) HTTP method (2) URL (3) HTTP version
            raise Exception("Malformed request start line")

        method, target, ver = words
        if ver != 'HTTP/1.1':
            raise Exception("Unexpectet HTTP version")

        return Requests(method, target, ver, rfile)

    def handle_request(self, req):
    # TODO : https://iximiuz.com/ru/posts/writing-python-web-server-part-3/    
        pass

    def send_reponse(self, conn, resp):
        pass

    def send_error(self, conn, err):
        pass

class Request:
    def __init__(self, method, target, ver, rfile):
        self.method = method
        self.target = target
        self.ver = ver
        self.rfile = rfile


def main():
    host = sys.argv[1]
    port = int(sys.argv[2])
    server_name = sys.argv[3]

    serv = MyHTTPServer(host, port, server_name)
    try:
        serv.serve_forever()
    except KeyboardInterrupt:
        pass

if __name__ == "__main__":
    main()