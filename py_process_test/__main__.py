import unittest
import yaml
from os import path
from py_process.core import *

process = Process()

def loadConfig(path):
    with open(path, 'r') as stream:
        try:
            data = yaml.safe_load(stream)
            _keys=data['Process']
            for _key in _keys:
                process.addSpec(_key,_keys[_key]) 
        except yaml.YAMLError as exc:
            print(exc)
        except Exception as ex:
            print(ex) 

dir_path = path.dirname(path.realpath(__file__))
loadConfig(path.join(dir_path,'data/bpm01.yml'))

class TestProcess(unittest.TestCase):
    def test_simple(self):
        context = {"a":2,"b":5}
        instance = process.create('bpm01',context)
        process.start(instance,sync=True)
        self.assertEqual(context['a'],7)


unittest.main()
