import random


class MyFuzzer:

    def _getRandomBool(self):
        # return (random.randint(0,1))
        return random.choice([True,False, False, False, True, False, False, False, False])
    def _getNumberString(self):
        return str(random.randint(0, 9))
    def fuzz(self):
        string = ""
        for i in range(10):
            if (self._getRandomBool()):
               string = string + ","
            elif(self._getRandomBool()):
                string =string+ "."
            string = string + self._getNumberString()
        return string


