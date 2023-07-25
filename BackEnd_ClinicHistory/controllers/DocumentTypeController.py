from repositories.DocumentTypeRepository import DocumentTypeRepository
from models.DocumentType import DocumentType


class DocumentTypeController():
    def __init__(self):
        self.DocumentTypeRepository = DocumentTypeRepository()

    def index(self):
        return self.DocumentTypeRepository.findAll()

    def create(self, infoDocumentType):
        newDocumentType = DocumentType(infoDocumentType)
        return self.DocumentTypeRepository.save(newDocumentType)

    def show(self, id):
        theDocumentType = DocumentType(self.DocumentTypeRepository.findById(id))
        return theDocumentType.__dict__

    # This method contains the class attributes.
    def update(self, id, infoDocumentType):
        currentDocumentType = DocumentType(self.DocumentTypeRepository.findById(id))
        currentDocumentType.type = infoDocumentType["Tipo"]
        return self.DocumentTypeRepository.save(currentDocumentType)

    def delete(self, id):
        return self.DocumentTypeRepository.delete(id)