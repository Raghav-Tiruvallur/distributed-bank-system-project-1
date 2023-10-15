import grpc
from example_pb2 import responseData
import example_pb2_grpc



class Branch(example_pb2_grpc.BankTransactionsServiceServicer):

    def __init__(self, id, balance, branches):
        # unique ID of the Branch
        self.id = id
        # replica of the Branch's balance
        self.balance = balance
        # the list of process IDs of the branches
        self.branches = branches
        # the list of Client stubs to communicate with the branches
        self.stubList = list()
        for branch in self.branches:
            _id = int(branch[len(branch) - 2 :])
            if _id == self.id:
                continue
            channel = grpc.insecure_channel(f'localhost:{branch}')
            stub = example_pb2_grpc.BankTransactionsServiceStub(channel)
            self.stubList.append(stub)
        # a list of received messages used for debugging purpose
        self.recvMsg = list()
        # iterate the processID of the branches

        # TODO: students are expected to store the processID of the branches
    def __reduce__(self):
        return (self.__class__,(self.id,self.balance,self.branches))
    
    def Query(self):
        return self.balance

    def Withdraw(self,request):
        self.balance -= request.event.money
        for stub in self.stubList:
            request.event.interface = "branch/withdraw"
            response = stub.MsgDelivery(request)
    def Deposit(self,request):
        self.balance += request.event.money
        for stub in self.stubList:
            request.event.interface = "branch/deposit"
            response = stub.MsgDelivery(request)
    def Propogate_Withdraw(self,amount):
        self.balance -= amount 
        return "success" #return success
        
    def Propogate_Deposit(self,amount):
        self.balance += amount
        return "success" #return success - the status of the request


    # TODO: students are expected to process requests from both Client and Branch
    def MsgDelivery(self,request, context):

        event = request.event
        response = None
        eventType = event.interface
        if eventType == "withdraw":
            response = self.Withdraw(request)
        elif eventType == "deposit":
            response = self.Deposit(request)
        elif eventType == "query":
            response = self.Query()
        else:
            propogateDirection = eventType.split('/')[1]
            if propogateDirection == "withdraw":
                response = self.Propogate_Withdraw(event.money)
                return responseData(interface= eventType,result = response)
            else:
                response = self.Propogate_Deposit(event.money)
                return responseData(interface= eventType,result = response)
        if response is not None:
            return responseData(interface = eventType,balance = response)
        return responseData(interface = eventType,result = "success")
        