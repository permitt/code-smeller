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
    extracted_vector = predictor.predict()

    save_vector = CodeModel(name, label, extracted_vector)
    save_vector.save()

    model.close_session()


if __name__ == '__main__':
    DATA_PATH = '../data/MLCQ_long_method/'
    MODEL_PATH = '../models/java-large-model/model_iter52.release'

    none = {'label':'none', 'data': []}
    for index, file in enumerate(os.listdir(path= DATA_PATH + none['label'])):
        print(index)
        extract_vector(MODEL_PATH, DATA_PATH + none['label'] + '/' + file, index) if file[-3:] == 'txt' else None


    minor = []
    major = []
    critical = []





    # parser = ArgumentParser()
    # parser.add_argument("-d", "--data", dest="data_path",
    #                     help="path to preprocessed dataset", required=False)
    # parser.add_argument("-te", "--test", dest="test_path",
    #                     help="path to test file", metavar="FILE", required=False)
    #
    # parser.add_argument("-s", "--save_prefix", dest="save_path_prefix",
    #                     help="path to save file", metavar="FILE", required=False)
    # parser.add_argument("-l", "--load", dest="load_path",
    #                     help="path to saved file", metavar="FILE", required=False)
    # parser.add_argument('--release', action='store_true',
    #                     help='if specified and loading a trained model, release the loaded model for a smaller model '
    #                          'size.')
    # parser.add_argument('--predict', action='store_true')
    # parser.add_argument('--debug', action='store_true')
    # parser.add_argument('--seed', type=int, default=239)
    # args = parser.parse_args()
    #
    # np.random.seed(args.seed)
    # tf.set_random_seed(args.seed)
    #
    # if args.debug:
    #     config = Config.get_debug_config(args)
    # else:
    #     config = Config.get_default_config(args)
    #
    # model = Model(config)
    # print('Created model')
    # if config.TRAIN_PATH:
    #     model.train()
    # if config.TEST_PATH and not args.data_path:
    #     results, precision, recall, f1, rouge = model.evaluate()
    #     print('Accuracy: ' + str(results))
    #     print('Precision: ' + str(precision) + ', recall: ' + str(recall) + ', F1: ' + str(f1))
    #     print('Rouge: ', rouge)
    # if args.predict:
    #     predictor = InteractivePredictor(config, model)
    #     predictor.predict()
    # if args.release and args.load_path:
    #     model.evaluate(release=True)
    # model.close_session()


