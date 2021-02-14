import os
from argparse import ArgumentParser
import numpy as np
import tensorflow as tf
import time
from config import Config
from interactive_predict import InteractivePredictor
from model import Model

from code_model import CodeModel

DATA_PATH = '../data/MLCQ_long_method/'
DATA_PATH_GC = '../data/MLCQ_god_class/'
MODEL_PATH = '../models/java-large-model/model_iter52.release'


def init_predictor() -> (InteractivePredictor, Model):
    args = ArgumentParser()
    args.load_path = MODEL_PATH
    args.input_file = ''
    args.file_index = 0
    args.seed = 3
    args.data_path, args.save_path_prefix, args.release, args.test_path = [None] * 4

    config = Config.get_default_config(args)

    np.random.seed(args.seed)
    tf.set_random_seed(args.seed)

    model = Model(config)
    predictor = InteractivePredictor(config, model)

    return predictor, model


def parse_long_method():
    predictor, model = init_predictor()
    label = 'none'   # label and folder name at the same time
    for index, file in enumerate(os.listdir(path=DATA_PATH + label)):
        print(index)

        input_file = DATA_PATH_GC + label + '/' + file
        name = input_file.split('/')[-1][:-4]  # remove .txt extension

        if index == 1:
            model.config.FILE_INDEX = 1
            predictor.model = model

        if file[-3:] == 'txt':
            extracted_vector = predictor.predict(input_file)
            save_vector = CodeModel(name, label, extracted_vector, "god_class")
            save_vector.save()

    model.close_session()


def parse_god_class():
    predictor, model = init_predictor()
    # ostao ti je, tj pukao na minor
    label = 'none'
    for index, file in enumerate(os.listdir(path=DATA_PATH_GC + label)):
        print(index)
        temp_file = DATA_PATH_GC + "temp.txt"  # path to file where each method will be written
        input_file = DATA_PATH_GC + label + '/' + file
        name = input_file.split('/')[-1][:-4]  # remove .txt extension

        if index == 1:
            model.config.FILE_INDEX = 1
            predictor.model = model

        if file[-3:] == 'txt':
            # isparsiras odje metodu u neki temp fajl i njega prosledjujes sve dok ne zavrsis s klasom.
            with open(input_file, "r") as class_file:
                next(class_file)  # skip first line

                methodString = ""
                brackets = 0
                vectors = []
                for line in class_file:
                    if line.strip()[-1:] == "{" and brackets == 0:
                        methodString = line
                        brackets += 1
                    elif line.strip()[-1:] == "{" and "}" not in line:
                        methodString += line
                        brackets += 1
                    elif line.strip()[-1:] == "}" and brackets == 1:
                        methodString += line
                        with open(temp_file, "w") as write_file:
                            write_file.write(methodString)
                        vector = np.array(predictor.predict(temp_file))
                        if not np.isnan(vector[0][0]):
                            vectors.append(vector)
                        brackets = 0
                    elif "}" in line and "{" in line:
                        methodString += line
                    elif "}" in line and "{" not in line:
                        methodString += line
                        brackets -= 1
                    elif brackets > 0:
                        methodString += line


                np_vectors = np.array(vectors)
                mean_vector = np.mean(np_vectors, axis=0)
                save_vector = CodeModel(name, label, mean_vector, "god_class")
                save_vector.save()

    model.close_session()


if __name__ == '__main__':
    start_time = time.time()
    # parse_long_method()
    parse_god_class()
    print("--- %s seconds ---" % (time.time() - start_time))

