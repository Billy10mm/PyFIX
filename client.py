import zmq
import example_pb2

a = example_pb2.Example()
a.first_name = 'Billy'
a.last_name = '10mm'
a.age = 43
a.weight = 178

context = zmq.Context()
socket = context.socket(zmq.REQ)
socket.connect("tcp://127.0.0.1:61000")

socket.send(a.SerializeToString())
reply = socket.recv()
print(reply)
