#!/bin/python

from utils import *
import argparse


parser= argparse.ArgumentParser(description="Tool to generate 2D linear access traces.")
parser.add_argument('read',metavar="-r",type=int,nargs=1, help='number of elements to read in sequence')
parser.add_argument('skip',metavar="-s",type=int,nargs=1, help='number of elements to skip in sequence')
parser.add_argument('M',metavar="-M",type=int,nargs=1, help='Number of columns in the 2D data structure')
parser.add_argument('N',metavar="-N",type=int,nargs=1, help='Number of rows in the 2D data structure')
parser.add_argument('offset',metavar="-o",type=int,nargs=1, help='number of elements to skip at the beginning')
args = parser.parse_args()

read=args.read[0]
skip=args.skip[0]
M=args.M[0]
N=args.N[0]
offset=args.offset[0]

def write_pattern(filename, pattern):
    text_file = open(filename, "w")
    text_file.write("%s" % pattern)
    text_file.close()

sparsity=read*100/(skip+read)

pattern=generateAccessPatterns_Atrace_linear_dense_new_correct(read,skip,M,N,offset)
outputfilename="pattern_"+str(sparsity)+"percent_M_"+str(M)+"_N_"+str(N)+"_offset_"+str(offset)+".atrace"
write_pattern(outputfilename,pattern)


