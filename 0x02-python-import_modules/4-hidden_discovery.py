#!/usr/bin/python3
if __name__ == "__main__":
    import hidden_4
    defined = []
    for w in dir(hidden_4):
        if not w.startswith('__'):
            defined.append(w)
    defined.sort()
    for w in defined:
        print("{:s}".format(w))
