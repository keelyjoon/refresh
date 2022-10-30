"""
goal parser: goal parser cacn interpret a string command. The command consists of an alphabet
of "G", "()", or "(al)".

example: 
input: command = "G()(al)"
output: Goal

example:
input 
"""

# make list, loop through list, conditions, print 
    # this wont work because it will seperate 

def replaced(string):
    if "G" in string:
        string.replace("G", "G")
    elif "()" in string:
        string.replace("()", "o")
    elif "(al)" in string:
        string.replace("(al)", "al")
    
    print(string)

replaced("G()(al)")