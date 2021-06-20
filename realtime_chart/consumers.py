from channels.generic.websocket import WebsocketConsumer
import json
import threading
import time
import random

from socket import socket, AF_INET, SOCK_DGRAM


class SensorConsumer(WebsocketConsumer):

    def connect(self):
        self.accept()
        self.start_publish()

    def disconnect(self, close_code):
        self.stop_publish()

    def start_publish(self):
        self.publishing = True
        self.t = threading.Thread(target=self.publish)
        self.t.start()

    def stop_publish(self):
        self.publishing = False
        self.t.join()

    def publish(self):
        # UDPの設定
        HOST = ''   
        PORT = 4001

        s = socket(AF_INET, SOCK_DGRAM)
        s.bind((HOST, PORT))

        while True:
            # センサーからUDPでデータを受信
            msg, address = s.recvfrom(8192)

            t = int(float(msg.decode('utf-8').split('\t')[0]))
            x = float(msg.decode('utf-8').split('\t')[-1].split(',')[1])
            y = float(msg.decode('utf-8').split('\t')[-1].split(',')[2])
            z = float(msg.decode('utf-8').split('\t')[-1].split(',')[3])

            # Websocketで送信
            if self.publishing == False:
                break
            self.send(text_data=json.dumps([
                {'time': t,'y': x,},
                {'time': t,'y': y,},
                {'time': t,'y': z,},
                ]))

        s.close()
