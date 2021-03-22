from client import Client
from filter import Filter
import json

class DataBase():
    def __init__(self):
        self.instance = FileDataBase

    def getClients(self):
        return self.instance.getClients(self)

    def getFilters(self,client_id):
        return self.instance.getFilters(self,client_id)


class RemoteDataBase(DataBase):
    def getClients(self):
        pass

    def getFilters(self,client_id):
        pass


class FileDataBase(DataBase):
    def getClients(self):
        with open("clients.json") as c:
            clients = json.load(c)
        return clients

    def getFilters(self,client_id):
        with open("filters.json") as f:
            filters = json.load(f)

        ret = []

        for filter in filters:
            if filter.get("client_id") == client_id:
                ret.append(filter)

        return ret
