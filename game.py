from create_field import *
from field_tools import *
from ship import *

field = read_field('field.txt')
print(field)
print('----------')
print(field_to_str(field))
print('----------')
print(is_valid(field))