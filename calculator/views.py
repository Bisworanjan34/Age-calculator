from django.shortcuts import render, redirect, get_object_or_404
from .models import Person
from .forms import PersonForm  # Form create kar lena model se
from datetime import date
from django.contrib.auth.decorators import login_required


@login_required(login_url="core:login")
def register(request):
    if request.method == "POST":
        form = PersonForm(request.POST)
        if form.is_valid():
            person = form.save()
            # Save hone ke baad seedha result page par redirect karein
            return redirect("calculator:result", pk=person.pk)
    else:
        form = PersonForm()
    return render(request, "calculator/register.html", {"form": form})


@login_required(login_url="core:login")
def result(request, pk):
    person = get_object_or_404(Person, pk=pk)
    dob = person.date_of_birth
    today = date.today()

    # Age Calculation Logic
    age = today.year - dob.year - ((today.month, today.day) < (dob.month, dob.day))

    return render(request, "calculator/calculator.html", {"person": person, "age": age})
