import sys
import os
import random

import num2words

import url_parser
import matplotlib.pyplot as plt

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../Partie-A')))
from random_fuzzer import RandomFuzzer
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../Partie-B')))
from mutation_fuzzer import MutationFuzzer
from my_fuzzer import MyFuzzer


class Coverage:
    def __init__(self):
        self.covered_lines = set()

    def trace(self, frame, event, arg):
        if event == "line":
            code = frame.f_code
            filename = code.co_filename
            lineno = frame.f_lineno
            self.covered_lines.add((filename, lineno))
        return self.trace

    def start(self):
        sys.settrace(self.trace)

    def stop(self):
        sys.settrace(None)

    def coverage(self):
        return self.covered_lines


def calculate_cumulative_coverage(input_population, function):
    cumulative_coverage = []
    all_coverage = set()

    for inp in input_population:
        coverage = Coverage()
        coverage.start()
        try:
            function(inp)
        except Exception:
            pass
        coverage.stop()
        all_coverage |= coverage.coverage()
        cumulative_coverage.append(len(all_coverage))
    return cumulative_coverage


# def plot(cumulative_coverage, label):
#     plt.plot(cumulative_coverage, label=label)
#     plt.title('Coverage')
#     plt.xlabel('# of inputs')
#     plt.ylabel('lines covered')
#     plt.show()
if __name__ == '__main__':
    # Exemple de couverture avec MutationFuzzer à modifier pour les tâches de la Partie-C
    # random.seed(2197269)
    random.seed(2195379)
    trials = 500
    fuzzerA = RandomFuzzer()
    fuzzerB = MutationFuzzer(seeds=["3452020"])
    fuzzerC = MyFuzzer()

    input_setA = [fuzzerA.fuzz() for _ in range(trials)]
    input_setB = [fuzzerB.fuzz() for _ in range(trials)]
    input_setC = [fuzzerC.fuzz() for _ in range(trials)]
    print(input_setA)
    print(input_setB)
    print(input_setC)
    cumulative_coverageA = calculate_cumulative_coverage(
        input_setA, num2words.num2words)
    cumulative_coverageB = calculate_cumulative_coverage(
        input_setB, num2words.num2words)
    cumulative_coverageC = calculate_cumulative_coverage(
        input_setC, num2words.num2words)
    plt.plot(cumulative_coverageA, label ="RandomFuzzer")
    plt.plot(cumulative_coverageB,label = "MutationFuzzer")
    plt.plot(cumulative_coverageC,label = "MyFuzzer")

    plt.legend()
    plt.title('Coverage')
    plt.xlabel('# of inputs')
    plt.ylabel('lines covered')
    plt.show()

