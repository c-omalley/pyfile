#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#----------------------------------------------------------------------------
# File: pyfile3.py
#
# Create an empty python script file to expidite the writing of
# utility scripts
#----------------------------------------------------------------------------

import sys

# For working with file and folder names (paths)
from pathlib import Path

# For creating timestamps
from time import strftime


# Create an empty python file using the given name. If the file exists, 
# ValueError will be raised unless force is True.
def pyfile(newfile, force=False):

    p = Path(newfile)
    
    if p.exists() and not force:
        raise ValueError('File exists: use "-f" option to force overwrite')
    
    # Create the scripts's contents
    text = f'''#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#-----------------------------------------------------------------------------
# File: {p.name}
# Date: {strftime('%m-%d-%Y')}
#-----------------------------------------------------------------------------
# Synopsis
#-----------------------------------------------------------------------------

if __name__ == '__main__':
    pass
'''
    # Create any intermediate folders required by the new python file
    if not p.parent.exists():
        p.parent.mkdir(parents=True)
    
    # Create and write the new python file
    with open(p, 'w') as f:
        f.write(text)
    
    # On Linux, mark the new python file as executable
    if sys.platform.startswith('linux'):
        p.chmod(0o755)


# Run script
if __name__ == '__main__':

    help = '''
Usage: pyfile [-f] file(s) to create...

Creates an empty python script file to expedite the writing of
utility programs

Options:

    -f  force overwrite if file already exists (be careful)
    -h  print this help message

Author:

    Charlie O'Malley <comalley68w@gmail.com>
'''

    # Grab a copy of the script arguments
    arguments = sys.argv[1:]

    # Simple method for parsing script flags like "-h" and "-f" as
    # noted in the help message above
    def flag(f):
        try:
            arguments.remove(f)
            return True
        except ValueError:
            return False

    # Process flag options
    force = flag('-f')
    if flag('-h') or not arguments:
        sys.exit(help)
    
    # Process all remaining arguments as python files to create by name
    for filename in arguments:
        try:
            pyfile(filename, force)
            print(f'Created: {filename}')
        except Exception as e:
            print(f'[{filename}] {e}')
