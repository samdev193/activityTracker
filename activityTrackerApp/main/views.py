from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render
from .forms import RegisterForm
from .models import UserProfile
import pandas as pd
from matplotlib import pyplot as plt

# Create your views here.


def home(request):
    return render(request, "main/home.html")

def register(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/login/")
    else:
        form = RegisterForm()

    return render(request, "main/register.html", {"form": form})

def questionnaire(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        user = request.user.id
        if request.user.userprofile.filter(user_id=user):
            UserProfile.objects.filter(user_id=user).delete()

        profile = UserProfile(
            exercise= int(form.data["Exercise"]),
            work= int(form.data["Work"]),
            relax= int(form.data["Relax"]),
            study= int(form.data["Study"]),
            self_care= int(form.data["Self Care"])
        )

        profile.save()
        request.user.userprofile.add(profile)
        df = pd.DataFrame(
            {"activities": {"work": profile.work, "exercise": profile.exercise,
                            "relax": profile.relax, "study": profile.study, "self care":profile.self_care}}
        )

        fig, ax = plt.subplots()
        plt.bar(range(len(df)), df["activities"], color=['C0', 'C1', 'C2','C3','C4'])
        fig.savefig('staticfiles/images/graph.png')

        return redirect("/profile/")

    return render(request, "main/questionnaire.html")


def profile(request):

    user = request.user.id
    user_profile = UserProfile.objects.get(user_id=user)

    return render(request, "main/profile.html", {"user_profile":user_profile})
