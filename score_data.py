class ScoreData:

    @staticmethod
    def save(value):
        file = open("score_data.txt", "w")
        try:
            file.write(str(value))
        finally:
            file.close()

    @staticmethod
    def load():
        file = open("score_data.txt", "r")
        try:
            result = int(file.read())
        finally:
            file.close()
        return result
