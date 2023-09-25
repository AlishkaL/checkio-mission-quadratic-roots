"""
TESTS is a dict with all of your tests.
Keys for this will be the categories' names.
Each test is a dict with
    "input" -- input data for a user function
    "answer" -- your right answer
    "explanation" -- not necessarily a key, it's used for an additional info in animation.
"""


TESTS = {
    "Basics": [
        {"input": [1, -3, 2], "answer": (2, 1)},
        {"input": [1, 0, -1], "answer": (1, -1)},
        {"input": [1, 2, 1], "answer": (-1, -1)},
        {"input": [1, 0, 1], "answer": "No real roots"},
        {"input": [1, 4, 4], "answer": (-2, -2)},
        {"input": [1, -5, 6], "answer": (3, 2)},
        {"input": [1, -6, 9], "answer": (3, 3)},
        {"input": [2, 2, 1], "answer": "No real roots"},
        {"input": [2, -7, 6], "answer": (2, 1.5)},
        {"input": [2, -3, 1], "answer": (1, 0.5)},
    ],
    "Extra": [
        {"input": [1, 7, 15], "answer": "No real roots"},
        {"input": [1, -8, 15], "answer": (5, 3)}
    ]
}
