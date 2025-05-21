from src.views.http_types.http_response import HttpResponse
from src.errors.errors_types.http_bad_request_error import HttpBadRequest
from src.errors.errors_types.http_not_found_error import HttpNotFound
from src.errors.errors_types.http_unauthorized_error import HttpUnauthorized

def error_handler(error: Exception) -> HttpResponse:
    if isinstance (error, (HttpBadRequest, HttpNotFound, HttpUnauthorized)):
        return HttpResponse(
            body={
                "error":[{
                    "title": error.name,
                    "detail": error.message
                }]
            },
            status_code= error.status_code
        )
    return HttpResponse(
        body={
            "error":[{
                "title": "Server Error",
                "detail": str(error)
            }]
        },
        status_code= 500
    )
