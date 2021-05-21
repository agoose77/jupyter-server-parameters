from jupyter_server.base.handlers import JupyterHandler
from urllib.parse import urljoin
import tornado.web


class ParametersHandler(JupyterHandler):
    @tornado.web.authenticated
    async def get(self, *args):
        params = {k: self.get_argument(k) for k in self.request.arguments}

        # Swallow out parameters URL
        redirect = params.pop("redirect", "/lab")

        # Send parameter values to server_params
        server_params = self.settings["server_params"]
        try:
            await server_params.handle_parameters(params)
        except Exception:
            self.log.exception("Unable to handle parameters")

        # Perform redirect
        self.redirect(urljoin(self.base_url, redirect))
