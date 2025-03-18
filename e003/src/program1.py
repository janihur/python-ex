from jinja2 import Environment, FunctionLoader

import resources.resource as resource
import module1 as M1

def main():
    # -------------------------------------------------------------------------
    print('--- data file')
    print(resource.read('data1.txt'))

    # -------------------------------------------------------------------------
    print('--- template')
    env = Environment(loader=FunctionLoader(M1.load_template))
    template = env.get_template(None)
    data = {
        'text': M1.content(),
    }
    output = template.render(data)
    print(output)

if __name__ == '__main__':
    main()