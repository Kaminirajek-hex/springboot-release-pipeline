import traceback
from fastapi import APIRouter, HTTPException
from business import sampleservice
from schema.sample import Sample

router = APIRouter(prefix="/sample")


@router.get('')
def api_fetch_sample():
    return sampleservice.fetch_sample()

@router.post('')
def api_insert_sample(sample: Sample):
    sampleservice.insert_sample(sample)
    return "success"

@router.put('/{id}')
def api_update_sample(id: int, sample: Sample):
    sampleservice.update_sample(id, sample)
    return "success"

@router.delete('/{id}')
def api_delete_sample(id: int):
    sampleservice.delete_sample(id)
    return "success"