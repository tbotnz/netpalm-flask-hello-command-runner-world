# netpalm-flask-hello-world
simple hello world command running webapp talking to network device via netpalm

![netpalm auto ingest](/flask-netpalm-hello-world.gif)

### getting started
- ensure you have a [netpalm](https://github.com/tbotnz/netpalm) container running
- git clone the project ``` git clone https://github.com/tbotnz/netpalm-flask-hello-world.git && cd netpalm-hello-world ```
- update the app.py with your ```NETPALM_SERVER_IP``` ```NETPALM_SERVER_PORT``` ```NETPALM_API_KEY```
- install the requirements ```pip3 install -r requirements.txt```
- run the app ```python3 app.py```
