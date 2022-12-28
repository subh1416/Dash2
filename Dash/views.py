from django.shortcuts import render


def main_view(request):
    return render(request, 'dash/Dashboard.html')

def home(request):
    return render(request, 'dash/home.html')

def satellite(request):
    return render(request, 'dash/satellite.html')

def packet(request):
    return render(request, 'dash/packet.html')

def station(request):
    return render(request, 'dash/station.html')
    

