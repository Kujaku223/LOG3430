import random


class MyFuzzer:

    def _getRandomBool(self):
        # return (random.randint(0,1))
        return random.choice([True,False, False, False, False, False, False, False, False])
    def _getNumberString(self):
        return str(random.randint(0, 9))
    def fuzz(self):
        string = ""
        dotBool = True
        for i in (random.randint(0,20)):
            if (self._getRandomBool() and dotBool):
               string = string + ","
            elif(self._getRandomBool() and dotBool):
                string =string+ "."
                dotBool = False
            string = string + self._getNumberString()
        return string


