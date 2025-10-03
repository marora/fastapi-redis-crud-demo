def response(data=None, status=200, error=None):
    return {
        "status": status,
        "data": data,
        "error": error
    }
