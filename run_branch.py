from multiprocessing import Process
import grpc
from Branch import Branch
from example_pb2_grpc import add_BankTransactionsServiceServicer_to_server
import json
from concurrent.futures import ThreadPoolExecutor
from utils import getPort
import grpc



def serve(port,branchData):
    server = grpc.server(ThreadPoolExecutor(max_workers=10))
    add_BankTransactionsServiceServicer_to_server(branchData, server)
    server.add_insecure_port("[::]:" + port)
    server.start()
    print("Server started, listening on " + port)
    server.wait_for_termination()

def spawnBranchProcesses(branchData):
    processes = []
    for branch in branchData:
        port = getPort(branch.id)
        process = Process(target=serve,args=(port,branch))
        process.start()
        processes.append(process)
    for process in processes:
        process.join()




f = open("input.json")
input = json.load(f)



if __name__ == "__main__":
    processes = []
    branches = []
    balance = 0
    branchData = []
    for data in input:
        if data["type"] == "branch":
            id = data["id"]
            port = getPort(id)
            branches.append(port)
    for data in input:
        if data["type"] == "branch":
            id = data["id"]
            port = getPort(id)
            balance = data["balance"]
            branch = Branch(id,balance,branches)
            branchData.append(branch)

    spawnBranchProcesses(branchData)