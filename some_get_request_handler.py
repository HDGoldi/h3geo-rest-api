from fastapi.responses import JSONResponse


def handle_get_endpoint():
    return JSONResponse(status_code=200, content={"message": "OK"})
