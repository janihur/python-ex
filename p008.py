#
# Get value "safely" from list and map.
#

def main():
    x = [{'x': 0}]

    def f():
        def safe_get(data, index, key):
            try:
                return data[index][key]
            except (IndexError, KeyError):
                return None

        try:
            x1 = x[1]['x']
        except IndexError:
            x1 = None

        print('({0})({1})({2})({3})({4})'.format(
            x[0]['x'],
            x1,
            safe_get(x, 0, 'x'),
            safe_get(x, 0, 'y'),
            safe_get(x, 1, 'x')
        ))

    f()

if __name__ == '__main__':
    main()
