from django.contrib import admin
from .models import (
    HomePageBanner,
    Appointment,
    ContactMessage,
    Doctor,
    Department,
)


@admin.register(HomePageBanner)
class HomePageBannerAdmin(admin.ModelAdmin):
    list_display = ("title",)


@admin.register(Appointment)
class AppointmentAdmin(admin.ModelAdmin):
    list_display = ("full_name", "phone_number", "date", "time", "service", "created_at")
    list_filter = ("service", "date")
    search_fields = ("full_name", "phone_number")


@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ("name", "email", "subject", "created_at")
    search_fields = ("name", "email", "subject")


@admin.register(Doctor)
class DoctorAdmin(admin.ModelAdmin):
    list_display = ("name", "specialty", "order")
    list_editable = ("order",)
    search_fields = ("name", "specialty")


@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    list_display = ("name", "order")
    list_editable = ("order",)
    search_fields = ("name",)