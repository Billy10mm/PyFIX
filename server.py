#!/home/billy/miniconda3/bin/python -u

import zmq
import example_pb2

context = zmq.Context()
socket = context.socket(zmq.REP)
socket.bind("tcp://127.0.0.1:61000")

while True:
    example = example_pb2.Example()
    a = example.FromString(socket.recv())
    print(a.first_name)
    socket.send(b"got it")
