import sys

class MyTree:

    def __init__(self, PARRENT, TYPE, STATEMENT, PREF):
        self.parrent = PARRENT
        self.childs = []
        self.Type = TYPE
        self.statement = STATEMENT
        self.pref = PREF

result = ""

tree = MyTree(None, "root", "root", "")

MYFILE = []

def define_statement(line):
    line = line.replace(';', '').replace('\n', '').lstrip().rstrip()
    if ('if' in line):
        return line.replace('if', '').replace('(', '').replace(')', '').replace('{', '').rstrip()
    if ('while' in line):
        return line.replace('while', '').replace('(', '').replace(')', '').replace('{', '').rstrip()
    if ('else' in line):
        return ""
    if ('int ' in line):
        return line.replace('int ', '')
    if ('System.out.print' in line):
        return line.replace('System.out.print', '').replace('(', '').replace(')', '')
    return line

def define_type(line):
    if '}' in line:
        return 'end'
    if 'if' in line:
        return 'if'
    if 'while' in line:
        return 'while'
    if 'else' in line:
        return 'else'
    if 'System.out.print' in line:
        return 'print'
    return 'default'

def parse(TREE, pref):
    global MYFILE

    for line in MYFILE:
        statement = define_statement(line)
        Type = define_type(line)
        
        new_tree = MyTree(TREE, Type, statement, pref)
        
        if Type == 'end' and TREE.parrent != None:
            pref = (len(pref) - 1) * '\t'
            TREE = TREE.parrent
        else:
            TREE.childs.append(new_tree)

        if Type == 'if' or Type == 'else' or Type == 'while':
            TREE = TREE.childs[-1]
            pref+='\t'

def goFile(file):
    global MYFILE
    for line in file:
        line.replace('\n', '')
        if 'class' not in line and 'void ' not in line:
            MYFILE.append(line)
  
def make(TREE):
    global result

    if (TREE.Type != 'end'):
        result += TREE.pref

    if (TREE.Type != 'root'):
        if (TREE.Type == 'if'):
            result += 'if ' + TREE.statement + ':'
        if (TREE.Type == 'else'):
            result += 'else:'
        if (TREE.Type == 'while'):
            result += 'while ' + TREE.statement + ':'
        if (TREE.Type == 'default'):
            result += TREE.statement
        if (TREE.Type == 'print'):
            result += 'print(' + TREE.statement + ')'
        
        if (TREE.Type != 'end'):
            result += '\n'
    
    for i in TREE.childs:
        make(i)

# curTree = tree
# make(curTree)

def do_it(filename):
    global result, tree, MYFILE

    result = ""
    f = open(filename, 'r')
    goFile(f)
    f.close()
    parse(tree, "")
    curTree = tree
    make(curTree)
    return result
