"""
This file used for common purpose for whole project
"""
import random

from rest_framework.response import Response
from rest_framework import status

from apps.chat.models import SentenceCorpus
from apps.common.constants import NUM
from apps.common.messages import NO_RESPONSE


class CustomResponse:
    """
    To create class for success and error response
    """
    def __init__(self, status: int, detail=None):
        """
        To set status & detail
        """
        self.status = status
        self.detail = detail

    @staticmethod
    def _get_validate_error_string(errors):
        """
        To Get string for error
        :param errors: list
        :return: string
        """
        detail_error = list(errors.values())[0]
        if isinstance(detail_error, list):
            detail_error = detail_error[0]
        if isinstance(detail_error, dict):
            detail_error = list(detail_error.values())[0]
        return detail_error

    def success_response(self, data=None, **kwargs):
        """
        function is used for getting same global response for all api
        :param data: data
        :return: Json response
        """
        code = self.status if self.status else status.HTTP_200_OK

        response_data = {"detail": self.detail, "data": data}
        return Response(response_data, status=int(code), **kwargs)

    def error_response(self, **kwargs):
        """
        function is used for getting same global error response
        for all api
        :return: Json response
        """
        error = self.detail
        detail = error
        if isinstance(self.detail, str):
            error = None
        else:
            detail = self._get_validate_error_string(error)

        code = self.status if self.status else status.HTTP_400_BAD_REQUEST

        return Response(
            {"detail": detail, 'error': error},
            status=int(code),
            **kwargs
        )


class RandomResponse:
    """
    This class is for random responses
    """

    @staticmethod
    def generate_random_response():
        """
        Generate random response for a question
        :return: random_sentence
        """
        try:
            sentence_count = SentenceCorpus.objects.all().count()
            random_offset = random.randint(NUM['zero'], sentence_count - NUM['one'])
            random_ins = SentenceCorpus.objects.all()[random_offset]
            random_sentence = random_ins.sentence
            sentence_id = random_ins.id
        except Exception as error:
            _ = error
            random_sentence = NO_RESPONSE
            sentence_id = None
        return random_sentence, sentence_id
