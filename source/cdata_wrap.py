"""
This is a wrapper function that takes in data generated by numerical solver in C 
for maxwells equations and pipes them into a user defined data format for ease
of use with pythons more accessible graph/plot libraries
----------------------------------------------------------------------------------------------------
user defines data format output (csv, text file, etc) ==> data_from_c_code (usually a text file) ==> 
==> data out from wrapper (in previously user defined data format)
----------------------------------------------------------------------------------------------------
"""

import sys, os

# data read in from C code
read_data_c():
    return 


# process read data into user defined data format
post_process_data_c():
    # formats include: csv, special data table, binary
    pass


