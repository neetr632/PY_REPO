print("""
Module Search Path Process:

Built-in Modules: 
Python first searches for a built-in module with the name module_name. These modules are part of the Python Standard Library and are always available.

sys.path:
If Python does not find a built-in module, it searches for a module in directories specified by sys.path. sys.path is a list of strings that specifies the directories to be searched for modules. It typically includes the following locations

:- The directory containing the script that is being executed.
:- The directories listed in the PYTHONPATH environment variable (if set).
:- Default system directories that Python is installed in.""")