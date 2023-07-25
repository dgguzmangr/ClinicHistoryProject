from repositories.ReasonForConsultationRepository import ReasonForConsultationRepository
from models.ReasonForConsultation import ReasonForConsultation


class ReasonForConsultationController():
    def __init__(self):
        self.ReasonForConsultationRepository = ReasonForConsultationRepository()

    def index(self):
        return self.ReasonForConsultationRepository.findAll()

    def create(self, infoReasonForConsultation):
        newReasonForConsultation = ReasonForConsultation(infoReasonForConsultation)
        return self.ReasonForConsultationRepository.save(newReasonForConsultation)

    def show(self, id):
        theReasonForConsultation = ReasonForConsultation(self.ReasonForConsultationRepository.findById(id))
        return theReasonForConsultation.__dict__

    # This method contains the class attributes.
    def update(self, id, infoReasonForConsultation):
        currentReasonForConsultation = ReasonForConsultation(self.ReasonForConsultationRepository.findById(id))
        currentReasonForConsultation.diet = ReasonForConsultation["Dieta"]
        currentReasonForConsultation.previousIllnesses = ReasonForConsultation["Enfermedades previas"]
        currentReasonForConsultation.sterilized = ReasonForConsultation["Esterilizado"]
        currentReasonForConsultation.numberOfBirths = ReasonForConsultation["Número de partos"]
        currentReasonForConsultation.previousSurgeries = ReasonForConsultation["Cirugías previas"]
        currentReasonForConsultation.recentTreatments = ReasonForConsultation["Tratamientos recientes"]
        currentReasonForConsultation.recentTrips = ReasonForConsultation["Viajes recientes"]
        currentReasonForConsultation.doesThePetLiveWithOtherAnimals = ReasonForConsultation["¿Vive con otros animales?"]
        currentReasonForConsultation.reasonForConsultation = ReasonForConsultation["Motivo de la consulta"]
        return self.ReasonForConsultationRepository.save(currentReasonForConsultation)

    def delete(self, id):
        return self.ReasonForConsultationRepository.delete(id)