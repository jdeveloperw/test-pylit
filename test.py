from unittest import TestCase


class TestImports(TestCase):
  IMPORTS = ('file1', 'file2')

  class __metaclass__(type):

    def __new__(meta, classname, supers, classdict):

      for i in classdict['IMPORTS']:
        method =  lambda self: self.import_test(i)
        method_name = 'test_%s' % i
        method.__name__ = method_name 
        classdict[method_name] = method

      return type.__new__(meta, classname, supers, classdict)

  def __init__(self, blah):
    super(TestImports, self).__init__(blah)

  def import_test(self, name):
    __import__(name)
