#!/usr/bin/env python

from collections import Counter
from dataclasses import dataclass
from scipy.ndimage import convolve
import re

import numpy as np
from math import prod, sqrt

pow2 = np.array([
    [1 << i, 1 << (9-i)]
    for i in range(10)
])

def grid_to_array(grid):
    return np.array([[1 if c == '#' else 0 for c in line] for line in grid.splitlines()])

class Tile:
    def __init__(self, n, grid):
        self.n = n
        self.grid = grid
        # precalculate useful numbers
        # edge number - pick lowest of two invariant to flipping
        self.t, self.tf = self.grid[0].dot(pow2)
        self.bf, self.b = self.grid[-1].dot(pow2)
        self.lf, self.l = self.grid[:,0].dot(pow2)
        self.r, self.rf = self.grid[:,-1].dot(pow2)
        self.edges = np.array([self.l, self.t, self.r, self.b])
        self.potential_edges = {
            self.t, self.tf,
            self.b, self.bf,
            self.l, self.lf,
            self.r, self.rf,
        }

    @staticmethod
    def parse(data):
        header, grid = data.split('\n', 1)
        n, = re.findall(r'Tile (\d+)', header)
        return Tile(int(n), grid_to_array(grid))

    def __repr__(self):
        return f'''   {self.t:4d} {self.tf:4d}
{self.lf:4d}  {self.n:4d}  {self.r:4d}
{self.l:4d}  {self.n:4d}  {self.rf:4d}
    {self.bf:4d} {self.b:4d}    '''

    def edge_orientations(self):
        # 16 orientations - 4 rotations, fliph+4 rotations, flipv+4rotations, transpose+4rotations
        return [
            np.roll([self.l, self.t, self.r, self.b], i) for i in range(0, 4)
        ] + [
            np.roll([self.rf, self.tf, self.lf, self.bf], i) for i in range(0, 4)
        ] + [
            np.roll([self.lf, self.bf, self.rf, self.tf], i) for i in range(0, 4)
        ] + [
            np.roll([self.tf, self.l, self.bf, self.r], i) for i in range(0, 4)
        ]

    def reorient(self, n):
        return Tile(self.n, transformations(self.grid, n))

NUM_TRANSFORMATIONS = 16

def transformations(grid, i):
    if i < 4:
        return np.rot90(grid, -i)
    elif 4 <= i < 8: # fliph
        return np.rot90(np.flip(grid, axis=1), -i)
    elif 8 <= i < 12: # flipv
        return np.rot90(np.flip(grid, axis=0), -i)
    else: # transpose
        return np.rot90(grid.T, -i)

def get_outer_edges(tiles):
    edge_count = Counter(edge for tile in tiles for edge in tile.potential_edges)
    # outer edges are unique
    outer_edges = {edge for edge, c in edge_count.items() if c == 1}
    # a corner has 4 outer edges (normal and flipped)
    corners = [tile for tile in tiles if len(tile.potential_edges & outer_edges) == 4]
    return outer_edges, corners

def part1(data):
    tiles = [Tile.parse(tiledata) for tiledata in data.split('\n\n')]
    _, corners = get_outer_edges(tiles)
    assert len(corners) == 4
    return prod(tile.n for tile in corners)

def solve_board(tiles, size):
    outer_edges, corners = get_outer_edges(tiles)
    starting_corner = corners[0]
    # orient corner left and top
    starting_corner = next(
        starting_corner.reorient(i)
        for i, (l, t, _, _) in enumerate(starting_corner.edge_orientations())
        if {t, l}.issubset(outer_edges)
    )
    unused = set(tiles)
    layout = np.zeros((size, size), np.object)
    lookup = {
        (l, t): (orient, tile)
        for tile in tiles
        for orient, (l, t, _, _) in enumerate(tile.edge_orientations())
    }
    for y in range(size):
        for x in range(size):
            if y == 0 and x == 0:
                tile = starting_corner
            elif x > 0 and y > 0:
                orient, tile = lookup[layout[y, x-1].rf, layout[y-1, x].bf]
                tile = tile.reorient(orient)
            else:
                leftside = outer_edges if x == 0 else {layout[y, x-1].rf}
                topside = outer_edges if y == 0 else {layout[y-1, x].bf}
                tile = next((
                    tile.reorient(orient)
                    for tile in unused
                    for orient, (l, t, _, _) in enumerate(tile.edge_orientations())
                    if l in leftside and t in topside
                ), None)
                assert tile

            layout[y,x] = tile
            unused = [t for t in unused if t.n != tile.n]
    return layout

def combine_tiles(layout, size):
    combined = np.zeros((8 * size, 8 * size), np.int)
    for y in range(size):
        for x in range(size):
            combined[y*8:(y+1)*8,x*8:(x+1)*8] = layout[y,x].grid[1:-1,1:-1]
    return combined

def solve_snakes(combined):
    snake = '''
                  # 
#    ##    ##    ###
 #  #  #  #  #  #   '''.strip('\n')
    snake = grid_to_array(snake)
    snakelen = snake.sum()
    found = False
    for i in range(NUM_TRANSFORMATIONS):
        d = transformations(combined, i)
        for y in range(d.shape[0] - snake.shape[0] + 1):
            for x in range(d.shape[1] - snake.shape[1] + 1):
                window = d[y:y+snake.shape[0], x:x+snake.shape[1]]
                if (window * snake).sum() == snakelen:
                    window -= snake
                    found = True
        if found:
            return d.sum()

def part2(data):
    tiles = [Tile.parse(tiledata) for tiledata in data.split('\n\n')]
    size = int(sqrt(len(tiles)))
    layout = solve_board(tiles, size)
    combined = combine_tiles(layout, size)
    return solve_snakes(combined)

def display(grid):
    print('\n'.join(''.join('#' if cell else '.' for cell in row) for row in grid))
    
if __name__ == '__main__':
    data = open('input20.txt').read()
    print(part1(data))
    print(part2(data))
