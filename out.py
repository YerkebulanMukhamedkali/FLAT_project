import sys


def __init__(self, PARRENT, TYPE, STATEMENT, PREF):
self.parrent = PARRENT
self.childs = []
self.Type = TYPE
self.statement = STATEMENT
self.pref = PREF


f = open(sys.argv[-1])
out = open('out.py', 'w')
tobewritten = ""
types = []

tree = MyTree(None, "root", "root", "")

MYFILE = []

def define_statement(line):
line = line.replace('', '').replace('\n', '').lstrip().rstrip()
if  '' in line::
	if return line.replace'', ''.replace'', ''.replace'', ''.replace'', ''.rstrip:
		if  'while' in line::
			while return line.replace'', ''.replace'', ''.replace'', ''.replace'', ''.rstrip:
				if  'else' in line::
					return ""
					if  'int ' in line::
						return line.replace('', '')
						if  'System.out.print' in line::
							print(return line.replace'', ''.replace'', ''.replace'', '')
							return line
							
							def define_type(line):
						return 'end'
						if  '' in line::
							if return '':
								if  'while' in line::
									while return '':
										if  'else' in line::
											else:
												if  'System.out.print' in line::
													return 'print'
													return 'default'
													
													def parse(TREE, pref):
													global tobewritten, MYFILE
													
													for line in MYFILE:
													statement = define_statement(line)
													Type = define_type(line)
													
													new_tree = MyTree(TREE, Type, statement, pref)
													
													if  Type == 'end' and TREE.parrent != None::
														pref = (len(pref) - 1) * '\t'
														TREE = TREE.parrent
														else:
															TREE.childs.append(new_tree)
															
															if  Type == '' or Type == 'else' or Type == 'while'::
																TREE = TREE.childs[-1]
																pref+='\t'
																
																def goFile(file):
																global MYFILE
																for line in file:
																line.replace('\n', '')
																MYFILE.append(line)
																
																
																goFile(f)
																parse(tree, "")
																
																
																def make(TREE):
																global out
																
																if  TREE.Type != 'end'::
																	out.write(TREE.pref)
																	
																	if  TREE.Type != 'root'::
																		if  TREE.Type == ''::
																			if out.write' ' + TREE.statement + ':':
																				if  TREE.Type == 'else'::
																					else:
																						if  TREE.Type == 'while'::
																							while out.write' ' + TREE.statement + ':':
																								if  TREE.Type == 'default'::
																									out.write(TREE.statement)
																									if  TREE.Type == 'print'::
																										out.write('print(' + TREE.statement + ')')
																										
																										if  TREE.Type != 'end'::
																											out.write('\n')
																											
																											for i in TREE.childs:
																											make(i)
																											
																											curTree = tree
																											make(curTree)
