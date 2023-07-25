from repositories.DosisRepository import DosisRepository
from models.Dosis import Dosis


class DosisController():
    def __init__(self):
        self.DosisRepository = DosisRepository()

    def index(self):
        return self.DosisRepository.findAll()

    def create(self, infoDosis):
        newDosis = Dosis(infoDosis)
        return self.DosisRepository.save(newDosis)

    def show(self, id):
        theDosis = Dosis(self.DosisRepository.findById(id))
        return theDosis.__dict__

    # This method contains the class attributes.
    def update(self, id, infoDosis):
        currentDosis = Dosis(self.DosisRepository.findById(id))
        currentDosis.scheduledDate = infoDosis["Fecha programada"]
        currentDosis.applicationDate = infoDosis["Fecha de aplicación"]
        currentDosis.weight = infoDosis["Peso"]
        currentDosis.veterinarian = infoDosis["Veterinario"]
        return self.DosisRepository.save(currentDosis)

    def delete(self, id):
        return self.DosisRepository.delete(id)