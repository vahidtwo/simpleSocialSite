from django.http import JsonResponse
from django.http.response import HttpResponseServerError
import json
import inspect
have_length = (str, dict, tuple, set)
_return_types = (json, JsonResponse)
__chert_number = -11232222.1


def get(_json_data, _value, _label, _can_null=False, _type=str, _size=-1, _default=__chert_number,
        _return_type=JsonResponse):
    """
        An getter Helper for Validate data in Json
        :param _json_data: json obj that want data in it
        :param _value: that key we want for validate it
        :param _label: name for novalidate data response
        :param _can_null: allow key not found
        :param _type: type of data
        :param _size: size of data
        :param _default: if data not found , value that pass to it put in json with _value key
        :param _return_type: type of return , must be json or JsonResponse
        :returns : if data is validate return True and that validated data
                   if data is novalidate return False and JsonResponse that show reason of why data is novalidate
        writen by Vahid Imanian :
                    email : vahidtwo@gmail.com
    """
    if _return_type not in _return_types:
        return JsonResponse(data={
            'msg': 'return type must be json or JsonResponse'
        })
    data = _json_data.get(_value, None)
    if data is not None:
        if type(data)in have_length:
            if len(data) == 0:
                if _default == __chert_number:
                    data = None
                else:
                    data[_value] = _default
        else:
            if _default == __chert_number:
                data = data
            elif data is None and _default != __chert_number:
                data[_value] = _default
    if not _can_null:
        if data is None:
            if _return_type is JsonResponse:
                return False, JsonResponse(data={
                    'success': False,
                    'message': '{} ارسال نشده است.'.format(_label)
                }, safe=False, status=HttpResponseServerError)
            return False, json.dumps({
                    'success': False,
                    'message': '{} ارسال نشده است.'.format(_label)
                })

    if data is not None and type(data)in have_length:
        if _size != -1 and len(data) != _size:
            if _return_type is JsonResponse:
                return False, JsonResponse(data={
                    'success': False,
                    'message': '{} باید {} رقمی باشد.'.format(_label, _size)
                }, safe=False, status=HttpResponseServerError)
            return False, json.dumps({
                    'success': False,
                    'message': '{} باید {} رقمی باشد.'.format(_label, _size)
                })
    if data is not None:
        if type(data) is not _type:
            if _return_type == JsonResponse:
                return False, JsonResponse(data={
                    'success': False,
                    'message': '{} را باید از نوع {} باشد.'.format(_label, _type.__name__)
                }, safe=False, status=HttpResponseServerError)
            return False, json.dumps({
                    'success': False,
                    'message': '{} را باید از نوع {} باشد.'.format(_label, _type.__name__)
                })
    return True, data


def lineno():
    """Returns the current line number in our program."""
    return inspect.currentframe().f_back.f_lineno
