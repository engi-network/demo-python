import os

# an example of a secret env var loaded from .env encrypted using git secrets
print("KEY={}".format(os.environ["KEY"]))


def add(x, y):
    return x + y


def sub(x, y):
    return y - x
