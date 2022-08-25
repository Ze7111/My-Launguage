from backend.libraries.include import includeBase as inc
from backend.core.BFLib import bflib as bf
from backend.functions.Func import list_functions as lf
from backend.libraries.print import var_name as vprint
import time

ln: int = 0
fn: list
as_statements = []

def rbc(lines):
    global ln, fn, as_statements
    endw, startw = None, None
    func = None
    for line in lines:
        func = None
        if line.startswith('//'):
            pass; # skip comments
        #else: print(line); pass # IMPLMENT THIS FUNCTION LATER --------------------------------------------------------------
        if line.startswith('library'):
            as_statements = inc(line, ln)
        if line.startswith('func'):
            lf.cleanaddNameLine(line, ln)
        if line.startswith('cout'):
            color = True
            vprint(line, ln, as_statements, color)
        
        if line.startswith('out'):
            color = False
            vprint(line, ln, as_statements, color)
        else:
            pass
        
        bf(line)
        
        ln += 1
        
