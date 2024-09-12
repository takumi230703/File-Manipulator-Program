import sys

inputpath = sys.argv[2]
outputpath = sys.argv[3]
contents = ''

if sys.argv[1] == 'reverse':
    with open(inputpath) as f:
        contents = f.read()
        tempt = contents
    with open(outputpath) as f:
        contents = f.read()
    with open(inputpath, 'w') as f:
        f.write(contents)
    with open(outputpath, 'w') as f:
        f.write(tempt)
elif sys.argv[1] == 'copy':
    with open(inputpath) as f:
        contents = f.read()
    with open(outputpath, 'w') as f:
        f.write(contents)
elif sys.argv[1] == 'duplicate-contents':
    time = int(sys.argv[3])
    with open(inputpath) as f:
        contents = f.read()
    with open(inputpath, 'w') as f:
        for i in range(0, time):
            f.write(contents + "\n")
elif sys.argv[1] == 'replace-string':
    s1 = sys.argv[3]
    s2 = sys.argv[4]
    with open(inputpath) as f:
        contents = f.read()
    modified_contents = contents.replace(s1, s2)
    with open(inputpath, 'w') as f:
        f.write(modified_contents)
else: print('Invalid command')

