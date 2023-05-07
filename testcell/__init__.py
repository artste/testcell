__version__ = "0.0.1"
# AUTOGENERATED! DO NOT EDIT! File to edit: ../nbs/02_testcell.ipynb.

# %% auto 0
__all__ = ['testcell']

# %% ../nbs/02_testcell.ipynb 4
import ast
from IPython.core.magic import register_cell_magic
from IPython import get_ipython # needed for quarto

# %% ../nbs/02_testcell.ipynb 5
from .core import auto_display

# %% ../nbs/02_testcell.ipynb 6
@register_cell_magic
def testcell(line, cell):
    if not ('skipdisplay' in line): cell = auto_display(cell)
    lines = cell.splitlines()
    
    # Wrap inside a function
    ret = ['def _test_cell_():']
    ret += ['\t'+x for x in lines]
    ret += ['try:\n\t_test_cell_()'] # execute it!
    ret += ['finally:\n\tdel _test_cell_'] # delete it
    wrapped_cell = '\n'.join(ret)
    
    if ('verbose' in line) or ('dryrun' in line): print('\n### BEGIN\n'+wrapped_cell+'\n### END')
    if not 'dryrun' in line: exec(wrapped_cell)
    
    if 'return_wrapped_cell' in line: return line, wrapped_cell
    else: pass
