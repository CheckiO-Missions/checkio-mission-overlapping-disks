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
        {
            "input": [[(0, 0, 3), (6, 0, 3), (6, 6, 3), (0, 6, 3)]],
            "answer": 4,
        },
        {
            "input": [[(4, -1, 3), (-3, 3, 2), (-3, 4, 2), (3, 1, 4)]],
            "answer": 2,
        },
        {
            "input": [[(-10, 6, 2), (6, -4, 5), (6, 3, 5), (-9, -8, 1), (1, -5, 3)]],
            "answer": 2,
        },
        {
            "input": [[(x, x, x//2) for x in range(2, 101)]],
            "answer": 2563,
        },
    ],
    "Extra": [
        {
            "input": [[(5, 10, 3), (15, -2, 7), (-3, 8, 4), (20, 5, 6), (0, 0, 2), (-10, 15, 9), (8, -6, 5), (12, 12, 3), (-5, -3, 6), (7, 7, 2)]],
            "answer": 5,
        },
        {
            "input": [[ (-8, -4, 5), (6, 3, 2), (-12, 10, 8), (18, -7, 4), (2, 6, 3), (-5, 2, 7), (14, 9, 5), (0, 0, 4), (-10, -12, 6), (9, -3, 2)]],
            "answer": 8,
        },
        {
            "input": [[ (3, -8, 6), (-7, 14, 5), (9, 2, 3), (-2, 10, 7), (6, -6, 4), (-5, 7, 2),(12, -3, 8), (-9, 5, 3), (0, 0, 5), (15, 1, 6)]],
            "answer": 14,
        },
    ]
}
