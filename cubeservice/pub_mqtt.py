import CubeSerializingSocket as css
import time
import logging
import Cube_Replay_Generator as replay


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


# Works on BSC1
# START ME 2nd
if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG)
    # dir_path = '/opt/cube_sessions/cube_captures/session_3DR_solo'  # BSC1
    dir_path = '/home/tj/z_to_slack/testdata'  # TJ laptop
    cube_gen = replay.Cube_File_Player(scan_dir=dir_path,
                                avg_pulse_rate_sec=1,
                                pulse_rate_tolerance_percent=0.05)
    cube_writer = css.CubeSerializingSocket()

    samples_to_generate = 2000
    for i in range(samples_to_generate):
        fake_cube = next(cube_gen.receive_generated_cube())
        cube_sleep = next(cube_gen.get_next_sleep_time())
        time.sleep(cube_sleep)
        logging.debug("Send cube: {}".format(fake_cube['Prediction']))
        cube_writer.send_zipped_cube(fake_cube)
