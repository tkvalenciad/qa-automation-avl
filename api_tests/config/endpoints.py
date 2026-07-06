JSONPLACEHOLDER_POSTS = "/posts"


def jsonplaceholder_post(post_id: int) -> str:
    return f"{JSONPLACEHOLDER_POSTS}/{post_id}"


DUMMYJSON_LOGIN = "/auth/login"
