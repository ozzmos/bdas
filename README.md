# bdas

Application to interact with a DAS.

Current release :  [v0.4.1](https://github.com/UMONS-GFA/bdas/releases/tag/v0.4.1) (October 2014)


### Requirements on server side

* Python 3
* python3-serial

You also need to configure a **settings.py** file (see below)

### Requirements on client side

* Python 3

[Read the wiki](https://github.com/UMONS-GFA/bdas/wiki)

### Procedure

Launch **simpleDASttytunnel.py** on server then **client2.py** on client for access to a DAS connected by serial on the server(LocalHost).
Launch  **DAStunnel.py** (or **simpleDAStunnel.py** if you do not have access to netcat) on server then **client2.py** on client for access to a DAS on a remote network (RemoteHost) accessible by the server.

**Remark :** Communication between client and local host might be restricted to communications within a private network. In such a case make sure to connect your client through a VPN connection before running client.py.

### Settings configuration (in settings.py):
```

LocalHost = 'IP_ADRESS'
LocalPort = NUM_PORT
RemoteHost = 'IP_ADRESS'
RemotePort = NUM_PORT
DefaultNetid = '255'
DefaultConnectionType = 'Serial'
DefaultConnectionDev = '/dev/ttyUSB0'
EOL = b'\r'

```

