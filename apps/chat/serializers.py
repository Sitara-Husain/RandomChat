"""
Questions related serializer
"""

# django import
from rest_framework import serializers

# Local imports
from apps.common.messages import VALIDATION, CHAR_LIMIT_SIZE
from apps.common.utils import RandomResponse


class QuestionSerializer(serializers.Serializer):
    """
    Serializer class used to receive question from user
    and generate response accordingly.
    """
    question = serializers.CharField(
        max_length=CHAR_LIMIT_SIZE['max_question_length'],
        required=True, allow_blank=False,
        error_messages=VALIDATION['question']
    )

    def save(self):
        """
        Create a chat instance.
        Args:
            self (dict): self request.
        """
        response, sentence_id = RandomResponse.generate_random_response()
        return response, sentence_id



