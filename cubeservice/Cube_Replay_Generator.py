import os
import random
from random import randint
import cPickle as pickle
import time


class Cube_File_Player(object):

    def __init__(self, scan_dir, avg_pulse_rate_sec, pulse_rate_tolerance_percent=0.05):
        self.time_low_sec = avg_pulse_rate_sec - avg_pulse_rate_sec * pulse_rate_tolerance_percent
        self.time_hi_sec = avg_pulse_rate_sec + avg_pulse_rate_sec * pulse_rate_tolerance_percent
        self.prediction_candidates = ['Parrot.Bebop', 'Matrice.100', 'Xiro', 'Unknown']

        self.file_corpus = self.__get_files_from_dir(scan_dir)
        if len(self.file_corpus) < 1:
            raise Exception("Not enough files in dir: {}".format(scan_dir))

    def __get_files_from_dir(self, folder):
        directory_contents = os.listdir(folder)
        path_list = []

        for item in directory_contents:
            abs_path = os.path.join(folder, item)
            if os.path.isfile(abs_path) and item.endswith("pickle"):
                path_list.append(abs_path)

        return path_list

    def __assign_ml_prediction(self):
        idx = randint(0, len(self.prediction_candidates) - 1)
        ml_class_prediction = self.prediction_candidates[idx]
        return ml_class_prediction

    def __load_random_cube(self, assigned_prediction):
        idx = randint(0, len(self.file_corpus) - 1)
        pickle_file = self.file_corpus[idx]
        cube = pickle.load(open(pickle_file, "rb"))
        cube['Prediction'] = assigned_prediction
        cube['Timestamp'] = time.time()
        return cube

    def get_next_sleep_time(self):
        yield random.uniform(self.time_low_sec, self.time_hi_sec)

    def receive_generated_cube(self):
        cube = self.__load_random_cube(self.__assign_ml_prediction())
        yield cube

if __name__ == '__main__':
    cube_gen = Cube_File_Player(scan_dir='/opt/cube_sessions/cube_captures/session_3DR_solo',
                                avg_pulse_rate_sec=1,
                                pulse_rate_tolerance_percent=0.05)

    samples_to_generate = 2000
    for i in range(samples_to_generate):
        cube = next(cube_gen.receive_generated_cube())
        cube_sleep = next(cube_gen.get_next_sleep_time())
        time.sleep(cube_sleep)
        print 'Received: {}'.format(cube['Prediction'])

