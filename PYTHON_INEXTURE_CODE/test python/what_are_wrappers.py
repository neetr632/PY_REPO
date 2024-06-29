# What are wrappers and its uses?
"""
Wrapper:- allows you to add extra functionality around the original function (`func`) this could include:
Logging: printing the messages or logging function calls.
Timing: measuring the execution time of the function.
Validation: checking arguments or return values.
Caching: storing results of expensive computations for future use.
"""

# Pre-Processing: perform setup tasks or validation before calling `func`. for example, initializing resources or verifying conditions.
# Post-Processing: After func completes execution, wrapper lets you handle clean-up tasks or additional actions based on the function's output or side effects.

# Return Value Handling: similarly wrapper can intercept the return value of the func. modify it if neccesaary, or perform additional actions based on the return value.