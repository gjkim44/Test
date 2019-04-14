v1 = 10
v2 = 5
decAnswer = None


class MathProcessor(object):


    @staticmethod
    def AddValues(value1, value2):
        return value1 + value2

    @staticmethod
    def SubtractValues(value1, value2):
        return value1 - value2

    @staticmethod
    def MultiplyValues(value1, value2):
        return value1 * value2

    @staticmethod
    def DivideValues(value1, value2):
        return value1 / value2

decAnswer = MathProcessor.AddValues(v1, v2),MathProcessor.SubtractValues(v1, v2),MathProcessor.MultiplyValues(v1, v2),MathProcessor.DivideValues(v1, v2)

print(str(decAnswer))