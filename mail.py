class Mail():
    def __init__(self, address_from, address_to):
        self.address_from = address_from
        self.address_to = address_to
        self.message = ""

    def add(self,resume):
        self.message += resume.message
