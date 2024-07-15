from my_package import module1, module2

print(module1.function1())
print(module2.function2())

'''
You can also use the import statement to import specific functions from the modules within the package:

from my_package.module1 import function1
from my_package.module2 import function2

Packages allow you to create a nested structure for your code, making it easier to manage large projects.

my_project/
    __init__.py
    module1.py
    module2.py
    sub_package/
        __init__.py
        sub_module1.py
        sub_module2.py

from my_project import module1, module2
from my_project.sub_package import sub_module1, sub_module2

Relative imports use a dot (.) notation:

Single dot (.) refers to the current package.
Double dots (..) refer to the parent package.
Triple dots (...) refer to the grandparent package, and so on.

'''