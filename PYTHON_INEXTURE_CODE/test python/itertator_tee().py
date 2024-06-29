from itertools import tee

use_case = "the iterators returned by the tee() can be used to feed the same set of data into multiple algorithms to be processed in parallel"
#created to push the iterators values into different algorithms
tee1, tee2 = tee(use_case, 2)

print(f"calling next on tee1: {next(tee1)}")  
print(f"calling next on tee2: {next(tee1)}")  
print(f"calling next on tee3: {next(tee1)}") 
print(f"calling next on tee3: {next(tee1)}") 
print(f"calling next on tee3: {next(tee1)}") 
print(f"calling next on tee4: {next(tee2)}")
print(f"calling next on tee5: {next(tee2)}")
print(f"calling next on tee6: {next(tee2)}")
print(f"calling next on tee7: {next(tee2)}") 