import socket
import time
import _thread

import display_engine
from machine import Pin
from movements import Movements
from wifi_connectivity import Wifi


class Router:
    def __init__(self):
        Wifi()

    def start_server_service(self, s):
        while True:
            display_engine.open_eyes()
            time.sleep(1)
            display_engine.close_eyes()
            time.sleep(1)

            cl, addr = s.accept()
            print("Client connected from", addr)
            request = cl.recv(1024).decode()
            print("Request:", request)

            # Basic routing
            if "GET /status" in request:
                response = '{"status": "ok"}'
            elif "GET /default" in request:
                display_engine.open_eyes()
                Movements().set_to_default_positions()
            elif "GET /standup" in request:
                display_engine.open_eyes()
                Movements().set_to_standing_position()
            elif "GET /sitdown" in request:
                display_engine.open_eyes()
                Movements().set_to_sit_down_position()
            elif "GET /forward" in request:
                display_engine.open_eyes()
                Movements().set_to_move_forward()
            else:
                response = '{"error": "not found"}'

            cl.send("HTTP/1.1 200 OK\r\nContent-Type: application/json\r\n\r\n")
            cl.send(response)
            cl.close()

    def start_server(self):

        addr = socket.getaddrinfo("0.0.0.0", 80)[0][-1]
        s = socket.socket()
        s.bind(addr)
        s.listen(1)
        print("Listening on", addr)
        Movements().set_to_default_positions()
        _thread.start_new_thread(self.start_server_service(s), ())
        _thread.start_new_thread(display_engine.blink_eye(), ())
