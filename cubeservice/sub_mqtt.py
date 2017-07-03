import os
import CubeSerializingSocket as css
import time
import Cube_Wrapper as group_key


# ========================================================================
# Ubuntu 14.04 Mosquitto Install Requirements
# ========================================================================
# Need the mosquitto server installed
# Start the mosquitto server
#
# sudo apt-add-repository -y ppa:mosquitto-dev/mosquitto-ppa
# sudo apt-get update
# sudo apt-get install -y mosquitto mosquitto-clients
# ========================================================================

def on_recv(topic, cube):
    # print 'GOT A CUBE: Topic: {}, Cube: {}'.format(topic, cube['Prediction'])
    gk = group_key.get_group_key(cube)
    print 'Received: Topic: {}, Group Key: {}'.format(topic, gk)

# START ME 1st
# Works on BSC1
if __name__ == '__main__':
    print 'Listening on MQTT for all cubes'
    cube_sub = css.CubeSerializingSocket(on_recv)

    while True:
        time.sleep(0.5)
        # print "Try to read a cube and process with callback..."

