from repositories.VaccineRepository import VaccineRepository
from models.Vaccine import Vaccine


class VaccineController():
    def __init__(self):
        self.VaccineRepository = VaccineRepository()

    def index(self):
        return self.VaccineRepository.findAll()

    def create(self, infoVaccine):
        newVaccine = Vaccine(infoVaccine)
        return self.VaccineRepository.save(newVaccine)

    def show(self, id):
        theVaccine = Vaccine(self.VaccineRepository.findById(id))
        return theVaccine.__dict__

    # This method contains the class attributes.
    def update(self, id, infoVaccine):
        currentVaccine = Vaccine(self.VaccineRepository.findById(id))
        currentVaccine.comercialName = infoVaccine["Nombre comercial"]
        currentVaccine.genericName = infoVaccine["Nombre genérico"]
        currentVaccine.lotNumber = infoVaccine["Lote"]
        currentVaccine.dateOfElaboration = infoVaccine["Fecha de elaboración"]
        currentVaccine.dateOfExpiry = infoVaccine["Fecha de vencimiento"]
        return self.VaccineRepository.save(currentVaccine)

    def delete(self, id):
        return self.AntiparasiteControlRepository.delete(id)