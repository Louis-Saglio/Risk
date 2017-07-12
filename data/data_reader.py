class Iterateur:

    def __init__(self):
        self.prefix = []
        self.rep = []

    def flattern(self, data, rep=None):
        if rep is None:
            rep = []
        for i in data:
            if hasattr(i, '__iter__') and not isinstance(i, str):
                self.flattern(i, rep)
            else:
                rep.append(i)
        return tuple(rep)

    def iter_dico(self, dico: dict):
        for key, d in dico.items():
            self.prefix.append(key)
            if isinstance(d, dict):
                self.iter_dico(d)
            elif isinstance(d, tuple):
                for t in d:
                    self.rep.append((*self.prefix, *t))
                self.prefix.pop(-1)
        if self.prefix:
            self.prefix.pop(-1)
        for i in range(len(self.rep)):
            self.rep[i] = self.flattern(self.rep[i])
        return self.rep


def serialize(data):
    i = Iterateur()
    return i.iter_dico(data)


def dump_data(data):
    if isinstance(data, dict):
        data = serialize(data)
    rep = []
    for a in data[1::]:
        rep.append({})
        for i in range(len(a)):
            key = data[0][i]
            rep[-1][key] = a[i]
    return rep


def create_objects_from_data(data, klass: type):
    rep = []
    for dico in dump_data(data):
        rep.append(klass(**dico))
    return rep
