# pylint: skip-file
from django.shortcuts import render, redirect
from .forms import CustomUserForm, AuthenticateLogin
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from .models import *


def homePage(request):
    return render(request, "HomePage.html")


def signUp(request):
    if request.method == "POST":
        form = CustomUserForm(request.POST)
        print(form.errors)
        if form.is_valid():
            print("validate?")
            form.save()
            return redirect("logIn")
    else:
        form = CustomUserForm()
    return render(request, "SignUp.html", {"form": form})


def logIn(request):
    if request.method == "POST":
        form = AuthenticateLogin(request, request.POST)
        if form.is_valid():
            email = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
            user = authenticate(request, email=email, password=password)
            if user is not None:
                login(request, user)
                print("login ayi")
                return redirect("dashboard")
    else:
        form = AuthenticateLogin()
    return render(request, "Login.html", {"form": form})


@login_required(login_url="logIn")
def logOut(request):
    logout(request)
    return redirect("homePage")


@login_required(login_url="logIn")
def dashboard(request):
    user = request.user
    print(user)
    return render(request, "Dashboard.html", {"user": user})


@login_required(login_url="logIn")
def profile(request):
    currentUser = request.user
    filterUser = AddUserData.objects.filter(email=currentUser)
    filterUserDob = currentUser.dob
    filterUserGender = currentUser.gender
    return render(
        request,
        "Profile.html",
        {"filterUser": filterUser, "dob": filterUserDob, "gender": filterUserGender},
    )


@login_required(login_url="logIn")
def updateProfileForm(request, id):
    if request.method == "POST":
        profileToUpdate = AddUserData.objects.get(id=id)
        profileToUpdate.first_name = request.POST["firstName"]
        profileToUpdate.last_name = request.POST["lName"]
        profileToUpdate.mobileNumber = request.POST["mobNo"]
        profileToUpdate.dob = request.POST["dob"]
        profileToUpdate.height = request.POST["height"]
        profileToUpdate.weight = request.POST["weight"]
        profileToUpdate.save()
    return redirect("dashboard")


@login_required(login_url="logIn")
def medicineList(request):
    currentUser = request.user
    medicineList = CurrentMedicine.objects.filter(user=currentUser)
    print(medicineList)
    print(currentUser)
    return render(request, "MedicineHistory.html", {"medicineList": medicineList})


@login_required(login_url="logIn")
def addMedicine(request):
    if request.method == "POST":
        currentUser = request.user
        medicineName = request.POST["medicineName"]
        medicineTime = request.POST["medicineTime"]
        saveMedicine = CurrentMedicine(
            user=currentUser, medicine_name=medicineName, medicine_time=medicineTime
        )
        saveMedicine.save()
    return redirect("medicineList")


@login_required(login_url="logIn")
def updateMedicine(request, id):
    medicineToUpdate = CurrentMedicine.objects.get(id=id)
    medicine_time = medicineToUpdate.medicine_time
    return render(
        request,
        "UpdateMedicine.html",
        {"id": medicineToUpdate, "medicine_time": medicine_time},
    )


@login_required(login_url="logIn")
def updateMedicineForm(request, id):
    if request.method == "POST":
        medicineToUpdate = CurrentMedicine.objects.get(id=id)
        medicineToUpdate.user = request.user  # Assign User to  CurrentMedicine Object
        medicineToUpdate.medicine_name = request.POST["medicineName"]
        medicineToUpdate.medicine_time = request.POST["medicineTime"]
        medicineToUpdate.save()
    return redirect("medicineList")


@login_required(login_url="logIn")
def deleteMedicine(request, id):
    medicineToDelete = CurrentMedicine.objects.get(id=id)
    medicineToDelete.delete()
    return redirect("medicineList")


@login_required(login_url="logIn")
def vaccineList(request):
    currentUser = request.user
    vaccineList = VaccineList.objects.filter(user=currentUser)
    print(vaccineList)
    print(currentUser)
    return render(request, "Vaccines.html", {"vaccineList": vaccineList})


@login_required(login_url="logIn")
def addVaccine(request):
    if request.method == "POST":
        currentUser = request.user
        vaccineName = request.POST["vaccineName"]
        vaccineStart = request.POST["vaccineStart"]
        vaccineEnd = request.POST["vaccineEnd"]
        saveVaccine = VaccineList(
            user=currentUser,
            vaccine_name=vaccineName,
            vaccine_startdt=vaccineStart,
            vaccine_enddt=vaccineEnd,
        )
        saveVaccine.save()
    return redirect("vaccineList")


@login_required(login_url="logIn")
def updateVaccine(request, id):
    vaccineToUpdate = VaccineList.objects.get(id=id)
    vaccine_startdt = vaccineToUpdate.vaccine_startdt
    vaccine_enddt = vaccineToUpdate.vaccine_enddt
    return render(
        request,
        "UpdateVaccines.html",
        {
            "id": vaccineToUpdate,
            "vaccine_startdt": vaccine_startdt,
            "vaccine_enddt": vaccine_enddt,
        },
    )


@login_required(login_url="logIn")
def updateVaccineForm(request, id):
    if request.method == "POST":
        vaccineToUpdate = VaccineList.objects.get(id=id)
        vaccineToUpdate.user = request.user
        vaccineToUpdate.vaccine_name = request.POST["vaccineName"]
        vaccineToUpdate.vaccine_startdt = request.POST["vaccineStart"]
        vaccineToUpdate.vaccine_enddt = request.POST["vaccineEnd"]
        vaccineToUpdate.save()
    return redirect("vaccineList")


@login_required(login_url="logIn")
def deleteVaccine(request, id):
    vaccineToDelete = VaccineList.objects.get(id=id)
    vaccineToDelete.delete()
    return redirect("vaccineList")


@login_required(login_url="logIn")
def insuranceList(request):
    currentUser = request.user
    insuranceDetails = HealthInsurance.objects.filter(user=currentUser)
    print(insuranceDetails)
    print(currentUser)
    return render(
        request, "Insurance.html", {"insuranceDetails": insuranceDetails}
    )  # Stored as key value pairs


@login_required(login_url="logIn")
def addInsurance(request):
    if request.method == "POST":
        currentUser = request.user
        policyName = request.POST["policyName"]
        premium = request.POST["premium"]
        startDate = request.POST["startDate"]
        endDate = request.POST["endDate"]
        saveInsurance = HealthInsurance(
            user=currentUser,
            insurance_policy_name=policyName,
            insurance_premium=premium,
            insurance_startdt=startDate,
            insurance_enddt=endDate,
        )
        saveInsurance.save()
    return redirect("insuranceList")


@login_required(login_url="logIn")
def updateInsurance(request, id):
    insuranceToUpdate = HealthInsurance.objects.get(id=id)
    insurance_startdt = insuranceToUpdate.insurance_startdt
    insurance_enddt = insuranceToUpdate.insurance_enddt
    return render(
        request,
        "UpdateInsurance.html",
        {
            "id": insuranceToUpdate,
            "insurance_startdt": insurance_startdt,
            "insurance_enddt": insurance_enddt,
        },
    )


@login_required(login_url="logIn")
def updateInsuranceForm(request, id):
    if request.method == "POST":
        insuranceToUpdate = HealthInsurance.objects.get(id=id)
        insuranceToUpdate.user = request.user
        insuranceToUpdate.insurance_policy_name = request.POST["policyName"]
        insuranceToUpdate.insurance_premium = request.POST["premium"]
        insuranceToUpdate.insurance_startdt = request.POST["startDate"]
        insuranceToUpdate.insurance_enddt = request.POST["endDate"]
        insuranceToUpdate.save()
    return redirect("insuranceList")


@login_required(login_url="logIn")
def deleteInsurance(request, id):
    insuranceToDelete = HealthInsurance.objects.get(id=id)
    insuranceToDelete.delete()
    return redirect("insuranceList")


@login_required(login_url="logIn")
def listLabResult(request):
    currentUser = request.user
    labDetails = LabTestResults.objects.filter(user=currentUser)
    print(labDetails)
    print(currentUser)
    return render(
        request, "LabResult.html", {"labDetails": labDetails}
    )  # Stored as key value pairs


@login_required(login_url="logIn")
def addLabResult(request):
    if request.method == "POST":
        currentUser = request.user
        testDate = request.POST["testDate"]
        sugar = request.POST["sugar"]
        pressure = request.POST["pressure"]
        cholesterol = request.POST["cholesterol"]
        saveLabResult = LabTestResults(
            user=currentUser,
            lab_test_date=testDate,
            lab_sugar=sugar,
            lab_pressure=pressure,
            lab_Cholesterol=cholesterol,
        )
        saveLabResult.save()
    return redirect("listLabResult")


@login_required(login_url="logIn")
def updateLabResult(request, id):
    labResultToUpdate = LabTestResults.objects.get(id=id)
    lab_test_date = labResultToUpdate.lab_test_date
    return render(
        request,
        "UpdateLabResult.html",
        {"id": labResultToUpdate, "lab_test_date": lab_test_date},
    )


@login_required(login_url="logIn")
def updateLabResultForm(request, id):
    if request.method == "POST":
        labResultToUpdate = LabTestResults.objects.get(id=id)
        labResultToUpdate.user = request.user
        labResultToUpdate.lab_test_date = request.POST["testDate"]
        labResultToUpdate.lab_pressure = request.POST["pressure"]
        labResultToUpdate.lab_sugar = request.POST["sugar"]
        labResultToUpdate.lab_Cholesterol = request.POST["cholesterol"]
        labResultToUpdate.save()
    return redirect("listLabResult")


@login_required(login_url="logIn")
def deleteLabResult(request, id):
    labResultToDelete = LabTestResults.objects.get(id=id)
    labResultToDelete.delete()
    return redirect("listLabResult")


@login_required(login_url="logIn")
def listAllergies(request):
    currentUser = request.user
    allergyDetails = AllergicHistory.objects.filter(user=currentUser)
    print(allergyDetails)
    print(currentUser)
    return render(
        request, "Allergies.html", {"allergyDetails": allergyDetails}
    )  # Stored as key value pairs


@login_required(login_url="logIn")
def addAllergies(request):
    if request.method == "POST":
        currentUser = request.user
        allergyName = request.POST["allergyName"]
        allergyDescription = request.POST["allergyDescription"]
        saveAllergy = AllergicHistory(
            user=currentUser,
            gen_allergy_name=allergyName,
            gen_allergy_description=allergyDescription,
        )
        saveAllergy.save()
    return redirect("listAllergies")


@login_required(login_url="logIn")
def updateAllergies(request, id):
    allergyToUpdate = AllergicHistory.objects.get(id=id)
    return render(request, "UpdateAllergies.html", {"id": allergyToUpdate})


@login_required(login_url="logIn")
def updateAllergiesForm(request, id):
    if request.method == "POST":
        allergyToUpdate = AllergicHistory.objects.get(id=id)
        allergyToUpdate.user = request.user
        allergyToUpdate.gen_allergy_name = request.POST["allergyName"]
        allergyToUpdate.gen_allergy_description = request.POST["allergyDescription"]
        allergyToUpdate.save()
    return redirect("listAllergies")


@login_required(login_url="logIn")
def deleteAllergies(request, id):
    allergicMedicineToUpdate = AllergicHistory.objects.get(id=id)
    allergicMedicineToUpdate.delete()
    return redirect("listAllergies")


@login_required(login_url="logIn")
def listAllergicMedicine(request):
    currentUser = request.user
    allergyMedicineDetails = AllergicMedicine.objects.filter(user=currentUser)
    print(allergyMedicineDetails)
    print(currentUser)
    return render(
        request,
        "AllergicMedicine.html",
        {"allergyMedicineDetails": allergyMedicineDetails},
    )  # Stored as key value pairs


@login_required(login_url="logIn")
def addAllergicMedicine(request):
    if request.method == "POST":
        currentUser = request.user
        medAllergyName = request.POST["medAllergyName"]
        medAllergyDescription = request.POST["medAllergyDescription"]
        saveAllergicMedicine = AllergicMedicine(
            user=currentUser,
            med_allergy_name=medAllergyName,
            med_allergy_description=medAllergyDescription,
        )
        saveAllergicMedicine.save()
    return redirect("listAllergicMedicine")


@login_required(login_url="logIn")
def updateAllergicMedicine(request, id):
    allergicMedicineToUpdate = AllergicMedicine.objects.get(id=id)
    return render(
        request, "UpdateAllergicMedicine.html", {"id": allergicMedicineToUpdate}
    )


@login_required(login_url="logIn")
def updateAllergicMedicineForm(request, id):
    if request.method == "POST":
        allergicMedicineToUpdate = AllergicMedicine.objects.get(id=id)
        allergicMedicineToUpdate.user = request.user
        allergicMedicineToUpdate.med_allergy_name = request.POST["medAllergyName"]
        allergicMedicineToUpdate.med_allergy_description = request.POST[
            "medAllergyDescription"
        ]
        allergicMedicineToUpdate.save()
    return redirect("listAllergicMedicine")


@login_required(login_url="logIn")
def deleteAllergicMedicine(request, id):
    allergicMedicineToUpdate = AllergicMedicine.objects.get(id=id)
    allergicMedicineToUpdate.delete()
    return redirect("listAllergicMedicine")
