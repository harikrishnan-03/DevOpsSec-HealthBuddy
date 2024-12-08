from django.db import models
from django.contrib.auth.models import (
    AbstractBaseUser,
    PermissionsMixin,
    BaseUserManager,
)
from django.conf import settings


# medicine list
class CurrentMedicine(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    medicine_name = models.CharField(max_length=120)
    medicine_time = models.TimeField()

    # Vaccine list


class VaccineList(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    vaccine_name = models.CharField(max_length=120)
    vaccine_startdt = models.DateField()
    vaccine_enddt = models.DateField()

    # insurance_list


class HealthInsurance(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    insurance_policy_name = models.CharField(max_length=120)
    insurance_premium = models.IntegerField()
    insurance_startdt = models.DateField()
    insurance_enddt = models.DateField()

    # lab test list


class LabTestResults(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    lab_test_date = models.DateField()
    lab_sugar = models.IntegerField()
    lab_pressure = models.IntegerField()
    lab_Cholesterol = models.IntegerField()

    # general allergy list


class AllergicHistory(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    gen_allergy_name = models.CharField(max_length=120)
    gen_allergy_description = models.TextField()

    # medicine allergy list


class AllergicMedicine(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    med_allergy_name = models.CharField(max_length=120)
    med_allergy_description = models.TextField()


# Login
class UserManage(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError("Invalid email address")
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user


# Extra Fields
class AddUserData(AbstractBaseUser, PermissionsMixin):
    first_name = models.CharField(max_length=30, blank=True)
    last_name = models.CharField(max_length=30, blank=True)
    email = models.EmailField(unique=True)
    mobileNumber = models.IntegerField()
    dob = models.DateField()
    height = models.IntegerField()
    weight = models.IntegerField()
    bloodGroup = models.CharField(max_length=15, blank=True)
    gender = models.CharField(max_length=15, blank=True)

    objects = UserManage()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    def str(self):
        return self.email
