import os

def file_to_file(input):

    output = "/home/dani/Escritorio/output.txt"
    os.system(("ps2ascii %s %s") %( input , output))
    
    return(output)