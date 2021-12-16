import solve
import utils


def test_parse_signal_data_empty():
    line = ""

    signals, outputs = utils.parse_signal_data(line)

    assert not signals
    assert not outputs


def test_parse_signal_data():
    line = (
        "acedgfb cdfbe gcdfa fbcad dab cefabd cdfgeb eafb cagedb ab | "
        "cdfeb fcadb cdfeb cdbaf")

    signals, outputs = utils.parse_signal_data(line)

    assert signals == [
        "acedgfb", "cdfbe", "gcdfa", "fbcad", "dab", "cefabd", "cdfgeb",
        "eafb", "cagedb", "ab"]
    assert outputs == ["cdfeb", "fcadb", "cdfeb", "cdbaf"]


def test_translate_by_count_unrecognized():
    output_value = "a"

    digits = utils.translate_by_count(output_value)

    assert digits == []


def test_translate_by_count_single_digit():
    output_value = "ab"

    digits = utils.translate_by_count(output_value)

    assert digits == [1]


def test_translate_by_count_multiple_digit():
    output_value = "abcde"

    digits = utils.translate_by_count(output_value)

    assert digits == [2, 3, 5]


def test_part1_sample_input():
    sample_input = [
        "be cfbegad cbdgef fgaecd cgeb fdcge agebfd fecdb fabcd edb | fdgacbe cefdb cefbgd gcbe",
        "edbfga begcd cbg gc gcadebf fbgde acbgfd abcde gfcbed gfec | fcgedb cgb dgebacf gc",
        "fgaebd cg bdaec gdafb agbcfd gdcbef bgcad gfac gcb cdgabef | cg cg fdcagb cbg",
        "fbegcd cbd adcefb dageb afcb bc aefdc ecdab fgdeca fcdbega | efabcd cedba gadfec cb",
        "aecbfdg fbg gf bafeg dbefa fcge gcbea fcaegb dgceab fcbdga | gecf egdcabf bgf bfgea",
        "fgeab ca afcebg bdacfeg cfaedg gcfdb baec bfadeg bafgc acf | gebdcfa ecba ca fadegcb",
        "dbcfg fgd bdegcaf fgec aegbdf ecdfab fbedc dacgb gdcebf gf | cefg dcbef fcge gbcadfe",
        "bdfegc cbegaf gecbf dfcage bdacg ed bedf ced adcbefg gebcd | ed bcgafe cdgba cbgef",
        "egadfb cdbfeg cegd fecab cgb gbdefca cg fgcdab egfdb bfceg | gbdfcae bgc cg cgb",
        "gcafb gcf dcaebfg ecagb gf abcdeg gaef cafbge fdbac fegbdc | fgae cfgab fg bagce",
    ]

    result = solve.part_1(sample_input)

    assert result == 26
