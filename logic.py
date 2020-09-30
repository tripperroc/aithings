import numpy as np
import pdb

SIZE = 4
B = np.array([["B%d%d" % (i,j) for j in range(SIZE)] for i in range(SIZE)])
P = np.array([["P%d%d" % (i,j) for j in range(SIZE)] for i in range(SIZE)])
W = np.array([["W%d%d" % (i,j) for j in range(SIZE)] for i in range(SIZE)])
S = np.array([["S%d%d" % (i,j) for j in range(SIZE)] for i in range(SIZE)])


KB = ["iff", [B[0,0], ["or", [P[1,0],P[0,1]]]]]

def eliminate_iffs(formula):
	if formula[0] == "if":
		return eliminate_iffs(["or" , [["not", formula[1][0]],
			formula[1][1]]])
	elif formula[0] == "iff":
		return ["and", [eliminate_iffs(["or" , [["not", formula[1][0]],
			formula[1][1]]]), eliminate_iffs(["or" , [["not", formula[1][1]],
			formula[1][0]]])]]
	elif formula[0] in {"and", "or"}:
		return [formula[0], [eliminate_iffs(formula[1][0]),
			eliminate_iffs(formula[1][1])]]
	elif formula[0] in {"not"}:
		return [formula[0], eliminate_iffs(formula[1])]
	else:
		return formula

def eliminate_nots(formula):
	if formula[0] == "not":
		#pdb.set_trace()
		if formula[1][0] in {"or", "and"}:
			return [({"or", "and"}-{formula[1][0]}).pop(), [["not", eliminate_nots(formula[1][1][0])],
				["not", eliminate_nots(formula[1][1][1])]]]
		#elif formula[1][0] == "and":
		#	return ["or", [["not", eliminate_nots(formula[1][1][0])],
		#		["not", eliminate_nots(formula[1][1][1])]]]
		else:
			return formula
	elif formula[0] in {"or", "and"}:
		#pdb.set_trace()
		return [formula[0], [eliminate_nots(formula[1][0]),
			eliminate_nots(formula[1][1])]]
	else:
		return formula


def to_cnf(formula):
	if formula[0] in {"or", "and"}:
		if formula[1][0] == "or" and formula[1][1] == "or":
			return  

KB=eliminate_iffs(KB)

