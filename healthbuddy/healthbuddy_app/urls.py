# pylint: skip-file
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path("", views.homePage, name="homePage"),
    path("dashboard", views.dashboard, name="dashboard"),
    path("login", views.logIn, name="logIn"),
    path("logout", views.logOut, name="logOut"),
    path("signup", views.signUp, name="signUp"),
    path("profile", views.profile, name="profile"),
    path(
        "updateprofileform/<int:id>", views.updateProfileForm, name="updateProfileForm"
    ),
    path("medicinelist", views.medicineList, name="medicineList"),
    path("addmedicine", views.addMedicine, name="addMedicine"),
    path("updatemedicine/<int:id>", views.updateMedicine, name="updateMedicine"),
    path(
        "updatemedicineform/<int:id>",
        views.updateMedicineForm,
        name="updateMedicineForm",
    ),
    path("deletemedicine/<int:id>", views.deleteMedicine, name="deleteMedicine"),
    path("vaccinelist", views.vaccineList, name="vaccineList"),
    path("addvaccine", views.addVaccine, name="addVaccine"),
    path("updatevaccine/<int:id>", views.updateVaccine, name="updateVaccine"),
    path(
        "updatevaccineform/<int:id>", views.updateVaccineForm, name="updateVaccineForm"
    ),
    path("deletevaccine/<int:id>", views.deleteVaccine, name="deleteVaccine"),
    path("insurancelist", views.insuranceList, name="insuranceList"),
    path("addinsurance", views.addInsurance, name="addInsurance"),
    path("updateinsurance/<int:id>", views.updateInsurance, name="updateInsurance"),
    path(
        "updateinsuranceform/<int:id>",
        views.updateInsuranceForm,
        name="updateInsuranceForm",
    ),
    path("deleteinsurance/<int:id>", views.deleteInsurance, name="deleteInsurance"),
    path("listlabresult", views.listLabResult, name="listLabResult"),
    path("addLabResult", views.addLabResult, name="addLabResult"),
    path("updatelabresult/<int:id>", views.updateLabResult, name="updateLabResult"),
    path(
        "updatelabresultform/<int:id>",
        views.updateLabResultForm,
        name="updateLabResultForm",
    ),
    path("deletelabresult/<int:id>", views.deleteLabResult, name="deleteLabResult"),
    path("listallergies", views.listAllergies, name="listAllergies"),
    path("addallergies", views.addAllergies, name="addAllergies"),
    path("updateallergies/<int:id>", views.updateAllergies, name="updateAllergies"),
    path(
        "updateallergiesform/<int:id>",
        views.updateAllergiesForm,
        name="updateAllergiesForm",
    ),
    path("deleteallergies/<int:id>", views.deleteAllergies, name="deleteAllergies"),
    path(
        "listallergicmedicine", views.listAllergicMedicine, name="listAllergicMedicine"
    ),
    path("addallergicmedicine", views.addAllergicMedicine, name="addAllergicMedicine"),
    path(
        "updateallergicmedicine/<int:id>",
        views.updateAllergicMedicine,
        name="updateAllergicMedicine",
    ),
    path(
        "updateallergicmedicineform/<int:id>",
        views.updateAllergicMedicineForm,
        name="updateAllergicMedicineForm",
    ),
    path(
        "deleteallergicmedicine/<int:id>",
        views.deleteAllergicMedicine,
        name="deleteAllergicMedicine",
    ),
]
