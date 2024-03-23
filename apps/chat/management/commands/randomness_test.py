"""
File used to test randomness of api response
"""
import os

from django.core.management.base import BaseCommand
import numpy as np
import randtest as rt
import requests

from apps.common.constants import CREATED_STATUS, NUM_SAMPLES


class Command(BaseCommand):
    """
    A management command to test the randomness of API responses.

    Usage:
    python manage.py test_api_randomness

    This command collects responses from the specified API endpoint and performs
    a randomness test on the collected data.
    """

    help = 'Test the randomness of API responses'

    def handle(self, *args, **kwargs):
        """
        Handle method to execute the command.

        Adjust the number of samples as needed using 'num_samples'.

        Args:
            *args: Additional positional arguments.
            **kwargs: Additional keyword arguments.
        """
        api_url = os.getenv('BASE_URL') + "/api/v1/chat/question/"
        num_samples = NUM_SAMPLES
        self.stdout.write("Collecting responses from API...")
        responses = self.collect_responses(api_url, num_samples)
        self.stdout.write("Performing randomness test...")
        # Perform randomness test on the collected responses
        randomness_score = self.perform_randomness_test(responses)
        # Print randomness: False if the sequence is ordered and
        # True if the sequence is random.
        self.stdout.write(self.style.SUCCESS(f"Randomness: {randomness_score}"))

    @staticmethod
    def collect_responses(api_url, num_samples):
        """
        Collect responses from the API endpoint.

        Args:
            api_url (str): The URL of the API endpoint.
            num_samples (int): The number of samples to collect.

        Returns:
            list: List of collected responses.
        """
        responses = []

        # Call the API multiple times and collect responses
        for _ in range(num_samples):
            response = requests.post(
                api_url, data={"question": "Testing randomness"}
            )
            if response.status_code == CREATED_STATUS:
                data = response.json()
                responses.append(data['detail'])

        return responses

    @staticmethod
    def perform_randomness_test(data):
        """
        Perform randomness test on the collected data.

        Args:
            data (list): List of collected responses.

        Returns:
            float: Randomness score.
        """
        # Convert data to numpy array
        data_array = np.array(data)
        # Perform randomness testing using randtest
        score = rt.random_score(data_array)
        return score

