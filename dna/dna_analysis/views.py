from django.shortcuts import render, get_object_or_404
from .models import dna_profile

# Create your views here.
def home(request):
    profiles = dna_profile.objects
    return render(request, 'profiles.html', {'profiles':profiles})

def detail(request, profile_id):
    profile = get_object_or_404(dna_profile, pk = profile_id)
    return render(request, 'detail.html', {'profile':profile})

def fasta(request):
    profiles = dna_profile.objects
    return render(request, 'fasta.html', {'profiles':profiles})