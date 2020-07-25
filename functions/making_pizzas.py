'''
To call a function from an imported model,enter the name of the module you imported.
import module
this way import all of the fuctions in module
and each function in the module is available through the following syntax:
module_name.function_name()

importing specific functions
from module_name import function_name  #one function
from module_name import function_0,function_1,function_2 #several functions
if  you use this way,you donot need to use the dot notation when you call a function
and directly use with function()
'''

'''
using as to give a function an alias
the as keyword renames a function using the alias you provide
from module_name import function_name as fn
'''

'''
using as to give a module as alias
import module_name as mn
'''
'''
importing all functions in a module
from module_name import *
'''

'''
import module_name
from module_name import function_name
from module_name import function1,function2,function3
from module_name import fuction_name as fn
imort module_name as mn
from module import *
'''

import pizza_1
pizza_1.make_pizza(16,'pepproni')
pizza_1.make_pizza(12,'mushroom','green peppers','extra cheese')

from pizza import make_pizza
make_pizza(16,'pepproni')
make_pizza(12,'mushroom','green peppers','extra cheese')

from pizza import make_pizza as mp
mp(16,'pepproni')
mp(12,'mushroom','green peppers','extra cheese')

import pizza as p
p.make_pizza(16,'pepproni')
p.make_pizza(12,'mushroom','green peppers','extra cheese')

from pizza import *
make_pizza(16,'pepproni')
make_pizza(12,'mushroom','green peppers','extra cheese')