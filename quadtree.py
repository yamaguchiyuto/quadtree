from sklearn.base import BaseEstimator,TransformerMixin

class Quadtree(BaseEstimator,TransformerMixin):
    def __init__(self,x1=None,y1=None,x2=None,y2=None,maxpoints=None,maxdivision=None):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
        self.maxpoints = maxpoints
        self.maxdivision = maxdivision

    def fit(self,X,y=None):
        self.seq_id__ = 0
        self.leaves_ = {}
        self.root__ = self.divide(self.init_area(X),self.maxdivision)
        return self

    def transform(self,X,y=None):
        ret = []
        for i in range(X.shape[0]):
            ret.append(self.root__.get_leaf(X[i]))
        return np.array(ret)

    def fit_transform(self,X,y=None):
        self.fit(X,y)
        return self.transform(X,y)

    def seq_id(self):
        self.seq_id__ += 1
        return self.seq_id__-1

    def gen_leaves(self):
        for l in self.leaves_:
            yield l

    def gen_areas(self):
        r = self.root__
        areas = [r]
        while len(areas) > 0:
            a = areas.pop()
            yield a
            for c in a.children:
                if c != None: areas.append(c)

    def init_area(self,X):
        initial = Area(self.seq_id(),self.x1,self.y1,self.x2,self.y2)
        initial.set_data(X)
        return initial

    def subdivide(self,area):
        division = []

        xl = (area.x2 - area.x1)/2.
        yl = (area.y2 - area.y1)/2.

        upper = (area.data[:,0] > area.x1+xl)
        right = (area.data[:,1] > area.y1+yl)

        for dx in [0,1]:
            for dy in [0,1]:
                """
                Order
                0 2
                1 3
                """
                sub_area = Area(self.seq_id(),area.x1+dx*xl, area.y1+dy*yl, area.x1+(1+dx)*xl, area.y1+(1+dy)*yl)
                sub_area.set_data(area.data[(upper==dx)&(right==dy)])
                division.append(sub_area)

        return division

    def divide(self, area, division_left):
        if division_left == 0 or area.number_of_points() <= self.maxpoints:
            """ Terminate if the number of points in this area does not exceed `maxpoints` """
            self.leaves_[area.aid] = area
            area.set_isfixed()
            area.set_isleaf()
        else:
            """ Do division if the number of points in this aera exceeds `maxpoints` """
            children = self.subdivide(area)
            area.data = None
            """ Divide child areas recursively """
            for i in range(4):
                child = self.divide(children[i],division_left-1)
                area.set_child(i,child)
            """ Return divided area """
        return area

class Area:
    def __init__(self,aid,x1,y1,x2,y2):
        self.aid = aid
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
        self.isfixed_ = False # True if it has no children
        self.isleaf_ = False
        """
        0 2
        1 3
        """
        self.children = [None,None,None,None]

    def set_data(self,X):
        self.data = X

    def number_of_points(self):
        return self.data.shape[0]

    def is_fixed(self):
        return self.isfixed_

    def set_isfixed(self):
        self.isfixed_ = True

    def is_leaf(self):
        return self.isleaf_

    def set_isleaf(self):
        self.isleaf_ = True

    def set_child(self,n,area):
        self.children[n] = area

    def get_leaf(self,p):
        if self.is_leaf():
            return self.aid
        else:
            for c in self.children:
                if c.cover(p):
                    return c.get_leaf(p)

    def cover(self, p):
        """ True if `p` is in this area """
        if self.x1 < p[0] and self.y1 < p[1] and self.x2 >= p[0] and self.y2 >= p[1]:
            return True
        else:
            return False

if __name__ == '__main__':
    import sys
    import numpy as np

    def read_data(file_name):
        data = []
        for line in open(file_name, 'r'):
            entries = line.rstrip().split(' ')
            lat = float(entries[0])
            lng = float(entries[1])
            data.append((lat,lng))
        return np.array(data)

    def usage(com):
        print "[USAGE]: python %s [x left] [y up] [x right] [y down] [maxpoints] [maxdivision] [data filepath] (output filepath)" % com

    if len(sys.argv) < 8:
        usage(sys.argv[0])
        exit()

    x1 = float(sys.argv[1])
    y1 = float(sys.argv[2])
    x2 = float(sys.argv[3])
    y2 = float(sys.argv[4])
    maxpoints = int(sys.argv[5])
    maxdivision = int(sys.argv[6])
    data = read_data(sys.argv[7])

    qtree = Quadtree(x1,y1,x2,y2,maxpoints,maxdivision)

    #qtree.fit(data)
    for aid in qtree.fit_transform(data):
        print aid
    exit()

    if len(sys.argv) == 9:
        import pickle
        output_filepath = sys.argv[8]
        with open(output_filepath, 'w') as f:
            pickle.dump(qtree, f)

    print "AreaID,Depth,x_left,y_up,x_right,y_down"
    for a in qtree.gen_leaves():
        print "%s,%s,%s,%s,%s" % (a.aid,a.x1,a.y1,a.x2,a.y2)

    p = np.array([[0.37,0.55],[0.65,0.90]])
    aids = qtree.transform(p)
    for aid in aids:
        print qtree.leaves_[aid]
