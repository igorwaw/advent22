#!/usr/bin/python3

from treelib import Node, Tree


INPUTFILE = "7-input.txt"
#INPUTFILE = "7-small.txt"
MAXSIZE=100000
TOTALSPACE=70000000
REQUIREDSPACE=30000000


# class for representing file or dir in the directory tree
# size 0 = size unknown
# type = f for file, d for directory
class FSnode():
    def __init__(self, type, size=0):
        self.type = type
        self.size = size

#directory tree
fstree = Tree()
fstree.create_node("/", "/", data=FSnode("d"))

# current directory - as stack so we can easily do cd ..
cwd = ["/"]

#directory list, dictionary path: size
dirlist={}

def parse_line(line):
    if line[0] == "$":  # we got a command
        if line[2:4] == "cd":  # we only need to do something with cd and skip ls
            do_cd(line[5:])
    elif line[0] == "d":
        append_node("d", line[4:])
    else:
        filesize, filename = line.split()
        append_node("f", filename, filesize)


def append_node(type, filename, filesize=0):
    global cwd, fstree
    fullpath, parentpath = create_path(cwd, filename)
    # print("Adding node ", filename, " type ", type, "size ", filesize, " in ", parentpath, " fullpath ",fullpath)
    fstree.create_node(filename, fullpath, parent=parentpath,
                       data=FSnode(type, filesize))


def create_path(cwd, filename):
    path = ""
    for dir in cwd:
        if dir == "/":
            continue
        else:
            path = path+"/"+dir
    if path == "":
        parentpath = "/"
    else:
        parentpath = path
    path = path+"/"+filename
    return path, parentpath


def do_cd(dir):
    global cwd
    #print("cd to: ",dir, "path before ", "/".join(cwd))
    if dir == "/":
        cwd = ["/"]
    elif dir == "..":
        cwd.pop()
    else:
        cwd.append(dir)
    #print("   path after ","/".join(cwd))



def traverse_tree(startnode):
    global fstree
    #print("Checking node ", startnode)
    for node in fstree.children(startnode.identifier):
        if node.data.type == "d":
            startnode.data.size+=traverse_tree(node)
        else:
                # somehow anytree thinks the second size is string
            startnode.data.size += int(node.data.size)
    # we reached here - it means we iterated through the whole dir + subdirs
    # return the calculated size so it can be used by the higher-lever traverse_tree
    # (see few lines above)
    return startnode.data.size


def create_dirlist(tree):
    dirlist={}
    for node in tree.all_nodes():
        if node.data.type=="d":
            #print(node.data)
            dirlist[node.identifier] = node.data.size
    return dirlist


# parse input
with open(INPUTFILE) as inputfile:
    for line in inputfile:
        parse_line(line.rstrip())

#fstree.show()
#fstree.show(data_property="size")  # sizes before
traverse_tree(fstree.get_node("/")) # recursively traverse tree and calculate directory sizes
#fstree.show(data_property="size")  # sizes after
dirlist=create_dirlist(fstree)


totalsize=0 #for part1
usedspace=fstree.get_node("/").data.size
requiredsize=REQUIREDSPACE+usedspace-TOTALSPACE #for part 2
dirlist2={} # for part2

for path,size in dirlist.items():
    if size<=MAXSIZE:  # find answer to part 1
        totalsize+=size
    if size>=requiredsize: # create another dict with dirs of required size for part 2
        dirlist2[size]=path
print("Part 1, total size: ", totalsize)
dirkey=(sorted(dirlist2))[0] # size, and also key, of the smallest dir meeting the criteria
print("Part 2, required size: ", requiredsize, "found dir ", dirlist2[dirkey]," of size ", dirkey)

