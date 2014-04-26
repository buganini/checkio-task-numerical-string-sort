"""
TESTS is a dict with all you tests.
Keys for this will be categories' names.
Each test is dict with
    "input" -- input data for user function
    "answer" -- your right answer
    "explanation" -- not necessary key, it's using for additional info in animation.
"""


TESTS = {
    "Basics": [
        {
            "input": ["01","10","100","20","3"],
            "answer": ['01', '3', '10', '20', '100'],
            "explanation": "Sort numerical string"
        },
        {
            "input": ["1.0a","10.0a","2.0b","2.0a","0.1"],
            "answer": ['0.1', '1.0a', '2.0a', '2.0b', '10.0a'],
            "explanation": "Sort numerical string mixed with text"
        }
    ],
}
