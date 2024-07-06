#!/usr/bin/env python3
''' Description: Accepts a string k and an int OR float v as arguments and
                 returns a tuple. The first element of the tuple is the
                 string k.
                 The second element is the square of the int/float v and
                 should be annotated as a float.
    Parameters: k: str, v: Union[int, float]
'''

from typing import Tuple, Union


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    ''' return a tuple '''
    return (k, v * v)
