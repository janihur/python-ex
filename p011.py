#
# Read file several times and write to another file
#

with open('p011-in.txt', 'r') as infile:
    with open('p011-out.txt', 'w') as outfile:
        for i in range(4):
            outfile.write('*** Read {} ***\n'.format(i+1))
            outfile.write(infile.read())
            outfile.write('\n')
            infile.seek(0)
