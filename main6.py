# MediCare Connect - simple OOP appointment system
class Patient:
    def __init__(self, name, age):
        self.name = name
        self.age = age

class Doctor:
    def __init__(self, name, specialization):
        self.name = name
        self.specialization = specialization

class Appointment:
    def __init__(self, patient, doctor, date):
        self.patient = patient
        self.doctor = doctor
        self.date = date

    def show_details(self):
        print("\nAPPOINTMENT")
        print("Patient:", self.patient.name, "| Age:", self.patient.age)
        print("Doctor:", self.doctor.name, "| Specialization:", self.doctor.specialization)
        print("Date:", self.date)

patient = Patient(input("Patient name: "), int(input("Age: ")))
doctor = Doctor("Dr. Anu", "General Medicine")
appointment = Appointment(patient, doctor, input("Appointment date: "))
appointment.show_details()
