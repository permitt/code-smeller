from common import Common
from extractor import Extractor

import sys

sys.path.append('./JavaExtractor/')

from extract import run

SHOW_TOP_CONTEXTS = 10
MAX_PATH_LENGTH = 80
MAX_PATH_WIDTH = 2
EXTRACTION_API = 'https://po3g2dx2qa.execute-api.us-east-1.amazonaws.com/production/extractmethods'


class InteractivePredictor:
    exit_keywords = ['exit', 'quit', 'q']

    def __init__(self, config, model):
        model.predict([])
        self.model = model
        self.config = config
        self.path_extractor = Extractor(config, EXTRACTION_API, self.config.MAX_PATH_LENGTH, max_path_width=2)

    @staticmethod
    def read_file(input_filename):
        with open(input_filename, 'r') as file:
            return file.readlines()

    def predict(self, input_file_path):

        # try:
        #     predict_lines, pc_info_dict = self.path_extractor.extract_paths(user_input)
        # except ValueError:
        #     continue

        predicted_lines = run(input_file_path)

        num_contexts = len(predicted_lines.split(' '))
        if (num_contexts <= self.config.DATA_NUM_CONTEXTS):
            predicted_lines = [predicted_lines.strip() + (' ' * (self.config.DATA_NUM_CONTEXTS - num_contexts + 1))]
        else:
            predicted_lines = [' '.join(predicted_lines.split(' ')[:self.config.DATA_NUM_CONTEXTS + 1])]

        model_results, extracted_vector = self.model.predict(predicted_lines)
        print("VEKTOR KODA " + str(extracted_vector) + " \n\n\n\n\n\n\n\n\n\n\n")

        return extracted_vector
