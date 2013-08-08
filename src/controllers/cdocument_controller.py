class CDocumentController(object):
    def __init__(self, db):
        self.db = db
        self.db.cdocs.ensure_index('name', unique=True)
    def create(self, name, d):
        self.db.cdocs.insert({'name' : name, 'content' : d})
    def get_document_by_name(self, name):
        d = self.db.cdocs.find_one({'name' : name})
        return d['content']
