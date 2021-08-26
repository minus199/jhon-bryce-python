@SET PATH=%PATH%;"C:\Python32"
@SET PYTHONPATH=C:\Python32\Lib

@ASSOC .py=Python.File
@ASSOC .pyc=Python.CompiledFile
@ASSOC .pyo=Python.CompiledFile
@ASSOC .pyw=Python.NoConFile

@FTYPE Python.CompiledFile="C:\Python32\python.exe" "%%1" %%*
@FTYPE Python.File="C:\Python32\python.exe" "%%1" %%*
@FTYPE Python.NoConFile="C:\Python32\pythonw.exe" "%%1" %%*
@SET PATHEXT=.py;%PATHEXT%