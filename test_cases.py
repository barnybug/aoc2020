import pytest
import day01, day02, day03, day04, day05, day06, day07, day08, day09, day10
import day11, day12, day13, day14, day15, day16, day17, day18, day19

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
    ('19,x,x,x,x,x,x,x,x,41,x,x,x,x,x,x,x,x,x,523,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,17,13,x,x,x,x,x,x,x,x,x,x,29,x,853,x,x,x,x,x,37,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,23', 210612924879242),
]

@pytest.mark.parametrize(('data', 'expected'), day13_part2_testcases)
def test_day13_part2(data, expected):
    assert day13.part2(data) == expected

def test_day13_chinese_remainder_theorem():
    assert day13.chinese_remainder_theorem([(1,3),(4,5),(6,7)]) == 34

day14_example = '''mask = XXXXXXXXXXXXXXXXXXXXXXXXXXXXX1XXXX0X
mem[8] = 11
mem[7] = 101
mem[8] = 0'''

def test_day14_part1():
    assert day14.part1(day14_example) == 165

day14_example_2 = '''mask = 000000000000000000000000000000X1001X
mem[42] = 100
mask = 00000000000000000000000000000000X0XX
mem[26] = 1'''

def test_day14_part2():
    assert day14.part2(day14_example_2) == 208

def test_day15_part1():
    assert day15.part1([0,3,6]) == 436
    assert day15.part1([1,3,2]) == 1
    assert day15.part1([2,1,3]) == 10
    assert day15.part1([1,2,3]) == 27
    assert day15.part1([2,3,1]) == 78
    assert day15.part1([3,2,1]) == 438
    assert day15.part1([3,1,2]) == 1836

def test_day15_part2():
    assert day15.part2([0,3,6]) == 175594

day16_example = '''class: 1-3 or 5-7
row: 6-11 or 33-44
seat: 13-40 or 45-50

your ticket:
7,1,14

nearby tickets:
7,3,47
40,4,50
55,2,20
38,6,12'''

def test_day16_part1():
    assert day16.part1(day16_example) == 71

day16_example_2 = '''class: 0-1 or 4-19
row: 0-5 or 8-19
seat: 0-13 or 16-19

your ticket:
11,12,13

nearby tickets:
3,9,18
15,1,5
5,14,9'''

def test_day16_part2():
    assert day16.field_order(day16_example_2) == ['row', 'class', 'seat']

day17_example = '''.#.
..#
###'''

def test_day17_part1():
    assert day17.part1(day17_example) == 112

def test_day17_part2():
    assert day17.part2(day17_example) == 848

day18_part1_cases = [
    ('1 + 2 * 3 + 4 * 5 + 6', 71),
    ('1 + (2 * 3) + (4 * (5 + 6))', 51),
    ('2 * 3 + (4 * 5)', 26),
    ('5 + (8 * 3 + 9 + 3 * 4 * 3)', 437),
    ('5 * 9 * (7 * 3 * 3 + 9 * 3 + (8 + 6 * 4))', 12240),
    ('((2 + 4 * 9) * (6 + 9 * 8 + 6) + 6) + 2 + 4 * 2', 13632),
]

@pytest.mark.parametrize(['expression', 'value'], day18_part1_cases)
def test_day18_part1(expression, value):
    assert day18.part1(expression) == value

day18_part2_cases = [
    ('1 + 2 * 3 + 4 * 5 + 6', 231),
    ('1 + (2 * 3) + (4 * (5 + 6))', 51),
    ('2 * 3 + (4 * 5)', 46),
    ('5 + (8 * 3 + 9 + 3 * 4 * 3)', 1445),
    ('5 * 9 * (7 * 3 * 3 + 9 * 3 + (8 + 6 * 4))', 669060),
    ('((2 + 4 * 9) * (6 + 9 * 8 + 6) + 6) + 2 + 4 * 2', 23340),
]

@pytest.mark.parametrize(['expression', 'value'], day18_part2_cases)
def test_day18_part2(expression, value):
    assert day18.part2(expression) == value

day19_example = '''0: 4 1 5
1: 2 3 | 3 2
2: 4 4 | 5 5
3: 4 5 | 5 4
4: "a"
5: "b"

ababbb
bababa
abbbab
aaabbb
aaaabbb'''

def test_day19_part1():
    assert day19.part1(day19_example) == 2
