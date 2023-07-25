from repositories.PatientsDataRepository import PatientsDataRepository
from models.PatientsData import PatientsData


class PatientsDataController():
    def __init__(self):
        self.PatientsDataRepository = PatientsDataRepository()

    def index(self):
        return self.PatientsDataRepository.findAll()

    def create(self, infoPatientsData):
        newPatientsData = PatientsData(infoPatientsData)
        return self.PatientsDataRepository.save(newPatientsData)

    def show(self, id):
        thePatientsData = PatientsData(self.PatientsDataRepository.findById(id))
        return thePatientsData.__dict__

    # This method contains the class attributes.
    def update(self, id, infoPatientsData):
        currentPatientsData = PatientsData(self.PatientsDataRepository.findById(id))
        currentPatientsData.name = infoPatientsData["Nombre"]
        currentPatientsData.species = infoPatientsData["Especie"]
        currentPatientsData.dateOfBirth = infoPatientsData["Fecha de Nacimiento"]
        currentPatientsData.raze = infoPatientsData["Raza"]
        currentPatientsData.color = infoPatientsData["Color"]
        currentPatientsData.coatType = infoPatientsData["Pelaje"]
        currentPatientsData.sex = infoPatientsData["Sexo"]
        currentPatientsData.microchipNumber = infoPatientsData["Número de microchip"]
        currentPatientsData.otherIdentifications = infoPatientsData["Otras identificaciones"]
        currentPatientsData.origin = infoPatientsData["Origen"]
        currentPatientsData.zoothecnicalPurpose = infoPatientsData["Fin zootécnico"]
        return self.PatientsDataRepository.save(currentPatientsData)

    def delete(self, id):
        return self.PatientsDataRepository.delete(id)