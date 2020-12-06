import pytest
import day01, day02, day03, day04, day05, day06

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
