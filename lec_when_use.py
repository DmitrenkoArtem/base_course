from lec_module import b
from lec_import import b

print(b) #значение из последнего import

import lec_module as m
import lec_import_as as ia

print(m.b+ia.m.b)