from core.forms import ContactForm
from django.contrib import messages
from django.shortcuts import render, redirect


def home(request):
    if request.method == "POST":
        form = ContactForm(request.POST)

        if form.is_valid():
            form.save()
            messages.success(
                request,
                "Your message has been sent successfully!"
            )
            return redirect("/#contact")
    else:
        form = ContactForm()

    return render(request, "core/home.html", {
        "form": form
    })