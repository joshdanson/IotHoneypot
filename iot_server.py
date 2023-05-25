import logging
import asyncio
import random
from aiocoap import Context, Message, Code, numbers
import aiocoap.resource as resource

# define the host and port for the server and client
HOST = '0.0.0.0'
SERVER_PORT = 5683
CLIENT_PORT = 5684


# Creates a TemperatureResource that can be observed by a client. The resource is updated every 5 seconds.
class TemperatureResource(resource.ObservableResource):
    def __init__(self):
        super().__init__()
        self.temperature = 20
        self.handle = None

        # set up logging
        self.logger = logging.getLogger('TemperatureResource')
        self.logger.setLevel(logging.DEBUG)
        handler = logging.FileHandler('logs/temperature.log')
        handler.setLevel(logging.DEBUG)
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        handler.setFormatter(formatter)
        self.logger.addHandler(handler)

    # Returns the current temperature
    def get_temperature(self):
        self.temperature += random.uniform(-2, 2)
        return round(self.temperature, 2)

    # TODO: make this look like a real sensor

    # Handles a GET request
    async def render_get(self, request):
        temperature = self.get_temperature()
        payload = str(temperature).encode('utf-8')
        self.logger.debug("Temperature requested: %s", temperature)
        return Message(code=Code.CONTENT, payload=payload, mtype=numbers.types.CON)

async def main():
    # set up logging
    logging.basicConfig(filename='logs/server.log', level=logging.DEBUG,
                        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

    # create a server context and add a resource
    root = resource.Site()
    root.add_resource(['.well-known', 'core'], resource.WKCResource(root.get_resources_as_linkheader))
    root.add_resource(['temp'], TemperatureResource())

    await Context.create_server_context(root, bind=(HOST, SERVER_PORT))

    await asyncio.get_running_loop().create_future()


if __name__ == "__main__":
    asyncio.run(main())
