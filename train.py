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
p.add_argument("-o", "--outfile", help="output model file", type=argparse.FileType('w'), required=True)
p.add_argument("-d", "--maxdepth", help="the maximum number of quadtree depth (default=10)", type=int, nargs='?', default=10)
p.add_argument("-p", "--maxpoints", help="the maximum number of points in each area (required)", type=int, required=True)
p.add_argument("-u", "--upper", help="upper left point (required)", type=float, nargs=2, metavar=('X','Y'), required=True)
p.add_argument("-l", "--lower", help="loewr right point (required)", type=float, nargs=2, metavar=('X', 'Y'), required=True)
args = p.parse_args()

X = read_data(args.infile)

qtree = Quadtree(args.upper[0],args.upper[1],args.lower[0],args.lower[1],args.maxpoints,args.maxdepth)
qtree.fit(X)

pickle.dump(qtree, args.outfile)
