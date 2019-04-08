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
            "input": 'example',
            "answer": 'm'
        },
        {
            "input": 'test',
            "answer": 'es'
        }
    ],
    "Extra": [
        {
            "input": '    few whitespaces   ',
            "answer": 'it'
        },
        {
            "input": 'very-very long sentence',
            "answer": 'o'
        },
	{
            "input": 'symbols are: !@#$%^&*()=',
            "answer": ': '
        },
	{
            "input": '*',
            "answer": '*'
        },
	{
            "input": 'Hi',
            "answer": 'Hi'
        }
    ]
}
