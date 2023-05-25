# IOT Honeypot

## Overview
The IOT Honeypot project is a proof-of-concept for integrating a new honeypot into the TPOT-CE (T-Pot's Community Edition) framework. The project features a client-server model using Python's asyncio library and the aiocoap package, which allows for easy development of internet of things (IoT) devices using the Constrained Application Protocol (CoAP).

## Structure
This repository is structured as follows:
```
| archive/
# Old versions of the honeypot

| fixingLogsIotPot/
# Work-in-progress directory for logging improvements. Contains copies of iot_client.py and iot_server.py

| testingIOTPot/
# Directory storing the actual TPOT-CE files. Contains copies of iot_client.py and iot_server.py

| Dockerfile
# Dockerfile for building a Docker image for the project

| iot_client.py
# The client script for the honeypot

| iot_server.py
# The server script for the honeypot
```

## iot_client.py
The `iot_client.py` script is an asynchronous client built using Python's asyncio library and the aiocoap package. It sends a GET request to the server and receives a response containing the server's temperature data. The client also logs its actions using the standard Python logging module, with log entries saved to `logs/client.log`.

## iot_server.py
The `iot_server.py` script is an asynchronous server also built with Python's asyncio and aiocoap. It hosts a "temperature" resource that generates temperature data and responds to GET requests from clients. The server logs its actions, with log entries saved to `logs/server.log`.

## Running the Project
Before you run the client or server, ensure you have the required packages installed. These packages can be installed by running:

```bash
pip install aiocoap[all] asyncio
```

The client and server scripts can be run as standalone programs:

```bash
python iot_client.py
```

```bash
python iot_server.py
```

Remember, the server must be running before you start the client.

## Docker
A Dockerfile is provided for building a Docker image of the project. This allows the project to be run in a containerized environment, which can provide additional security and ease of deployment. The Docker image can be built by running:

```bash
docker build -t iot-honeypot .
```

And a container can be started from the image by running:

```bash
docker run -p 5683:5683 -p 5684:5684 iot-honeypot
```

This starts a container that hosts the server and exposes the server and client ports (5683 and 5684) to the host.

## Future Development
This project is a proof-of-concept and is still under development. Future updates may include improvements to logging, additional IoT device simulations, and full integration with the T-Pot's Community Edition framework.

## Contributions
Contributions to this project are welcome. Please feel free to open an issue or submit a pull request.

## License
This project is licensed under the MIT License. See the LICENSE file for details.