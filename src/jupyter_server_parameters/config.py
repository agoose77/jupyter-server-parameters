from traitlets import default, Callable
from traitlets.config import LoggingConfigurable

from .utils import maybe_future


class JupyterServerParameters(LoggingConfigurable):
    handle_parameters_hook = Callable(
        help="""
        An optional hook function that you can implement to handle parameters 
        passed to the `/parameters` endpoint. This maybe a coroutine.
        Example::
            def my_hook(self, parameters):
                self.log.info(f"The secret key is {parameters['key']}")
            c.JupyterServerParameters.handle_parameters_hook = my_hook
        """
    ).tag(config=True)

    @default("handle_parameters_hook")
    def _handle_parameters_hook_default(self, _, params):
        self.log.debug(f"Received {params!r} parameters")

    async def handle_parameters(self, params):
        await maybe_future(self.handle_parameters_hook(self, params))
