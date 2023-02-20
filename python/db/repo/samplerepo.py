from db.models.sample import Sample
from db.session import get_session


def get_sample():
    with get_session() as session:
        return session.query(Sample).all()

def insert_sample(sample):
    with get_session() as session:
        session.add(sample)
        session.commit()

def update_sample(id, schema_sample):
    with get_session() as session:
        sample = session.get(Sample, id)
        for key, value in schema_sample.items():
            setattr(sample, key, value)
        session.commit()

def delete_sample(id):
    with get_session() as session:
        sample = session.get(Sample, id)
        session.delete(sample)
        session.commit()
        
