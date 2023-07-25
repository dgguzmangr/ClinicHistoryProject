import json
import flask
from flask import jsonify
from flask_cors import CORS
from waitress import serve

from controllers.DocumentTypeController import DocumentTypeController
from controllers.OwnerDataController import OwnerDataController
from controllers.ClinicHistoryController import ClinicHistoryController
from controllers.PatientsDataController import PatientsDataController
from controllers.DosisController import DosisController
from controllers.AntiparasiteControlController import AntiparasiteControlController
from controllers.MedicalConsultationController import MedicalConsultationController
from controllers.HousingEnvironmentController import HousingEnvironmentController
from controllers.VaccineController import VaccineController
from controllers.DiseaseCourseController import DiseaseCourseController
from controllers.ReasonForConsultationController import ReasonForConsultationController

app = flask.Flask(__name__)
cors = CORS(app)
######################
##VARIABLES GLOBALES##
######################
myControllerDocumentType = DocumentTypeController()
myControllerOwnerData = OwnerDataController()
myControllerClinicHistory = ClinicHistoryController()
myControllerPatientsData = PatientsDataController()
myControllerDosis = DosisController()
myControllerAntiparasiteControl = AntiparasiteControlController()
myControllerMedicalConsultation = MedicalConsultationController()
myControllerHousingEnvironment = HousingEnvironmentController()
myControllerVaccine = VaccineController()
myControllerDiseaseCourse = DiseaseCourseController()
myControllerReasonForConsultation = ReasonForConsultationController()

###########################
##END POINT DOCUMENT TYPE##
###########################

@app.route("/documentType", methods=['GET'])
def getDocumentType():
    json = myControllerDocumentType.index()
    return jsonify(json)


@app.route("/documentType", methods=['POST'])
def createDocumentType():
    data = flask.request.get_json()
    json = myControllerDocumentType.create(data)
    return jsonify(json)

"""
@app.route("/documentType/<string:id>", methods=['GET'])
def getDocumentType(id):
    json = myControllerDocumentType.show(id)
    return jsonify(json)
"""


@app.route("/documentType/<string:id>", methods=['PUT'])
def modifyDocumentType(id):
    data = flask.request.get_json()
    json = myControllerDocumentType.update(id, data)
    return jsonify(json)


@app.route("/documentType/<string:id>", methods=['DELETE'])
def deleteDocumentType(id):
    json = myControllerDocumentType.delete(id)
    return jsonify(json)


########################
##END POINT OWNER DATA##
########################

@app.route("/ownerData", methods=['GET'])
def getOwnerData():
    json = myControllerOwnerData.index()
    return jsonify(json)


@app.route("/ownerData", methods=['POST'])
def createOwnerData():
    data = flask.request.get_json()
    json = myControllerOwnerData.create(data)
    return jsonify(json)

"""
@app.route("/ownerData/<string:id>", methods=['GET'])
def getOwnerData(id):
    json = myControllerOwnerData.show(id)
    return jsonify(json)
"""


@app.route("/ownerData/<string:id>", methods=['PUT'])
def modifyOwnerData(id):
    data = flask.request.get_json()
    json = myControllerOwnerData.update(id, data)
    return jsonify(json)


@app.route("/ownerData/<string:id>", methods=['DELETE'])
def deleteOwnerData(id):
    json = myControllerOwnerData.delete(id)
    return jsonify(json)

############################
##END POINT CLINIC HISTORY##
############################

@app.route("/clinicHistory", methods=['GET'])
def getClinicHistory():
    json = myControllerClinicHistory.index()
    return jsonify(json)


@app.route("/clinicHistory", methods=['POST'])
def createClinicHistory():
    data = flask.request.get_json()
    json = myControllerClinicHistory.create(data)
    return jsonify(json)


#@app.route("/clinicHistory/<string:id>", methods=['GET'])
#def getClinicHistory(id):
#    json = myClinicHistory.show(id)
#    return jsonify(json)



@app.route("/clinicHistory/<string:id>", methods=['PUT'])
def modifyClinicHistory(id):
    data = flask.request.get_json()
    json = myControllerClinicHistory.update(id, data)
    return jsonify(json)


@app.route("/clinicHistory/<string:id>", methods=['DELETE'])
def deleteClinicHistory(id):
    json = myControllerClinicHistory.delete(id)
    return jsonify(json)


###########################
##END POINT PATIENTS DATA##
###########################

@app.route("/patientsData", methods=['GET'])
def getPatientsData():
    json = myControllerPatientsData.index()
    return jsonify(json)


@app.route("/patientsData", methods=['POST'])
def createPatientsData():
    data = flask.request.get_json()
    json = myControllerPatientsData.create(data)
    return jsonify(json)

"""
@app.route("/patientsData/<string:id>", methods=['GET'])
def getPatientsData(id):
    json = myControllerPatientsData.show(id)
    return jsonify(json)
"""


@app.route("/patientsData/<string:id>", methods=['PUT'])
def modifyPatientsData(id):
    data = flask.request.get_json()
    json = myControllerPatientsData.update(id, data)
    return jsonify(json)


@app.route("/patientsData/<string:id>", methods=['DELETE'])
def deletePatientsData(id):
    json = myControllerPatientsData.delete(id)
    return jsonify(json)

###########################
##END POINT DOSIS##
###########################

@app.route("/dosis", methods=['GET'])
def getDosis():
    json = myControllerDosis.index()
    return jsonify(json)


@app.route("/dosis", methods=['POST'])
def createDosis():
    data = flask.request.get_json()
    json = myControllerDosis.create(data)
    return jsonify(json)

"""
@app.route("/dosis/<string:id>", methods=['GET'])
def getDosis(id):
    json = myControllerDosis.show(id)
    return jsonify(json)
"""


@app.route("/dosis/<string:id>", methods=['PUT'])
def modifyDosis(id):
    data = flask.request.get_json()
    json = myControllerDosis.update(id, data)
    return jsonify(json)


@app.route("/dosis/<string:id>", methods=['DELETE'])
def deleteDosis(id):
    json = myControllerDosis.delete(id)
    return jsonify(json)


##################################
##END POINT ANTIPARASITE CONTROL##
##################################

@app.route("/antiparasiteControl", methods=['GET'])
def getAntiparasiteControl():
    json = myControllerAntiparasiteControl.index()
    return jsonify(json)


@app.route("/antiparasiteControl", methods=['POST'])
def createAntiparasiteControl():
    data = flask.request.get_json()
    json = myControllerAntiparasiteControl.create(data)
    return jsonify(json)

"""
@app.route("/antiparasiteControl/<string:id>", methods=['GET'])
def getAntiparasiteControl(id):
    json = myControllerAntiparasiteControl.show(id)
    return jsonify(json)
"""


@app.route("/antiparasiteControl/<string:id>", methods=['PUT'])
def modifyAntiparasiteControl(id):
    data = flask.request.get_json()
    json = myControllerAntiparasiteControl.update(id, data)
    return jsonify(json)


@app.route("/antiparasiteControl/<string:id>", methods=['DELETE'])
def deleteAntiparasiteControl(id):
    json = myControllerAntiparasiteControl.delete(id)
    return jsonify(json)


##################################
##END POINT MEDICAL CONSULTATION##
##################################

@app.route("/medicalConsultation", methods=['GET'])
def getMedicalConsultation():
    json = myControllerMedicalConsultation.index()
    return jsonify(json)


@app.route("/medicalConsultation", methods=['POST'])
def createMedicalConsultation():
    data = flask.request.get_json()
    json = myControllerMedicalConsultation.create(data)
    return jsonify(json)

"""
@app.route("/medicalConsultation/<string:id>", methods=['GET'])
def getMedicalConsultation(id):
    json = myControllerMedicalConsultation.show(id)
    return jsonify(json)
"""


@app.route("/medicalConsultation/<string:id>", methods=['PUT'])
def modifyMedicalConsultation(id):
    data = flask.request.get_json()
    json = myControllerMedicalConsultation.update(id, data)
    return jsonify(json)


@app.route("/medicalConsultation/<string:id>", methods=['DELETE'])
def deleteMedicalConsultation(id):
    json = myControllerMedicalConsultation.delete(id)
    return jsonify(json)


#################################
##END POINT HOUSING ENVIRONMENT##
#################################

@app.route("/housingEnvironment", methods=['GET'])
def getHousingEnvironment():
    json = myControllerHousingEnvironment.index()
    return jsonify(json)


@app.route("/housingEnvironment", methods=['POST'])
def createHousingEnvironment():
    data = flask.request.get_json()
    json = myControllerHousingEnvironment.create(data)
    return jsonify(json)

"""
@app.route("/housingEnvironment/<string:id>", methods=['GET'])
def getHousingEnvironment(id):
    json = myControllerHousingEnvironment.show(id)
    return jsonify(json)
"""


@app.route("/housingEnvironment/<string:id>", methods=['PUT'])
def modifyHousingEnvironment(id):
    data = flask.request.get_json()
    json = myControllerHousingEnvironment.update(id, data)
    return jsonify(json)


@app.route("/housingEnvironment/<string:id>", methods=['DELETE'])
def deleteHousingEnvironment(id):
    json = myControllerHousingEnvironment.delete(id)
    return jsonify(json)


###########################
##END POINT VACCINE##
###########################

@app.route("/vaccine", methods=['GET'])
def getVaccine():
    json = myControllerVaccine.index()
    return jsonify(json)


@app.route("/vaccine", methods=['POST'])
def createVaccine():
    data = flask.request.get_json()
    json = myControllerVaccine.create(data)
    return jsonify(json)

"""
@app.route("/vaccine/<string:id>", methods=['GET'])
def getVaccine(id):
    json = myControllerVaccine.show(id)
    return jsonify(json)
"""


@app.route("/vaccine/<string:id>", methods=['PUT'])
def modifyVaccine(id):
    data = flask.request.get_json()
    json = myControllerVaccine.update(id, data)
    return jsonify(json)


@app.route("/vaccine/<string:id>", methods=['DELETE'])
def deleteVaccine(id):
    json = myControllerVaccine.delete(id)
    return jsonify(json)


############################
##END POINT DISEASE COURSE##
############################

@app.route("/diseaseCourse", methods=['GET'])
def getDiseaseCourse():
    json = myControllerDiseaseCourse.index()
    return jsonify(json)


@app.route("/diseaseCourse", methods=['POST'])
def createDiseaseCourse():
    data = flask.request.get_json()
    json = myControllerDiseaseCourse.create(data)
    return jsonify(json)

"""
@app.route("/diseaseCourse/<string:id>", methods=['GET'])
def getDiseaseCourse(id):
    json = myControllerDiseaseCourse.show(id)
    return jsonify(json)
"""


@app.route("/diseaseCourse/<string:id>", methods=['PUT'])
def modifyDiseaseCourse(id):
    data = flask.request.get_json()
    json = myControllerDiseaseCourse.update(id, data)
    return jsonify(json)


@app.route("/diseaseCourse/<string:id>", methods=['DELETE'])
def deleteDiseaseCourse(id):
    json = myControllerDiseaseCourse.delete(id)
    return jsonify(json)


#####################################
##END POINT REASON FOR CONSULTATION##
#####################################

@app.route("/reasonForConsultation", methods=['GET'])
def getReasonForConsultation():
    json = myControllerReasonForConsultation.index()
    return jsonify(json)


@app.route("/reasonForConsultation", methods=['POST'])
def createReasonForConsultation():
    data = flask.request.get_json()
    json = myControllerReasonForConsultation.create(data)
    return jsonify(json)

"""
@app.route("/reasonForConsultation/<string:id>", methods=['GET'])
def getReasonForConsultation(id):
    json = myControllerReasonForConsultation.show(id)
    return jsonify(json)
"""


@app.route("/reasonForConsultation/<string:id>", methods=['PUT'])
def modifyReasonForConsultation(id):
    data = flask.request.get_json()
    json = myControllerReasonForConsultation.update(id, data)
    return jsonify(json)


@app.route("/reasonForConsultation/<string:id>", methods=['DELETE'])
def deleteReasonForConsultation(id):
    json = myControllerReasonForConsultation.delete(id)
    return jsonify(json)


####################################
##    PROBAR EL SERVICIO          ##
####################################
def loadFileConfig():
    with open('config.json') as f:
        data = json.load(f)
    return data

if __name__=='__main__':
    dataConfig = loadFileConfig()
    print("Server running : "+"http://"+dataConfig["url-backend"]+":" + str(dataConfig["port"]))
    serve(app,host=dataConfig["url-backend"],port=dataConfig["port"])