import sys
import argparse
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
p.add_argument("-i", "--infile", help="input file (default=STDIN)", type=argparse.FileType('r'), nargs='?', default=sys.stdin)
p.add_argument("-o", "--outfile", help="output file (default=STDOUT)", type=argparse.FileType('w'), nargs='?', default=sys.stdout)
p.add_argument("-d", "--maxdepth", help="the maximum number of quadtree depth (default=10)", type=int, nargs='?', default=10)
p.add_argument("-p", "--maxpoints", help="the maximum number of points in each area (required)", type=int, required=True)
p.add_argument("-u", "--upper", help="upper left point (required)", type=float, nargs=2, metavar=('X','Y'), required=True)
p.add_argument("-l", "--lower", help="loewr right point (required)", type=float, nargs=2, metavar=('X', 'Y'), required=True)
args = p.parse_args()

X = read_data(args.infile)

qtree = Quadtree(args.upper[0],args.upper[1],args.lower[0],args.lower[1],args.maxpoints,args.maxdepth)

X_trans = qtree.fit_transform(X)
print '"area ID","upper left x","upper left y","lower right x","lower right y"'
for i in range(len(X_trans)):
    a = qtree.leaves_[X_trans[i]]
    print >>args.outfile, "%s,%s,%s,%s,%s" % (a.aid,a.x1,a.y1,a.x2,a.y2)
