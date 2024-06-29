from string import Template

var_1 = "rupees"
var_2 = "dollar"

my_string = Template(
    "we can put '$variable_1' with '$variable_2' prefix and use them later , creating a template"
)
print(my_string.substitute(variable_1=var_1, variable_2=var_2))

print(
    """
    string.template():

    Pros:
    Simplicity: Easier to use for basic replacements.
    Safety: Less prone to security issues when dealing with user input.
    
    Cons:
    Limited Functionality: Lacks advanced formatting options.
    Verbose: Requires creating a Template object and using its methods.

    string.format():
    
    Pros:
    Flexibility: Allows complex expressions and advanced formatting.
    Versatile: Suitable for a wide range of use cases.
    
    Cons:
    Complexity: More complex syntax.
    Potential Security Issues: Can be less safe when formatting user input without proper handling.
    """
)


