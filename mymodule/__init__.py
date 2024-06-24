# /usr/bin/env python

__author_ = ['Dev One', 'Contrib Two']
__version__ = '0.9'
__date__ = '2024-06-22'
__citation__ = """
% If this work is used to support a publication please
% cite the following publication:
% Description of This code
@ARTICLE{ExcellentCode_2022, 
   author = { {One}, D. and {Two}, C. and {People}, O},
    title = "{Awesome sauce code for astronomy projects}",
  journal = {Nature},
 keywords = {techniques: image processing, catalogues, surveys},
     year = 2021,
    month = may,
   volume = 1337,
    pages = {11-15},
      doi = {some.doi/link.in.here}
} 

% It is also appropriate to link to the following repository: https://github/com/devone/AwesomeSauce
"""

print("Hello from module 'mymodule'")

def func():
    print("You just ran the function called `func` from module `mymodule'")

__all__ = ['sky_sim']

from mymodule import sky_sim
