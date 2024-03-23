"""
This file contains chat related views
"""
# Django imports
from rest_framework.viewsets import GenericViewSet
from rest_framework import mixins, status

# Local imports
from apps.chat.models import SentenceCorpus
from apps.chat.serializers import QuestionSerializer
from apps.common.utils import CustomResponse


class QuestionViewSet(
    GenericViewSet,
    mixins.CreateModelMixin
):
    """
    This class handles asked questions to give responses
    """
    http_method_names = ('post', )
    serializer_class = QuestionSerializer
    queryset = SentenceCorpus

    def create(self, request, *args, **kwargs):
        """
        To create the response for a question
        :param request: post request object
        :param args: arguments
        :param kwargs: key arguments
        :return: json response
        """
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            random_response, sentence_id = serializer.save()
            # return success message
            return CustomResponse(
                status.HTTP_201_CREATED, sentence_id,
            ).success_response(data={'response': random_response})
        return CustomResponse(status.HTTP_400_BAD_REQUEST, serializer.errors).error_response()
