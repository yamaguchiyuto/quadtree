class Quadtree:
    def __init__(self,data,x1,y1,x2,y2,maxpoints,maxdivision):
        self.data = data
        self.sequential_id = 0
        self.leaves = {}
        self.root = self.divide(self.init_area(data,x1,y1,x2,y2),maxpoints,maxdivision)

    def __iter__(self):
        for aid in self.leaves:
            yield self.leaves[aid]

    def init_area(self,data,x1,y1,x2,y2):
        initial = Area(x1,y1,x2,y2)
        for d in data:
            initial.append(d)
        return initial

    def subdivide(self,area):
        division = []

        xl = (area.x2 - area.x1)/2
        yl = (area.y2 - area.y1)/2

        for dx in [0,1]:
            for dy in [0,1]:
                """
                Order
                0 2
                1 3
                """
                sub_area = Area(area.x1+dx*xl, area.y1+dy*yl, area.x1+(1+dx)*xl, area.y1+(1+dy)*yl)
                division.append(sub_area)

        """ Assign points to new areas """
        for p in area.points():
            for sub_area in division:
                if sub_area.cover(p):
                    sub_area.append(p)
                    break

        return division

    def divide(self, area, maxpoints, division_left):
        if division_left == 0 or area.number_of_points() <= maxpoints:
            """ Terminate if the number of points in this area does not exceed `maxpoints` """
            area.set_fixed(self.sequential_id)
            area.calc_center()
            self.leaves[self.sequential_id] = area
            self.sequential_id += 1
            return area
        else:
            """ Do division if the number of points in this aera exceeds `maxpoints` """
            next_level = self.subdivide(area)
            """ Divide child areas recursively """
            for i in range(4):
                child = self.divide(next_level[i],maxpoints,division_left-1)
                area.set_child(i,child)
            """ Return divided area """
            return area

    def get_area_id(self,p):
        return self.root.covered(p)

class Area:
    def __init__(self,x1,y1,x2,y2):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
        self.points_ = []
        self.fixed = False # True if it has no children
        """
        0 2
        1 3
        """
        self.children = [None,None,None,None]

    def calc_center(self):
        if self.number_of_points() == 0:
            self.center = (self.x1 + (self.x2-self.x1)/2, self.y1 + (self.y2-self.y1)/2)
        else:
            sumx = 0.
            sumy = 0.
            for p in self.points_:
                sumx += p[0]
                sumy += p[1]
            self.center = (sumx/len(self.points_), sumy/len(self.points_))

    def append(self, p):
        self.points_.append(p)

    def points(self):
        return self.points_

    def number_of_points(self):
        return len(self.points_)

    def is_fixed(self):
        return self.fixed

    def set_fixed(self,aid):
        self.fixed = True
        self.aid = aid

    def set_child(self,n,area):
        self.children[n] = area

    def covered(self,p):
        if self.cover(p):
            if self.fixed:
                return self.aid
            else:
                cid = 0
                if self.x1 + (self.x2 - self.x1) / 2 < p[0]:
                    cid += 2
                if self.y1 + (self.y2 - self.y1) / 2 < p[1]:
                    cid += 1
                return self.children[cid].covered(p)
        else:
            return None

    def cover(self, p):
        """ True if `p` is in this area """
        if self.x1 < p[0] and self.y1 < p[1] and self.x2 >= p[0] and self.y2 >= p[1]:
            return True
        else:
            return False

if __name__ == '__main__':
    import sys

    def read_data(file_name):
        data = []
        for line in open(file_name, 'r'):
            entries = line.rstrip().split(' ')
            lat = float(entries[0])
            lng = float(entries[1])
            data.append((lat,lng))
        return data

    def usage(com):
        print "[USAGE]: python %s [x left] [y up] [x right] [y down] [maxpoints] [maxdivision] [data filepath]" % com

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

    qtree = Quadtree(data,x1,y1,x2,y2,maxpoints,maxdivision)

    print "AreaID,x_left,y_up,x_right,y_down,x_center,y_center"
    for a in qtree:
        print "%s,%s,%s,%s,%s,%s,%s" % (a.aid,a.x1,a.y1,a.x2,a.y2,a.center[0],a.center[1])

    p = (0.37,0.55)
    print 
    print "Query: (%s,%s)" % p
    print "Returned Area ID: %s" % qtree.get_area_id(p)
