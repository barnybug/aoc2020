import pytest
import day01, day02, day03, day04, day05, day06, day07, day08, day09, day10
import day11, day12, day13

def test_day01_part1():
    assert day01.part1([1721,979,366,299,675,1456]) == 514579

def test_day01_part2():
    assert day01.part2([1721,979,366,299,675,1456]) == 241861950

def test_day02_part1():
    assert day02.part1(['1-3 a: abcde', '1-3 b: cdefg', '2-9 c: ccccccccc']) == 2

def test_day02_part2():
    assert day02.part2(['1-3 a: abcde', '1-3 b: cdefg', '2-9 c: ccccccccc']) == 1

day03_testmap = '''
..##.......
#...#...#..
.#....#..#.
..#.#...#.#
.#...##..#.
..#.##.....
.#.#.#....#
.#........#
#.##...#...
#...##....#
.#..#...#.#'''.strip()

def test_day03_part1():
    assert day03.part1(day03_testmap) == 7

def test_day03_part2():
    assert day03.part2(day03_testmap) == 336

day04_data = '''
ecl:gry pid:860033327 eyr:2020 hcl:#fffffd
byr:1937 iyr:2017 cid:147 hgt:183cm

iyr:2013 ecl:amb cid:350 eyr:2023 pid:028048884
hcl:#cfa07d byr:1929

hcl:#ae17e1 iyr:2013
eyr:2024
ecl:brn pid:760753108 byr:1931
hgt:179cm

hcl:#cfa07d eyr:2025 pid:166559648
iyr:2011 ecl:brn hgt:59in
'''.strip()

def test_day04_part1():
    assert day04.part1(day04_data) == 2

day04_validate_field = [
    ('byr', '2002', True),
    ('byr', '2003', False),
    ('hgt', '60in', True),
    ('hgt', '190cm', True),
    ('hgt', '190in', False),
    ('hgt', '190', False),
    ('hcl', '#123abc', True),
    ('hcl', '#123abz', False),
    ('hcl', '123abc', False),
    ('ecl', 'brn', True),
    ('ecl', 'wat', False),
    ('pid', '000000001', True),
    ('pid', '0123456789', False),
]

@pytest.mark.parametrize(['field', 'value', 'expected'], day04_validate_field)
def test_day04_validate_field(field, value, expected):
    assert bool(day04.validate_field(field, value)) == expected


day04_invalid_passports = '''
eyr:1972 cid:100
hcl:#18171d ecl:amb hgt:170 pid:186cm iyr:2018 byr:1926

iyr:2019
hcl:#602927 eyr:1967 hgt:170cm
ecl:grn pid:012533040 byr:1946

hcl:dab227 iyr:2012
ecl:brn hgt:182cm pid:021572410 eyr:2020 byr:1992 cid:277

hgt:59cm ecl:zzz
eyr:2038 hcl:74454a iyr:2023
pid:3556412378 byr:2007
'''.strip().split('\n\n')

@pytest.mark.parametrize('data', day04_invalid_passports)
def test_day04_invalid_passports(data):
    passport = day04.Passport(data)
    assert passport.fields_valid() == False

day04_valid_passports = '''
pid:087499704 hgt:74in ecl:grn iyr:2012 eyr:2030 byr:1980
hcl:#623a2f

eyr:2029 ecl:blu cid:129 byr:1989
iyr:2014 pid:896056539 hcl:#a97842 hgt:165cm

hcl:#888785
hgt:164cm byr:2001 iyr:2015 cid:88
pid:545766238 ecl:hzl
eyr:2022

iyr:2010 hgt:158cm hcl:#b6652a ecl:blu byr:1944 eyr:2021 pid:093154719
'''.strip().split('\n\n')

@pytest.mark.parametrize('data', day04_valid_passports)
def test_day04_valid_passports(data):
    passport = day04.Passport(data)
    assert passport.fields_valid() == True

day05_seats = [
    ('FBFBBFFRLR', 357),
    ('BFFFBBFRRR', 567),
    ('FFFBBBFRRR', 119),
    ('BBFFBBFRLL', 820),
]

@pytest.mark.parametrize(['seat', 'id'], day05_seats)
def test_day05_seats(seat, id):
    assert day05.seat_id(seat) == id

day06_example = '''abc

a
b
c

ab
ac

a
a
a
a

b'''

def test_day06_part1():
    assert day06.part1(day06_example) == 11

def test_day06_part2():
    assert day06.part2(day06_example) == 6

day07_example = '''light red bags contain 1 bright white bag, 2 muted yellow bags.
dark orange bags contain 3 bright white bags, 4 muted yellow bags.
bright white bags contain 1 shiny gold bag.
muted yellow bags contain 2 shiny gold bags, 9 faded blue bags.
shiny gold bags contain 1 dark olive bag, 2 vibrant plum bags.
dark olive bags contain 3 faded blue bags, 4 dotted black bags.
vibrant plum bags contain 5 faded blue bags, 6 dotted black bags.
faded blue bags contain no other bags.
dotted black bags contain no other bags.'''

def test_day07_part1():
    assert day07.part1(day07_example) == 4

def test_day07_part1_answer():
    assert day07.part1(open('input07.txt').read()) == 155

def test_day07_part2_1():
    assert day07.part2(day07_example) == 32

day07_example_2 = '''shiny gold bags contain 2 dark red bags.
dark red bags contain 2 dark orange bags.
dark orange bags contain 2 dark yellow bags.
dark yellow bags contain 2 dark green bags.
dark green bags contain 2 dark blue bags.
dark blue bags contain 2 dark violet bags.
dark violet bags contain no other bags.'''

def test_day07_part2_2():
    assert day07.part2(day07_example_2) == 126

def test_day07_part2_answer():
    assert day07.part2(open('input07.txt').read()) == 54803

day08_example = '''nop +0
acc +1
jmp +4
acc +3
jmp -3
acc -99
acc +1
jmp -4
acc +6'''

def test_day08_part1():
    assert day08.part1(day08_example) == 5

def test_day08_part2():
    assert day08.part2(day08_example) == 8

day09_example = '''35
20
15
25
47
40
62
55
65
95
102
117
150
182
127
219
299
277
309
576'''

def test_day09_part1():
    assert day09.part1(day09_example, 5) == 127

def test_day09_part2():
    assert day09.part2(day09_example, 5) == 62

day10_1 = '16 10 15 5 1 11 7 19 6 12 4'
day10_2 = '28 33 18 42 31 14 46 20 48 47 24 23 49 45 19 38 39 11 1 32 25 35 8 17 7 9 4 2 34 10 3'

def test_day10_part1a():
    assert day10.part1(day10_1) == 7 * 5

def test_day10_part1b():
    assert day10.part1(day10_2) == 22 * 10

def test_day10_part2a():
    assert day10.part2(day10_1) == 8

def test_day10_part2b():
    assert day10.part2(day10_2) == 19208

day11_example = '''L.LL.LL.LL
LLLLLLL.LL
L.L.L..L..
LLLL.LL.LL
L.LL.LL.LL
L.LLLLL.LL
..L.L.....
LLLLLLLLLL
L.LLLLLL.L
L.LLLLL.LL'''

def test_day11_part1():
    assert day11.part1(day11_example) == 37

def test_day11_part2():
    assert day11.part2(day11_example) == 26

day12_example = '''F10
N3
F7
R90
F11'''

def test_day12_part1():
    assert day12.part1(day12_example) == 25

def test_day12_part2():
    assert day12.part2(day12_example) == 286

day13_example = '''939
7,13,x,x,59,x,31,19'''

def test_day13_part1():
    assert day13.part1(day13_example) == 295

day13_part2_testcases = [
    ('7,13,x,x,59,x,31,19', 1068781),
    ('17,x,13,19', 3417),
    ('67,7,59,61', 754018),
    ('67,x,7,59,61', 779210),
    ('67,7,x,59,61', 1261476),
    ('1789,37,47,1889', 1202161486),
]

@pytest.mark.parametrize(('data', 'expected'), day13_part2_testcases)
def test_day13_part2(data, expected):
    assert day13.part2(data) == expected

def test_day13_Eq():
    assert day13.Eq(5, 7).simplify() == day13.Eq(5, 2)

def test_day13_LinearEqs_merge():
    # (x) mod 19 = 0
    # (x + 19) mod 523 = 0
    # => (x) mod 9937 = -19
    eqs = day13.LinearEqs([
        day13.Eq(19, 0),
        day13.Eq(523, 19),
    ])
    assert eqs.merge() == [day13.Eq(523*19, 19)]

    # (x + 9) mod 41 == 0
    # (x + 50) mod 853 == 0
    # => (x) mod 34973 == -50
    eqs = day13.LinearEqs([
        day13.Eq(41, 9),
        day13.Eq(853, 50),
    ])
    assert eqs.merge() == [day13.Eq(853*41, 50)]

    # (x + 19) mod 493 == 0
    # (x + 19) mod 37 == 0
    # => (x + 19) mod 18241 == -50
    eqs = day13.LinearEqs([
        day13.Eq(493, 19),
        day13.Eq(37, 19),
    ])
    assert eqs.merge() == [day13.Eq(493*37, 19)]

    # (x + 11) mod 13 == 0
    # (x + 50) mod 34973 == 0
    # => (x + 50) mod 454649 == 0
    eqs = day13.LinearEqs([
        day13.Eq(13, 37),
        day13.Eq(34973, 50),
    ])
    assert eqs.merge() == [day13.Eq(13*34973, 50)]
