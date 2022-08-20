# from testpack.he import *  # work  A.hello() with nothing in __init__.py
import testpack  # work  testpack.he.A.hello() with     from testpack import he    in   __init__.py
from testmodule import *  # work

testpack.he.A.hello()
printJojo()
