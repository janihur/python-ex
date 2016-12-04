#
# Construct full paths from dictionary
#

# '<ID>': ('<NAME>', '<PARENT_ID>')
dirs = {
    'jqvhF6xI3bWhGWVQ5RVcxTWM': ('f1', 'jqvhF6xI3Uk9PVA')
   ,'jqvhF6xI3Uk9PVA': ('root', '')
   ,'26eBSyIQhRW9hbzdibG9pR3M': ('f1-1', 'jqvhF6xI3bWhGWVQ5RVcxTWM')
   ,'26eBSyIQhS2l3X21vcUFIQ2c': ('f2-1', 'jqvhF6xI3YzNrVjJ2QXRiLUk')
   ,'26eBSyIQhRmZOYkE4TFBQNlE': ('f2-1-2-3', '26eBSyIQhNWVXbk02a3gxaTQ')
   ,'26eBSyIQhNWVXbk02a3gxaTQ': ('f2-1-2', '26eBSyIQhS2l3X21vcUFIQ2c')
   ,'jqvhF6xI3YzNrVjJ2QXRiLUk': ('f2', 'jqvhF6xI3Uk9PVA')
}

paths = []

def r(path, id):
    path = dirs[id][0] + '/' + path
    if dirs[id][0] == 'root':
        return path
    else:
        return r(path, dirs[id][1])

for id in dirs.keys():
    print('(id {0})'.format(id))
    if dirs[id][0] == 'root':
        continue
    paths.append(r(dirs[id][0], dirs[id][1]))

for p in sorted(paths):
    print('({0})'.format(p))
