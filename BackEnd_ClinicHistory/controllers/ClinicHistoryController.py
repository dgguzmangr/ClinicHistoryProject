from repositories.ClinicHistoryRepository import ClinicHistoryRepository
from models.ClinicHistory import ClinicHistory


class ClinicHistoryController():
    def __init__(self):
        self.ClinicHistoryRepository = ClinicHistoryRepository()

    def index(self):
        return self.ClinicHistoryRepository.findAll()

    def create(self, infoClinicHistory):
        newClinicHistory = ClinicHistory(infoClinicHistory)
        return self.ClinicHistoryRepository.save(newClinicHistory)

    def show(self, id):
        theClinicHistory = ClinicHistory(self.ClinicHistoryRepository.findById(id))
        return theClinicHistory.__dict__

    # This method contains the class attributes.
    def update(self, id, infoClinicHistory):
        currentClinicHistory = ClinicHistory(self.ClinicHistoryRepository.findById(id))
        currentClinicHistory.number = infoClinicHistory["Número"]
        currentClinicHistory.date = infoClinicHistory["Fecha"]
        currentClinicHistory.hour = infoClinicHistory["Hora"]
        return self.ClinicHistoryRepository.save(currentClinicHistory)

    def delete(self, id):
        return self.ClinicHistoryRepository.delete(id)