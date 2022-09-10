# 0 - Smoke Test



## Problem statement

From [the original challenge page](https://protohackers.com/problem/0):
> Deep inside Initrode Global's enterprise management framework lies a component that writes data to a server and expects to read the same data back. (Think of it as a kind of distributed system delay-line memory). We need you to write the server to echo the data back.

### Requirements

Your program will implement the TCP Echo Service from [RFC 862](https://www.rfc-editor.org/rfc/rfc862.html).

1. Accept TCP connections.

2. Whenever you receive data from a client, send it back unmodified.

3. Make sure you don't mangle binary data, and that you can handle at least 5 simultaneous clients.

4. Once the client has finished sending data to you it shuts down its sending side. Once you've reached end-of-file on your receiving side, and sent back all the data you've received, close the socket so that the client knows you've finished.

## Running the server

`server.py` requires Python 3.8 or higher to run but otherwise has no dependencies. By default, the server listens on all interfaces to port 1024.

```shell
$ python server.py
2022-09-10 20:23:08 INFO     online - serving from 0.0.0.0:1024
```

In a separate terminal session, use netcat to send data and receive responses:

```shell
$ echo "foo" | nc localhost 1024
foo
```

### With Docker

For convenience, you can use the distributed Dockerfile to build a `tcp-server` image:

```sh
$ docker build . -t tcp-server:0.0.0
$ docker run tcp-server:0.0.0
```
