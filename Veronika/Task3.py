class UserDict:
    def __init__(self, data):
        self.data = data
        self.history = []

    def set_value(self, key, value):
        self.data[key] = value
        if key in self.history:
            self.history.remove(key)
        self.history.append(key)
        if len(self.history) > 10:
            del self.history[0]

    def get_history(self):
        return self.history

d = UserDict({"foo": 42})
d.set_value("bar", 43)
print(d.get_history())
