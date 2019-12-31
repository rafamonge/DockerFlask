from functools import wraps
from flask import request, abort

# based on https://github.com/ericsopa/flask-api-key/blob/master/hello.py
## using a dummy key here, should migrate to certificate based system like in the file.

# The actual decorator function
def require_appkey(view_function):
    @wraps(view_function)
    # the new, post-decoration function. Note *args and **kwargs here.
    def decorated_function(*args, **kwargs):
        api_key = request.headers.get('x-api-key')
        if api_key == "abcdefg":
            return view_function(*args, **kwargs)
        else:
            abort(401)
    return decorated_function