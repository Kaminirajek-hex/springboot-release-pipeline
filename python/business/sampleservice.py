from schema import sample as SchemaSample
from db.models.sample import Sample
from db.repo import samplerepo


def fetch_sample():
    return samplerepo.get_sample()

def insert_sample(schema_sample):
    sample = Sample(**schema_sample.dict())
    samplerepo.insert_sample(sample)

def update_sample(id, schema_sample):
    sample = schema_sample.dict()
    del sample['id']
    samplerepo.update_sample(id, sample)

def delete_sample(id):
    samplerepo.delete_sample(id)