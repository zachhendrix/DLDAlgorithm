class Package(object):
    objectid = ''
    address = ''
    city = ''
    state = ''
    zipcode = ''
    deadline = ''
    weight = ''
    status = ''
    message = ''

    def __init__(self, con_id, con_address, con_city, con_state, con_zip, con_deadline, con_weight, con_status, con_message):
        self.objectid = con_id
        self.address = con_address
        self.city = con_city
        self.state = con_state
        self.zipcode = con_zip
        self.deadline = con_deadline
        self.weight = con_weight
        self.status = con_status
        self.message = con_message

    def __str__(self):
        return self.objectid, self.address

    def get_id(self):
        return self.objectid

    def get_address(self):
        return self.address

    def set_address(self, address):
        self.address = address

    def get_city(self):
        return self.city

    def get_state(self):
        return self.state

    def get_zipcode(self):
        return self.zipcode

    def set_zip(self, zipcode):
        self.zipcode = zipcode

    def get_deadline(self):
        return self.deadline

    def get_weight(self):
        return self.weight

    def get_status(self):
        return self.status

    def set_status(self, new_status):
        self.status = new_status

    def get_message(self):
        return self.message
