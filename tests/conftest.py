# author: Roy Kid
# contact: lijichen365@126.com
# date: 2022-03-27
# version: 0.0.1
import pytest
import numpy as np

from poketto.model import Poketto

@pytest.fixture(scope='class', name='userdata')
def test_init():
    
    name = ['Alice', 'Bob', 'Charlie', 'David', 'Eve', 'Frank']
    age = np.array([14, 15, 16, 17, 18, 19])
    
    pk = Poketto('users', name=name, age=age)
    
    return pk