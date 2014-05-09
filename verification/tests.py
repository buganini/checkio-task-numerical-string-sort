"""
TESTS is a dict with all you tests.
Keys for this will be categories' names.
Each test is dict with
    "input" -- input data for user function
    "answer" -- your right answer
    "explanation" -- not necessary key, it's using for additional info in animation.
"""

"""
def tryint(s):
    try:
        return int(s)
    except:
        return s

def natsort_key(s):
    return [ tryint(c) for c in re.split(r"((?:(?:(?<=[ ,])|^)-)?[0-9]+)", s) ]

def checkio(a):
    return sorted(a, key=natsort_key)
"""

TESTS = {
    "Basics": [
        {
            "input": ['01', '10', '100', '20', '3'],
            "answer": ['01', '3', '10', '20', '100'],
        },
        {
            "input": ['c', 'd', 'A', 'Z', 'z'],
            "answer": ['A', 'Z', 'c', 'd', 'z'],
        },
    ],
    "Decimal fractions": [
        {
            "input": ['0.0', '10.0', '0.01', '1.0', '2.0'],
            "answer": ['0.0', '0.01', '1.0', '2.0', '10.0'],
        },
    ],
    "Negative Sign": [
        {
            "input": ['01', '10', '100', '20', '3', '-01', '-10', '-100', '-20', '-3'],
            "answer": ['-100', '-20', '-10', '-3', '-01', '01', '3', '10', '20', '100'],
        },
        {
            "input": ['0.0', '10.0', '0.01', '1.0', '2.0', '-10.0', '-0.01', '-1.0', '-2.0'],
            "answer": ['-10.0', '-2.0', '-1.0', '0.0', '0.01', '-0.01', '1.0', '2.0', '10.0'],
        },
    ],
    "Complex": [
        {
            "input": ['01a', '10d', '100aa', '20Z', '-3', '01b', '10c', '100a', '20z', '3'],
            "answer": ['-3', '01a', '01b', '3', '10c', '10d', '20Z', '20z', '100a', '100aa'],
        },
        {
            "input": ["121.6114,25.0411.jpg", "121.5643,25.034.jpg", "-157.8601,21.3053.jpg"],
            "answer": ['-157.8601,21.3053.jpg', '121.5643,25.034.jpg', '121.6114,25.0411.jpg'],
        },
        {
            "input": ["1.0a","10.0a","2.0b","2.0a","0.1"],
            "answer": ['0.1', '1.0a', '2.0a', '2.0b', '10.0a'],
        }
    ]
}
