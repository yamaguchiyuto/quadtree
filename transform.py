import sys
import argparse
import pickle
import numpy as np
from quadtree import Quadtree

def read_data(f):
    data = []
    for line in f:
        entries = line.rstrip().split(' ')
        lat = float(entries[0])
        lng = float(entries[1])
        data.append((lat,lng))
    return np.array(data)

p = argparse.ArgumentParser()
p.add_argument("-i", "--infile", help="input file", type=argparse.FileType('r'), required=True)
p.add_argument("-m", "--modelfile", help="model file", type=argparse.FileType('r'), required=True)
p.add_argument("-o", "--outfile", help="output file (default=STDOUT)", type=argparse.FileType('w'), nargs='?', default=sys.stdout)
args = p.parse_args()

X = read_data(args.infile)
qtree = pickle.load(args.modelfile)

X_trans = qtree.transform(X)
print '"area ID","upper left x","upper left y","lower right x","lower right y"'
for i in range(len(X_trans)):
    a = qtree.leaves_[X_trans[i]]
    print >>args.outfile, "%s,%s,%s,%s,%s" % (a.aid,a.x1,a.y1,a.x2,a.y2)
