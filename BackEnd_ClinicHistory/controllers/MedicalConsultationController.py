from repositories.MedicalConsultationRepository import MedicalConsultationRepository
from models.MedicalConsultation import MedicalConsultation


class MedicalConsultationController():
    def __init__(self):
        self.MedicalConsultationRepository = MedicalConsultationRepository()

    def index(self):
        return self.MedicalConsultationRepository.findAll()

    def create(self, infoMedicalConsultation):
        newMedicalConsultation = MedicalConsultation(infoMedicalConsultation)
        return self.MedicalConsultationRepository.save(newMedicalConsultation)

    def show(self, id):
        theMedicalConsultation = MedicalConsultation(self.MedicalConsultationRepository.findById(id))
        return theMedicalConsultation.__dict__

    # This method contains the class attributes.
    def update(self, id, infoMedicalConsultation):
        currentMedicalConsultation = MedicalConsultation(self.MedicalConsultationRepository.findById(id))
        currentMedicalConsultation.date = infoMedicalConsultation["Fecha"]
        currentMedicalConsultation.hour = infoMedicalConsultation["Hora"]
        return self.MedicalConsultationRepository.save(currentMedicalConsultation)

    def delete(self, id):
        return self.MedicalConsultationRepository.delete(id)