from django.db import models


class HomePageBanner(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to="banners/")

    def __str__(self):
        return self.title


class Appointment(models.Model):

    SERVICE_CHOICES = [
        ("General Medicine", "General Medicine"),
        ("Emergency Care", "Emergency Care"),
        ("Pharmacy", "Pharmacy"),
        ("Laboratory", "Laboratory"),
        ("Family Care", "Family Care"),
        ("Specialist Care", "Specialist Care"),
    ]

    full_name = models.CharField(max_length=150)
    phone_number = models.CharField(max_length=20)
    date = models.DateField()
    time = models.TimeField()
    service = models.CharField(max_length=50, choices=SERVICE_CHOICES, blank=True)
    message = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return f"{self.full_name} - {self.date} {self.time}"


class ContactMessage(models.Model):
    name = models.CharField(max_length=150)
    email = models.EmailField()
    subject = models.CharField(max_length=200, blank=True)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return f"{self.name} - {self.subject or 'No subject'}"


class Doctor(models.Model):
    name = models.CharField(max_length=150)
    specialty = models.CharField(max_length=150)
    photo = models.ImageField(upload_to="doctors/")
    order = models.PositiveIntegerField(default=0, help_text="Lower numbers appear first")

    class Meta:
        ordering = ["order", "name"]

    def __str__(self):
        return self.name


class Department(models.Model):
    name = models.CharField(max_length=150)
    description = models.TextField()
    image = models.ImageField(upload_to="departments/")
    order = models.PositiveIntegerField(default=0, help_text="Lower numbers appear first")

    class Meta:
        ordering = ["order", "name"]

    def _str_(self):
        return self.name