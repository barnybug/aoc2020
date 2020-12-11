import collections

class Grid(object):
    def __init__(self, d=None, default='.'):
        self.grid = d or {}
        self.default = default

    def __setitem__(self, xy, c):
        self.grid[xy] = c

    def __getitem__(self, xy):
        return self.grid.get(xy, self.default)

    def __str__(self):
        if not self.grid:
            return ''
        return '\n'.join(
            ''.join(
                str(self.grid.get((x,y), self.default))
                for x in self.xrange()
            )
            for y in self.yrange()
        )

    def adjacent(self, xy):
        for x in (-1, 0, 1):
            for y in (-1, 0, 1):
                if x == 0 and y == 0:
                    continue
                if (xy[0] + x, xy[1] + y) in self.grid:
                    yield self.grid[(xy[0] + x, xy[1] + y)]

    def xrange(self):
        minx = min(x for x, _ in self.grid.keys())
        maxx = max(x for x, _ in self.grid.keys())
        return range(minx, maxx+1)

    def yrange(self):
        miny = min(y for _, y in self.grid.keys())
        maxy = max(y for _, y in self.grid.keys())
        return range(miny, maxy+1)

    def bounds(self):
        minx = min(x for x, _ in self.grid.keys())
        maxx = max(x for x, _ in self.grid.keys())
        miny = min(y for _, y in self.grid.keys())
        maxy = max(y for _, y in self.grid.keys())
        return (minx, miny), (maxx, maxy)

    def range(self):
        return (
            (x, y)
            for x in self.xrange()
            for y in self.yrange()
        )

    def area(self):
        (ax, ay), (bx, by) = self.bounds()
        return (bx+1-ax)*(by+1-ay)

    def count(self):
        return collections.Counter(self.grid.values())

    def values(self):
        return self.grid.values()

    def __contains__(self, item):
        return item in self.grid

    @classmethod
    def parse(cls, lines, empty='.'):
        ret = cls(default=empty)
        for y, line in enumerate(lines):
            line = line.strip()
            for x, c in enumerate(line):
                if c != empty:
                    ret[(x, y)] = c
        return ret

