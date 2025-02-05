
import sciunit
from sciunit import Capability
import multiprocessing


class NumOfPossibleLocations(sciunit.Capability):
    """ Provides the number of available locations (segments in NEURON) in a section list"""

    def num_of_possible_locations(self):
        
        raise NotImplementedError()

    def get_num_of_possible_locations(self, serialized = False):
        """ Used to keep all NEURON related tasks in independent processes, to avoid errors like 'template can not be redefined', gives an option to be excuted in parallel or serially"""
        if serialized:
            return self.num_of_possible_locations()
        else:
            pool_ = multiprocessing.Pool(1, maxtasksperchild = 1)
            num = pool_.apply(self.num_of_possible_locations)
            pool_.terminate()
            pool_.join()
            del pool_
            return num
