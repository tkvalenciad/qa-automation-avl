LOGIN_SUCCESS_SCHEMA = {
    "type": "object",
    "required": [
        "id",
        "username",
        "email",
        "firstName",
        "lastName",
        "accessToken",
        "refreshToken",
    ],
    "properties": {
        "id": {"type": "integer"},
        "username": {"type": "string"},
        "email": {"type": "string"},
        "firstName": {"type": "string"},
        "lastName": {"type": "string"},
        "gender": {"type": "string"},
        "image": {"type": "string"},
        "accessToken": {"type": "string"},
        "refreshToken": {"type": "string"},
    },
    "additionalProperties": True,
}

LOGIN_ERROR_SCHEMA = {
    "type": "object",
    "required": ["message"],
    "properties": {
        "message": {"type": "string"},
    },
    "additionalProperties": True,
}
