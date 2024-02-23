import os
import marshal
import types

real_path = os.path.dirname(os.path.realpath(__file__))
pyc = open((real_path)+'/docs/lib.cpython-310.pyc', 'rb').read()
code = marshal.loads(pyc[16:])
module = types.ModuleType('module_name')
exec(code, module.__dict__)

module.function()

return_val = module.function2()
#print(return_val)