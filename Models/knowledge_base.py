class KnowledgeBase:
    def __init__(self, documents):
        self.documents = documents

    def search_documents(self, query):
        return [doc for doc in self.documents if query in doc.title]
