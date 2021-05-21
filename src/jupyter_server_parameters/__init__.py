from jupyter_server.utils import url_path_join

from .config import JupyterServerParameters
from .handlers import ParametersHandler


def _load_jupyter_server_extension(app):
    """
    This function is called when the extension is loaded.
    """
    app.web_app.settings["server_params"] = JupyterServerParameters(parent=app)

    handlers = [
        (
            url_path_join(app.web_app.settings["base_url"], "/parameters"),
            ParametersHandler,
        )
    ]
    app.web_app.add_handlers(".*$", handlers)


def _jupyter_server_extension_points():
    """
    Returns a list of dictionaries with metadata describing
    where to find the `_load_jupyter_server_extension` function.
    """
    return [{"module": "jupyter_server_parameters"}]
