from repositories.DiseaseCourseRepository import DiseaseCourseRepository
from models.DiseaseCourse import DiseaseCourse


class DiseaseCourseController():
    def __init__(self):
        self.DiseaseCourseRepository = DiseaseCourseRepository()

    def index(self):
        return self.DiseaseCourseRepository.findAll()

    def create(self, infoDiseaseCourse):
        newDiseaseCourse = DiseaseCourse(infoDiseaseCourse)
        return self.DiseaseCourseRepository.save(newDiseaseCourse)

    def show(self, id):
        theDiseaseCourse = DiseaseCourse(self.DiseaseCourseRepository.findById(id))
        return theDiseaseCourse.__dict__

    # This method contains the class attributes.
    def update(self, id, infoDiseaseCourse):
        currentDiseaseCourse = DiseaseCourse(self.DiseaseCourseRepository.findById(id))
        currentDiseaseCourse.fistSymptom = infoDiseaseCourse["Primeros síntomas"]
        currentDiseaseCourse.date = infoDiseaseCourse["Fecha"]
        currentDiseaseCourse.eventDescription = infoDiseaseCourse["Descripción del evento"]
        currentDiseaseCourse.didThePetHasFever = infoDiseaseCourse["¿Presentó fiebre?"]
        currentDiseaseCourse.receivedTreatment = infoDiseaseCourse["Tratamiento recibido"]
        currentDiseaseCourse.observations = infoDiseaseCourse["Observaciones"]
        return self.DiseaseCourseRepository.save(currentDiseaseCourse)

    def delete(self, id):
        return self.AntiparasiteControlRepository.delete(id)