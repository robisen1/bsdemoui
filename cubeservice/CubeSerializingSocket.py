import cPickle
import zlib
from paho.mqtt.client import Client as MqttClient
import time
import logging


class CubeSerializingSocket(object):

    CUBE_TOPIC_NAME = 'RawCubes'

    def __init__(self, on_receive_cube_fn=None):
        self.on_receive_cube_fn = on_receive_cube_fn

        # https://www.infoq.com/articles/practical-mqtt-with-paho
        self.mqtt_client = MqttClient()

        if self.on_receive_cube_fn is not None:
            def on_connect(client, userdata, flags, rc):
                self.mqtt_client.subscribe(CubeSerializingSocket.CUBE_TOPIC_NAME)
            self.mqtt_client.on_connect = on_connect
            self.mqtt_client.message_callback_add(CubeSerializingSocket.CUBE_TOPIC_NAME, self.receive_zipped_cube)

        self.mqtt_client.connect('127.0.0.1')
        self.mqtt_client.loop_start()

    def send_zipped_cube(self, cube_dict):
        dict = cPickle.dumps(cube_dict, protocol=cPickle.HIGHEST_PROTOCOL)
        dict = zlib.compress(dict)
        logging.debug("SEND Cube: Topic: {}".format(CubeSerializingSocket.CUBE_TOPIC_NAME))
        return self.mqtt_client.publish(CubeSerializingSocket.CUBE_TOPIC_NAME, bytearray(dict))

    def receive_zipped_cube(self, client, userdata, msg):
        data = msg.payload
        pobj = zlib.decompress(data)
        pobj = cPickle.loads(pobj)
        self.on_receive_cube_fn(msg.topic, pobj)
