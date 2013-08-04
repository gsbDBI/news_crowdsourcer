class CResponse(object) :
    def __init__(self, submitted=None, response=None, worker_name=None) :
        self.submitted = submitted # date
        self.response = response # list of data generated by QType
        self.worker_name = worker_name
    @classmethod
    def from_dict(cls, d) :
        return CResponse(submitted=d['submitted'],
                         response=d['response'],
                         worker_name=d['worker_name'])
    def to_dict(self) :
        return {'submitted' : self.submitted,
                'response' : self.response,
                'worker_name' : self.worker_name}