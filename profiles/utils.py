import random


def unique_id_generator():
    return ''.join(random.sample('0123456789', 5))
