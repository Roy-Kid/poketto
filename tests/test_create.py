# author: Roy Kid
# contact: lijichen365@126.com
# date: 2022-03-27
# version: 0.0.1

"""
| User A
+---------+---------+---------+---------+---------+---------+---------+---------+
| name    | age     |
+---------+---------+---------+---------+---------+---------+---------+---------+
| Alice   | 14      |
| Bob     | 15      |
| Charlie | 16      |
| David   | 17      |
| Eve     | 18      |
| Frank   | 19      |

"""

import numpy as np
import pytest
from poketto import Model
import numpy.testing as npt

class TestCreate:
    
    @pytest.fixture(scope='class', name='userdata')
    def test_init(self, ):
        
        name = ['Alice', 'Bob', 'Charlie', 'David', 'Eve', 'Frank']
        age = np.array([14, 15, 16, 17, 18, 19])
        
        return name, age, 
    
    def test_class_style_init_with_field_name(self):

        pk = Model('users', ['name', 'age'])
        # pk = Model('users', 'name, age')
        assert 'name' in pk
        
    def test_class_style_init_with_kwargs(self, userdata):
        name, age = userdata
        pk = Model('users', name=name, age=age)
        assert pk['name'] == name
        npt.assert_equal(pk['age'], age)
        
    def test_class_style_init_with_dict(self, userdata):
        name, age = userdata
        fields = {
            'name': name,
            'age': age
        }
        pk = Model('users', **fields)
        assert pk['name'] == name
        npt.assert_equal(pk['age'], age)        
        
    def test_fromDict(self, userdata):
        
        name, age = userdata
        
    def test_fromNumpy(self, userdata):
        pass
    
    def test_fromModel(self, userdata):
        pass
        