from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Appointment, ContactMessage, Doctor, Department


def index(request):

    if request.method == "POST" and request.POST.get("form_type") == "appointment":

        full_name = request.POST.get("full_name")
        phone_number = request.POST.get("phone_number")
        date = request.POST.get("date")
        time = request.POST.get("time")
        service = request.POST.get("service")
        message = request.POST.get("message")

        if full_name and phone_number and date and time:

            Appointment.objects.create(
                full_name=full_name,
                phone_number=phone_number,
                date=date,
                time=time,
                service=service,
                message=message,
            )

            messages.success(
                request,
                "Your appointment request has been received. We'll be in touch shortly."
            )

            return redirect("/#appointment")

        else:
            messages.error(request, "Please fill in all required fields.")

    elif request.method == "POST" and request.POST.get("form_type") == "contact":

        name = request.POST.get("name")
        email = request.POST.get("email")
        subject = request.POST.get("subject")
        message = request.POST.get("message")

        if name and email and message:

            ContactMessage.objects.create(
                name=name,
                email=email,
                subject=subject,
                message=message,
            )

            messages.success(
                request,
                "Your message has been sent. We'll get back to you soon."
            )

            return redirect("/#contact")

        else:
            messages.error(request, "Please fill in all required fields.")

    context = {
        "doctors": Doctor.objects.all(),
        "departments": Department.objects.all(),
    }

    return render(request, "index.html", context)