from repositories.HousingEnvironmentRepository import HousingEnvironmentRepository
from models.HousingEnvironment import HousingEnvironment

class HousingEnvironmentController():
    def __init__(self):
        self.HousingEnvironmentRepository = HousingEnvironmentRepository()

    def index(self):
        return self.HousingEnvironmentRepository.findAll()

    def create(self, infoHousingEnvironment):
        newHousingEnvironment = HousingEnvironment(infoHousingEnvironment)
        return self.HousingEnvironmentRepository.save(newHousingEnvironment)

    def show(self, id):
        theHousingEnvironment = HousingEnvironment(self.HousingEnvironmentRepository.findById(id))
        return theHousingEnvironment.__dict__

    # This method contains the class attributes.
    def update(self, id, infoHousingEnvironment):
        currentHousingEnvironment = HousingEnvironment(self.AntiparasiteControlRepository.findById(id))
        currentHousingEnvironment.startDate = HousingEnvironment["Fecha de inicio"]
        currentHousingEnvironment.endDate = HousingEnvironment["Fecha de finalización"]
        currentHousingEnvironment.period = HousingEnvironment["Periodo"]
        currentHousingEnvironment.location = HousingEnvironment["Locación"]
        currentHousingEnvironment.physicalCharacteristics = HousingEnvironment["Características físicas"]
        return self.HousingEnvironmentRepository.save(currentHousingEnvironment)

    def delete(self, id):
        return self.HousingEnvironmentRepository.delete(id)