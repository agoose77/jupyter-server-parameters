import inspect
import asyncio
import concurrent.futures


# Copied from jupyterhub/utils.py
def maybe_future(obj):
    """Return an asyncio Future
    Use instead of gen.maybe_future
    For our compatibility, this must accept:
    - asyncio coroutine (gen.maybe_future doesn't work in tornado < 5)
    - tornado coroutine (asyncio.ensure_future doesn't work)
    - scalar (asyncio.ensure_future doesn't work)
    - concurrent.futures.Future (asyncio.ensure_future doesn't work)
    - tornado Future (works both ways)
    - asyncio Future (works both ways)
    """
    if inspect.isawaitable(obj):
        # already awaitable, use ensure_future
        return asyncio.ensure_future(obj)
    elif isinstance(obj, concurrent.futures.Future):
        return asyncio.wrap_future(obj)
    else:
        # could also check for tornado.concurrent.Future
        # but with tornado >= 5.1 tornado.Future is asyncio.Future
        f = asyncio.Future()
        f.set_result(obj)
        return f
