#!/usr/local/bin/python
import GetProcs

   
###################################################################

def iGetProcs():
    
    Retn = GetProcs.GetFirstProc()
    yield Retn
    
    while Retn:
        Retn = GetProcs.GetNextProc()
        if Retn:
            yield Retn

###################################################################

pids = {pid:value for pid,*value in iGetProcs()}
print(pids)
       
