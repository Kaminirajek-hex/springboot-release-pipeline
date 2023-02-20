import unittest
from unittest import mock
from schema.sample import Sample as SampleSchema
from api.routes import app
from business import sampleservice

ENDPOINT = '/sample'
SUCCESS_MSG = '"success"'


class TestSampleService(unittest.TestCase):

    def setUp(self) -> None:
        self.sample = {
            'id': 1,
            'name': 'dpotX',
            'number': 
        }
        self.sample_list = [self.sample]
        self.sample_schema_obj = SampleSchema(**self.sample)
    
    @mock.patch('business.sampleservice.samplerepo.get_sample')
    def test_fetch_sample(self, mock_fetch):

        mock_fetch.return_value = self.sample_list

        out = sampleservice.fetch_sample()
        
        assert out == self.sample_list
        assert mock_fetch.called

    @mock.patch('business.sampleservice.samplerepo.insert_sample')
    def test_api_insert_sample(self, mock_insert):

        mock_insert.return_value = None

        out = sampleservice.insert_sample(self.sample_schema_obj)
        
        assert mock_insert.called
        assert out == None


    @mock.patch('business.sampleservice.samplerepo.update_sample')
    def test_api_update_sample(self, mock_update):

        mock_update.return_value = None

        out = sampleservice.update_sample(1, self.sample_schema_obj)
        
        assert mock_update.called
        assert out == None

    @mock.patch('business.sampleservice.samplerepo.delete_sample')
    def test_api_delete_sample(self, mock_delete):

        mock_delete.return_value = None

        out = sampleservice.delete_sample(1)
        
        assert mock_delete.called
        assert out == None
