#
# programmatic (dynamic) module import
#

import argparse
import glob
import importlib
import importlib.util

from importlib.machinery import SourceFileLoader
from pathlib import Path

def main():
    parser = argparse.ArgumentParser(description='Programmatic module import.')

    parser.add_argument('--module_path', help='Look the modules from this directory instead of the current working directory.')
    args = parser.parse_args()

    if args.module_path:
        module_path = args.module_path
    else:
        module_path = '.'
    
    for module_filename in glob.glob('{0}/?.py'.format(module_path)):
        module_name = Path(module_filename).stem
        print('found a module: {0} ({1})'.format(module_name, module_filename))

        # import when module in module path
        # module = importlib.import_module(module_name)

        # Python 3.5+
        # spec = importlib.util.spec_from_file_location(module_name, module_filename)
        # module = importlib.util.module_from_spec(spec)
        # spec.loader.exec_module(module)

        # Python 3.3./3.4
        module = SourceFileLoader(module_name, module_filename).load_module()

        # call the module if the interface is supported
        if hasattr(module, 'f'):
            module.f()
        else:
            print("the module doesn't implement the expected interface, skipped.")

if __name__ == '__main__':
    main()
