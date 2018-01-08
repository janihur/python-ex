#
# jinja2 templates
#

from jinja2 import Environment, FileSystemLoader
import os

ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
TEMPLATE_DIR = os.path.join(ROOT_DIR, 'templates')

J2 = Environment(
    loader = FileSystemLoader(TEMPLATE_DIR),
    trim_blocks = True
)

def render(template, **context):
    return J2.get_template(template).render(**context)

def main():
    print('(ROOT_DIR = {0})'.format(ROOT_DIR))
    print('(TEMPLATE_DIR = {0})'.format(TEMPLATE_DIR))

    data = {
        'a': "Fifteen men on a dead man's chest",
        'b': 'Yo ho ho and a bottle of rum',
        'c': 'Drink and the devil had done for the rest'
    }

    print(render('template-1.xml', **data))
    print(render('template-2.xml', **{
        'a': "Fifteen men on a dead man's chest",
        'b': 'Yo ho ho and a bottle of rum',
        'c': 'Drink and the devil had done for the rest'
    }))

if __name__ == '__main__':
    main()

