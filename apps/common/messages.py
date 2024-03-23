"""
Messages used in project
"""
# To define char limit
CHAR_LIMIT_SIZE = {
    'max_question_length': 1000,
}

VALIDATION = {
    'question': {
        "blank": "Please provide a question.",
        "invalid": "Invalid question format.",
        "min_length": "Question must be at least {limit_value} characters long.",
        "max_length": "Question must be at most {limit_value} characters long.",
        "required": "Question is required."
    },
}

NO_RESPONSE = "No response to display."
