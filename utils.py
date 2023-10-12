def getPort(id):
    port = "500"
    if id < 10:
        port += "0"
    port += str(id)
    return port