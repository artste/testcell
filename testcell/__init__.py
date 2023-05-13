__version__ = "0.0.4"
# AUTOGENERATED! DO NOT EDIT! File to edit: ../nbs/02_testcell.ipynb.

# %% auto 0
__all__ = ['testcell', 'testcelln']

# %% ../nbs/02_testcell.ipynb 4
import ast
from IPython.core.magic import register_cell_magic, needs_local_scope
from IPython import get_ipython # needed for quarto

# %% ../nbs/02_testcell.ipynb 5
from .core import auto_display

# %% ../nbs/02_testcell.ipynb 6
@register_cell_magic
@needs_local_scope
def testcell(line, cell, local_ns):
    if not ('skipdisplay' in line): cell = auto_display(cell)
    lines = cell.splitlines()

    # Wrap inside a function
    ret = ['def _test_cell_():']
    ret += ['\t'+x for x in lines]
    ret += ['try:\n\t_test_cell_()'] # execute it!
    ret += ['finally:\n\tdel _test_cell_'] # delete it
    wrapped_cell = '\n'.join(ret)

    if ('verbose' in line) or ('dryrun' in line): print('\n### BEGIN\n'+wrapped_cell+'\n### END')

    _globals = {} if ('noglobals' in line) else local_ns
    if not 'dryrun' in line: exec(wrapped_cell,_globals)

    if 'return_wrapped_cell' in line: return line, wrapped_cell
    else: pass

# %% ../nbs/02_testcell.ipynb 9
@register_cell_magic
@needs_local_scope
def testcelln(line, cell, local_ns):
    return testcell(line=line+ ' noglobals', cell=cell, local_ns=local_ns)
