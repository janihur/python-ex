#
# Traverse dictionary and construct all paths
#

def traverse(indata, outdata, parent_outpos, parent_id):
    print('(parent_outpos {0})(parent_id {1})'.format(parent_outpos, parent_id))

    children = {k: v for k, v in indata.items() if v['parent'] == parent_id}

    if not children:
        return

    print('children: {0}'.format(children))

    first_loop = True
    outdata_copy = outdata[parent_outpos].copy()
    
    for k, v in children.items():
        if first_loop:
            outdata[parent_outpos].append(k)
            traverse(indata, outdata, parent_outpos, k)
            first_loop = False
        else:
            outdata.append(outdata_copy.copy())
            outdata[-1].append(k)
            parent_outpos = len(outdata) - 1
            traverse(indata, outdata, parent_outpos, k)

def main():
    input = {
        "a1": {"parent": None}
       ,"a2": {"parent": "a1"}
       ,"a3": {"parent": "a2"}
       ,"a4": {"parent": "a3"}
       ,"b1": {"parent": "a3"}
       ,"b2": {"parent": "b1"}
       ,"c1": {"parent": "a1"}
       ,"d1": {"parent": "a3"}
       ,"d2": {"parent": "d1"}
    }

    root_id = "a1"
    output = [[root_id]]
    traverse(input, output, 0, root_id)
    print(output)
    
if __name__ == '__main__':
    main()
    
