import day01, day02

def test_day01_part1():
    assert day01.part1([1721,979,366,299,675,1456]) == 514579

def test_day01_part2():
    assert day01.part2([1721,979,366,299,675,1456]) == 241861950

def test_day02_part1():
    assert day02.part1(['1-3 a: abcde', '1-3 b: cdefg', '2-9 c: ccccccccc']) == 2

def test_day02_part2():
    assert day02.part2(['1-3 a: abcde', '1-3 b: cdefg', '2-9 c: ccccccccc']) == 1
