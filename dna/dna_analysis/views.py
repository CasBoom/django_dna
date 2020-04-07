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

def upload(request):
    profiles = dna_profile.objects
    if request.method=='POST':
        if request.POST['type'] == 'raw':
            if request.POST['title'] and request.POST['dna']:
                create(request.POST['title'], request.POST['dna'])
        elif request.POST['type'] == 'file':
            if request.POST['file']:
                fasta_to_model(request.POST['file'])

    return render(request, 'upload.html', {'profiles':profiles})

def create(title, dna):
    # for nucleobase in dna:
    #     if nucleobase != 'A' and nucleobase != 'C' and nucleobase != 'G' and nucleobase != 'T' and nucleobase != 'N':
    #         return False
    profile = dna_profile()
    profile.title = title
    profile.dna = dna
    profile.save()
    return True

def fasta_to_model(file):
    title = ""
    dna = ""
    for line in file:
        if line[0] == '>':
            if title != "":
                create(title, dna)
                title = ""
                dna = ""

            title = line.rstrip()
        else:
            dna = dna + line.rstrip()
    create(title, dna)
