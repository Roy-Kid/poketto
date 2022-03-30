# author: Roy Kid
# contact: lijichen365@126.com
# date: 2022-03-27
# version: 0.0.1

import numpy as np
from functools import reduce
from typing import Optional
from numpy import ndarray

np.recarray

class Model:
    
    def __init__(self, structName_, field_names=None, **fields):
        
        
        self._structName = structName_
        
        # pre-process `field_names``
        if isinstance(field_names, str):
            field_names = field_names.split(',')
        elif field_names is None:
            field_names = []
            
        self._fields = fields
        
        for name in field_names:
            self._fields[name] = None
        
    @property
    def structName(self):
        return self._structName
    
    @property
    def fields(self):
        return self._fields
        
    @property    
    def dtype(self):
        tmp = []
        for k, v in self._fields.items():
            if isinstance(v, np.ndarray):
                if v.ndim == 1:
                    tmp.append( (k, v.dtype) ) 
                else:
                    tmp.append( (k, v.dtype, v.shape[1:]) )
            else:
                t = type(v[0])
                if t == str:
                    t = 'U16'
                tmp.append( (k, t) )
                
        return np.dtype(tmp)
    
    @classmethod
    def fromDict(cls, structName_, fields:dict):
        return cls(structName_, fields)
    
    @classmethod
    def fromModel(cls, structName_, model):
        return cls(structName_, **model.fields)
    
    @classmethod
    def fromNumpy(cls, structName_, arr):
        
        arrDict = {}
        for field in arr.dtype.fields:
            arrDict[field] = arr[field]
        return cls(structName_, **arrDict)
        
    def __getitem__(self, key):
        
        if isinstance(key, str):
            return self._fields[key]
        elif isinstance(key, (int, slice, ndarray)):
            arr = self.toNumpy()
            return Model.fromNumpy(self.structName, arr[key])
        
    def __repr__(self):
        return f'<{self.__class__.__name__} {self.name} with len {len(self)}>'
    
    def __contains__(self, field_name):
        return field_name in self._fields
        
    def isAlign(self, fields:Optional[dict]=None):
        
        if fields is None:
            fields = self._fields.values()
                
        field_lengths = np.asarray(tuple(map(len, fields)))
        if (field_lengths == 0).all():
            return True
        elif (field_lengths == 0).any():
            return False
         
        field_lengths -= np.max(field_lengths)
        field_lengths = field_lengths.astype(np.bool_)
        if ~field_lengths.all():
            return True
        return False
    
    def toNumpy(self):
        
        arrs = self._fields.values()
        lengths = map(len, arrs)
        maxLen = max(lengths)

        data = np.empty((maxLen, ), dtype=self.dtype)
        for key in self._fields.keys():
            data[key] = self._fields[key]

        return data 
    
    def toDict(self):
        
        return self._fields
    
    