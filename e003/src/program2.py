from jinja2 import Environment, FunctionLoader

import resources.resource as resource
import module2 as M2

def main():
    # -------------------------------------------------------------------------
    print('--- data file')
    print(resource.read('data2.txt'))

    # -------------------------------------------------------------------------
    print('--- template')
    env = Environment(loader=FunctionLoader(M2.load_template))
    template = env.get_template(None)
    data = {
        'text': M2.content(),
    }
    output = template.render(data)
    print(output)

if __name__ == '__main__':
    main()