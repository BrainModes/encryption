from pydantic import BaseModel, Field
from .base_models import APIResponse


class POSTUserKey(BaseModel):
    user_geid: str
    user_public_key: str
    is_sandboxed: bool = False
    key_name: str = "default"


class POSTUserKeyResponse(APIResponse):
    result: dict = Field({}, example={
        'code': 200,
        'error_msg': '',
        'num_of_pages': 1,
        'page': 0,
        'result': 'success',
        'total': 1
    })


class GETUserKeyResponse(APIResponse):
    result: dict = Field({}, example={
        'code': 200,
        'error_msg': '',
        'num_of_pages': 1,
        'page': 0,
        'result': {'public_key': ''},
        'total': 1
    })


class GETServerKeyResponse(APIResponse):
    result: dict = Field({}, example={
        'code': 200,
        'error_msg': '',
        'num_of_pages': 1,
        'page': 0,
        'result': {'public_key': ''},
        'total': 1
    })
