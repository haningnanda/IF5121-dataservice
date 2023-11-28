def serialize(x):
    if type(x) == list:
        return [i.serialize() for i in x]
    return x.serialize()