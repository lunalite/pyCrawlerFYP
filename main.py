import re
import os
from Function_Decl import Function_Decl
from Tree import Tree


def cat_func(string_list):
    list_of_function_array = []
    function_array = []
    lock_first = 0
    lock_second = 0
    func = ""
    for line in string_list:
        if lock_first == 0:
            if re.match('(int|void) [a-zA-Z_]+\(.+', line):
                # print line
                line_split = line.split()
                m = re.search('^.+?(?=\()', line_split[1])
                if m:
                    func = Function_Decl(m.group(0))
                lock_first = 1
                function_array.append(line)
                continue
        elif lock_first == 1:
            if not re.match('}', line):
                function_array.append(line)
            else:
                function_array.append(line)
                lock_first = 0
                lock_second = 1
        if lock_second == 1:
            if isinstance(func, basestring):
                print 'error'
            else:
                func.body = function_array
            list_of_function_array.append(func)
            function_array = []
            lock_second = 0

    # for i in list_of_function_array:
    #     print i.body
    return list_of_function_array


def parseAST_to_tree(ast_list):
    for line in ast_list:
        # print line
        if re.match('@FunctionDecl.*', line):
            # level one nodes
            root = Tree(line)
            previous_node_one = root
        elif re.match('@(\||`)-.*', line):
            # level two nodes
            node = Tree(line)
            previous_node_one.add(node)
            previous_node_two = node
        elif re.match('@  (\||`)-.*', line):
            # level three nodes
            node = Tree(line)
            previous_node_two.add(node)
            previous_node_three = node
        elif re.match('@  (\|| ) (\||`)-.*', line):
            # level four nodes
            node = Tree(line)
            previous_node_three.add(node)
            previous_node_four = node
        elif re.match('@  (\|| ) (\|| ) (\||`)-.*', line):
            # level five nodes
            node = Tree(line)
            previous_node_four.add(node)
            previous_node_five = node
        elif re.match('@  (\|| ) (\|| ) (\|| ) (\||`)-.*', line):
            # level six nodes
            node = Tree(line)
            previous_node_five.add(node)
            previous_node_six = node
    Tree.print_node(root)


if __name__ == "__main__":
    fnames = []
    # fpath = "/home/hdk216/Documents/kernel/up.c"
    fpath = "/home/hdk216/a/test.c"

    with open(fpath) as f:
        content = f.readlines()
        content = [x.strip() for x in content]

    function_list = cat_func(content)

    print '**********************************'
    for i in function_list:
        with open('./temp.c', 'w+') as f:
            for k in i.body:
                f.write(k)

        os.system('clang-check -ast-dump -ast-dump-filter=' + i.name + ' temp.c 2>/dev/null > tempRecord ')

        with open('./tempRecord', 'r') as f:
            content = f.readlines()
            content = [x.strip('\n') for x in content]
            content = ["@" + x for x in content]
        parseAST_to_tree(content)
