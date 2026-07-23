class Memory:

    def __init__(self):
        self.data = []


    def save(self, text):
        self.data.append(text)


    def get(self):
        return self.data
