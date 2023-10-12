import grpc
import json
import example_pb2
import example_pb2_grpc
from run_branch import getPort
from Customer import Customer

# def run_client():
#     channel = grpc.insecure_channel('localhost:50001')
#     stub = example_pb2_grpc.GreeterStub(channel)
#     response = stub.SayHello(example_pb2.HelloRequest(name='Raghav'))
#     print('Received from server:', response.message)

f = open("input.json")
input = json.load(f)


if __name__ == '__main__':
    output = []
    for data in input:
        if data["type"] == "customer":
            id = int(data["id"])
            events = data["events"]
            customer = Customer(id,events)
            customer.createStub()
            messagesRecieved = customer.executeEvents()
            outputData = {"id" : id, "recv" : messagesRecieved}
            output.append(outputData)
    with open("output.json", "w") as json_file:
        json_file.write("[\n")
        for i, item in enumerate(output):
            json_file.write(json.dumps(item, indent=4))
            if i < len(output) - 1:
                json_file.write(",\n")  
            else:
                json_file.write("\n")
        json_file.write("]\n")
            
    

