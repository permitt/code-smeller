import os
from argparse import ArgumentParser
import numpy as np
import tensorflow as tf

from config import Config
from interactive_predict import InteractivePredictor
from model import Model

from code_model import CodeModel


def extract_vector(model_path, input_file, file_index):
    args = ArgumentParser()
    args.load_path = model_path
    args.input_file = input_file
    args.file_index = file_index
    args.seed = 3
    args.data_path, args.save_path_prefix, args.release, args.test_path = [None] * 4

    label = input_file.split('/')[-2]       # label is the last folder's name
    name = input_file.split('/')[-1][:-4]   # remove .txt extension

    config = Config.get_default_config(args)

    np.random.seed(args.seed)
    tf.set_random_seed(args.seed)

    model = Model(config)
    predictor = InteractivePredictor(config, model)


    extracted_vector = predictor.predict(input_file)

    save_vector = CodeModel(name, label, extracted_vector)
    save_vector.save()

    model.close_session()


if __name__ == '__main__':
    DATA_PATH = '../data/MLCQ_long_method/'
    MODEL_PATH = '../models/java-large-model/model_iter52.release'

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


    none = {'label': 'none', 'data': []}
    for index, file in enumerate(os.listdir(path= DATA_PATH + none['label'])):
        print(index)

        input_file = DATA_PATH + none['label'] + '/' + file
        label = input_file.split('/')[-2]  # label is the last folder's name
        name = input_file.split('/')[-1][:-4]  # remove .txt extension

        if index == 1:
            model.config.FILE_INDEX = 1
            predictor.model = model

        if file[-3:] == 'txt':
            extracted_vector = predictor.predict(input_file)

            save_vector = CodeModel(name, label, extracted_vector)
            save_vector.save()



    model.close_session()


    minor = []
    major = []
    critical = []





