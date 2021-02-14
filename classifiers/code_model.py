import pickle


class CodeModel:
    PATH_DATA = '../data/'

    def __init__(self, name, label, vector, folderName):
        self.vector = vector
        self.name = name
        self.label = label
        self.PATH = self.PATH_DATA + "/" + folderName

    """
        Saved file example path: data/INPUT/major/38568.pickle
    """
    def save(self):
        with open(f'{self.PATH}{self.label}/{self.name}.pickle', 'wb+') as f:
            pickle.dump(self, f, pickle.HIGHEST_PROTOCOL)
        print(f'Saved file successfully as {self.name}.pickle')

    def get_vector(self):
        return self.vector