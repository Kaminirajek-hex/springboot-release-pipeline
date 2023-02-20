import json
import unittest
from unittest import mock
from fastapi.testclient import TestClient
from api.routes import app
from schema.sample import Sample
from core.logger import logger

ENDPOINT = '/sample'
SUCCESS_MSG = '"success"'


class TestSampleAPI(unittest.TestCase):

    def setUp(self) -> None:
        self.sample = {
            'id': 1,
            'name': 'qgWf0',
            'number': 
        }
        self.sample_list = [self.sample]
        self.client = TestClient(app)
        logger.disabled = True

    @mock.patch('api.sampleapi.sampleservice.fetch_sample')
    def test_api_fetch_sample(self, mock_fetch):

        mock_fetch.return_value = self.sample_list

        response = self.client.get(ENDPOINT)
        response_content = json.loads(response.content.decode('utf-8'))

        assert response.status_code == 200
        assert response_content == self.sample_list

    @mock.patch('api.sampleapi.sampleservice.insert_sample')
    def test_api_insert_sample(self, mock_insert):

        mock_insert.return_value = self.sample_list
        sample = Sample(**self.sample)
        print(sample)

        response = self.client.post(ENDPOINT, data = json.dumps(self.sample))
        response_content = response.content.decode('utf-8')

        assert response_content == SUCCESS_MSG
        assert mock_insert.called

    @mock.patch('api.sampleapi.sampleservice.update_sample')
    def test_api_update_sample(self, mock_update):

        mock_update.return_value = self.sample_list

        response = self.client.put(f'{ENDPOINT}/1', data = json.dumps(self.sample))
        response_content = response.content.decode('utf-8')

        assert response_content == SUCCESS_MSG
        assert mock_update.called

    @mock.patch('api.sampleapi.sampleservice.delete_sample')
    def test_api_delete_sample(self, mock_delete):

        mock_delete.return_value = self.sample_list

        response = self.client.delete(f'{ENDPOINT}/1')
        response_content = response.content.decode('utf-8')

        assert response.status_code == 200
        assert response_content == SUCCESS_MSG
        assert mock_delete.called
