from django.db import models


from django.contrib.auth.models import Group, Permission

def create_groups():
    # Create a list of group names
    group_names = ['Receptionist', 'Manager', 'Nurse', 'Doctor', 'Cashier']

    for group_name in group_names:
        # Create the group
        group, created = Group.objects.get_or_create(name=group_name)
        if created:
            print(f"Group '{group_name}' created successfully.")
        else:
            print(f"Group '{group_name}' already exists.")

create_groups()




class Service(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.title


from django.contrib.auth.models import User

# No additional model is required as we'll use the built-in User model

class User(models.Model):
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    role = models.CharField(max_length=100)
    # Add other fields as needed


class Patient(models.Model):
    name = models.CharField(max_length=100)
    GENDER_CHOICES = (
            ('M', 'Homme'),
            ('F', 'Femme'),
        )
    gender = models.CharField(max_length=4, choices=GENDER_CHOICES, default="None", null=True)
    date_of_birth = models.DateField()
    address = models.CharField(max_length=30, default="Earth", null=True)
    # Add other fields as per the required information

    def __str__(self):
        return self.name

class Appointment(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    appointment_date = models.DateField()
    # Add other appointment fields as needed

    def __str__(self):
        return f"Appointment for {self.patient.name} on {self.appointment_date}"

class MedicalRecord(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    illness = models.CharField(max_length=100)
    date = models.DateField()
    symptom = models.TextField()
    # Add any additional fields as needed

class Prescription(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    drug = models.CharField(max_length=100)
    # Add any additional fields as needed

class Drug(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=8, decimal_places=2)

    def __str__(self):
        return self.name

class Bill(models.Model):
    patient = models.ForeignKey('dashboardguiv2.Patient', on_delete=models.CASCADE)
    drug = models.ForeignKey(Drug, on_delete=models.CASCADE)
    total_price = models.DecimalField(max_digits=8, decimal_places=2)

    def __str__(self):
        return f"Bill for {self.patient} - {self.drug}"

class Billings(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    exam_fee = models.DecimalField(max_digits=8, decimal_places=2)
    drug_fee = models.DecimalField(max_digits=8, decimal_places=2)
    total_fee = models.DecimalField(max_digits=8, decimal_places=2)
    paid = models.BooleanField(default=False)

    def __str__(self):
        return f"Bill for {self.patient}"

class Payment(models.Model):
    bill = models.ForeignKey(Bill, on_delete=models.CASCADE)
    amount_paid = models.DecimalField(max_digits=8, decimal_places=2)

    def __str__(self):
        return f"Payment for {self.bill}"

from django.db import models

class Regulation(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()

    def __str__(self):
        return self.title

from django.db import models

class MonthlyReport(models.Model):
    month = models.IntegerField()
    year = models.IntegerField()
    num_patients = models.IntegerField()
    drug_usage = models.TextField()
    revenue = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"Monthly Report - {self.month}/{self.year}"
