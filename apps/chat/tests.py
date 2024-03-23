"""
File use for chat test cases
"""
from django.core.management import call_command
from rest_framework.test import APITestCase
from django.urls import reverse
from rest_framework import status


class ChatTest(APITestCase):
    """
    Test case for testing random chat response api.
    """
    def setUp(self) -> None:
        """
        Set up the test environment.
        """
        self.url = reverse("chat:question-list")
        call_command('loaddata', 'fixtures/sentence_corpus.json')
        self.payload = {
            'question': 'what is your name?'
        }

    def test_with_valid_payload(self):
        """
        test case for valid payload
        """
        response = self.client.post(self.url, self.payload)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_with_empty_payload(self):
        """
        Test case for an empty payload
        """
        response = self.client.post(self.url, {})
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_with_missing_question_key(self):
        """
        Test case for missing 'question' key in payload
        """
        payload = {}
        response = self.client.post(self.url, payload)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_with_invalid_key(self):
        """
        Test case for missing 'question' key in payload
        """
        payload = {'ques': 'Why?'}
        response = self.client.post(self.url, payload)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_with_invalid_question(self):
        """
        Test case for an invalid question
        """
        payload = self.payload.copy()
        payload.update({'question': ''})
        response = self.client.post(self.url, payload)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_with_get_method(self):
        """
        Test case for accessing the endpoint with GET method
        """
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)

    def test_with_invalid_content_type(self):
        """
        Test case for sending request with invalid content type
        """
        response = self.client.post(self.url, self.payload, content_type='text/html')
        self.assertEqual(response.status_code, status.HTTP_415_UNSUPPORTED_MEDIA_TYPE)

