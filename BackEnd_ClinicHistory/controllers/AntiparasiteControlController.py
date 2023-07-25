from repositories.AntiparasiteControlRepository import AntiparasiteControlRepository
from models.AntiparasiteControl import AntiparasiteControl


class AntiparasiteControlController():
    def __init__(self):
        self.AntiparasiteControlRepository = AntiparasiteControlRepository()

    def index(self):
        return self.AntiparasiteControlRepository.findAll()

    def create(self, infoAntiparasiteControl):
        newAntiparasiteControl = AntiparasiteControl(infoAntiparasiteControl)
        return self.AntiparasiteControlRepository.save(newAntiparasiteControl)

    def show(self, id):
        theAntiparasiteControl = AntiparasiteControl(self.AntiparasiteControlRepository.findById(id))
        return theAntiparasiteControl.__dict__

    # This method contains the class attributes.
    def update(self, id, infoAntiparasiteControl):
        currentAntiparasiteControl = AntiparasiteControl(self.AntiparasiteControlRepository.findById(id))
        currentAntiparasiteControl.date = infoAntiparasiteControl["Fecha"]
        currentAntiparasiteControl.product = infoAntiparasiteControl["Producto"]
        currentAntiparasiteControl.weight = infoAntiparasiteControl["Peso"]
        return self.AntiparasiteControlRepository.save(currentAntiparasiteControl)

    def delete(self, id):
        return self.AntiparasiteControlRepository.delete(id)