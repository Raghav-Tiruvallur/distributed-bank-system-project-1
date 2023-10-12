import grpc
from example_pb2 import CustomerRequest
import json
import example_pb2_grpc
from google.protobuf.json_format import MessageToJson

from run_branch import getPort

class Customer:
    def __init__(self, id, events):
        # unique ID of the Customer
        self.id = id
        # events from the input
        self.events = events
        # a list of received messages used for debugging purpose
        self.recvMsg = list()
        # pointer for the stub
        self.stub = None

    # TODO: students are expected to create the Customer stub
    def createStub(self):
        port = getPort(self.id)
        channel = grpc.insecure_channel(f'localhost:{port}')
        stub = example_pb2_grpc.BankTransactionsServiceStub(channel)
        self.stub = stub

    # TODO: students are expected to send out the events to the Bank
    def executeEvents(self):
        for event in self.events:
            response = self.stub.MsgDelivery(CustomerRequest(id = self.id,event = event))
            response = json.loads(MessageToJson(response, preserving_proto_field_name = True))
            self.recvMsg.append(response)
        return self.recvMsg