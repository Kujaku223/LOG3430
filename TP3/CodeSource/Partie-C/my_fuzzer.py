import random

class MyFuzzer:

    def _get_random_bool(self, true_weight=1, false_weight=9):
        return random.choices([True, False], weights=[true_weight, false_weight])[0]

    def _get_number_string(self):
        return str(random.randint(0, 9))

    def fuzz(self):
        string = ""
        dot_used = False

        if self._get_random_bool():
            string += "-"

        for i in range(random.randint(1, 20)):
            if self._get_random_bool(true_weight=1, false_weight=15):
                if not dot_used and self._get_random_bool(true_weight=1, false_weight=4):
                    string += "."
                    dot_used = True
                else:
                    string += ","

            string += self._get_number_string()

        if string[-1] in [",", "."]:
            string = string[:-1]

        return string