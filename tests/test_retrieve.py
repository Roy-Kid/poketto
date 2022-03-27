# author: Roy Kid
# contact: lijichen365@126.com
# date: 2022-03-27
# version: 0.0.1

import pytest
import numpy as np
import numpy.testing as npt

from poketto.model import Poketto


class TestRetrieve:
    
    def test_get_field_by_attribute(self, userdata):
        pk = userdata
        name = pk.name
        assert (name == ['Alice', 'Bob', 'Charlie', 'David', 'Eve', 'Frank']).all()
        
    def test_get_field_by_getitem(self, userdata):
        pk = userdata
        name = pk['name']
        assert (name == ['Alice', 'Bob', 'Charlie', 'David', 'Eve', 'Frank']).all()
        
    def test_get_record_by_index(self, userdata):
        pk = userdata
        record = pk[0]
        assert record['name'] == 'Alice'
        assert record.name == 'Alice'
        
    def test_get_record_by_slice(self, userdata):
        pk = userdata
        record = pk[:3]
        assert record.name == ['Alice', 'Bob', 'Charlie']
        record = pk[::2]
        assert record.name == ['Alice', 'Charlie', 'Eve']
        
    def test_get_record_by_bool(self, userdata):
        pk = userdata
        record = pk[pk.age > 16]
        assert record.name == ['Charlie', 'David', 'Eve']
        
        