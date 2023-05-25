import asyncio
from aiocoap import Context, Message, Code, numbers
import logging

HOST = '127.0.0.1'
SERVER_PORT = 5683
CLIENT_PORT = 5684

async def main():
    # set up logging
    logging.basicConfig(filename='logs/client.log', level=logging.DEBUG,
                        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    logger = logging.getLogger('iot_client')

    # create a client context
    protocol = await Context.create_client_context()

    # create a request to send to the server
    request = Message(code=Code.GET, uri='coap://{}:{}/temp'.format(HOST, SERVER_PORT))
    logger.debug("Sending request to server")

    # send the request and wait for the response
    try:
       response = await protocol.request(request).response
       logger.debug("Received response from server")
    except Exception as e:
       logger.error("Failed to fetch resource: %s", e)
       print('Failed to fetch resource:')
       print(e)
    else:
      logger.info("Received response from server: %s", response.payload.decode())
      print('Result: %s\n%r'%(response.code, response.payload))

    # print the response payload
    print("Temperature:", response.payload.decode())

if __name__ == "__main__":
    asyncio.run(main())
