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
        input_filename = self.config.INPUT_FILE
        print('Serving')
        while True:
            print('Reading the input file...')

            #user_input = ' '.join(self.read_file(input_filename))

            # try:
            #     predict_lines, pc_info_dict = self.path_extractor.extract_paths(user_input)
            # except ValueError:
            #     continue


            predict_lines, pc_info_dict = [None, None]

            predicted_lines = run(input_file_path)
            print(input_file_path + "OVO JE KOD \n\n\n\n")


            num_contexts = len(predicted_lines.split(' '))
            if(num_contexts <= self.config.DATA_NUM_CONTEXTS):
                predicted_lines = [predicted_lines.strip() + (' ' * (self.config.DATA_NUM_CONTEXTS - num_contexts + 1))]
            else:
                predicted_lines = [' '.join(predicted_lines.split(' ')[:self.config.DATA_NUM_CONTEXTS + 1])]

            model_results, extracted_vector = self.model.predict(predicted_lines)
            print(" JEBENI VEKTOR SAM DOBIO " + str(extracted_vector) + " \n\n\n\n\n\n\n\n\n\n\n")


            #prediction_results = Common.parse_results(model_results, pc_info_dict, topk=SHOW_TOP_CONTEXTS)
            # for index, method_prediction in prediction_results.items():
            #     print('Original name:\t' + method_prediction.original_name)
            #     if self.config.BEAM_WIDTH == 0:
            #         print('Predicted:\t%s' % [step.prediction for step in method_prediction.predictions])
            #         for timestep, single_timestep_prediction in enumerate(method_prediction.predictions):
            #             print('Attention:')
            #             print('TIMESTEP: %d\t: %s' % (timestep, single_timestep_prediction.prediction))
            #             for attention_obj in single_timestep_prediction.attention_paths:
            #                 print('%f\tcontext: %s,%s,%s' % (
            #                     attention_obj['score'], attention_obj['token1'], attention_obj['path'],
            #                     attention_obj['token2']))
            #     else:
            #         print('Predicted:')
            #         for predicted_seq in method_prediction.predictions:
            #             print('\t%s' % predicted_seq.prediction)

            return extracted_vector
        # RETURN VEC

