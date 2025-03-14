from jinja2 import Environment, FunctionLoader

import module2 as M2

def main():
    env = Environment(loader=FunctionLoader(M2.load_template))
    template = env.get_template(None)
    data = {
        'text': M2.content(),
    }
    output = template.render(data)
    print(output)

if __name__ == '__main__':
    main()