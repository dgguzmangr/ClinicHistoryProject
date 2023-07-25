from repositories.OwnerDataRepository import OwnerDataRepository
from models.OwnerData import OwnerData


class OwnerDataController():
    def __init__(self):
        self.OwnerDataRepository = OwnerDataRepository()

    def index(self):
        return self.OwnerDataRepository.findAll()

    def create(self, infoOwnerData):
        newOwnerData = OwnerData(infoOwnerData)
        return self.OwnerDataRepository.save(newOwnerData)

    def show(self, id):
        theDocumentType = OwnerData(self.OwnerDataRepository.findById(id))
        return theDocumentType.__dict__

    # This method contains the class attributes.
    def update(self, id, infoOwnerData):
        currentOwnerData = OwnerData(self.OwnerDataRepository.findById(id))
        currentOwnerData.document = infoOwnerData["Documento"]
        currentOwnerData.firstName = infoOwnerData["Nombres"]
        currentOwnerData.lastName = infoOwnerData["Apellidos"]
        currentOwnerData.dateOfBirth = infoOwnerData["Fecha de Nacimiento"]
        currentOwnerData.adress = infoOwnerData["Dirección"]
        currentOwnerData.CellPhone = infoOwnerData["Celular"]
        currentOwnerData.eMail = infoOwnerData["Correo electrónico"]
        return self.OwnerDataRepository.save(currentOwnerData)

    def delete(self, id):
        return self.OwnerDataRepository.delete(id)