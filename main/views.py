from django.shortcuts import render

def home(requests):

    return render(requests,'index.html')


def birja(requests):

    return render(requests,'birja.html')



def profil(requests):

    return render(requests,'profil.html')