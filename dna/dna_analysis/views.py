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
                success = create(request.POST['title'], request.POST['dna'])
                if success != 1:
                    return render(request, 'upload.html', {'error':success})  
        elif request.POST['type'] == 'file':
            if request.POST['file']:
                fasta_to_model(request.POST['file'])

    return render(request, 'upload.html', {'profiles':profiles})

def create(title, dirty_dna):
    dna=""
    dna_lines = dirty_dna.splitlines()
    for line in dna_lines:
        dna += line.strip()
    for nucleobase in dna:
        if nucleobase != 'A' and nucleobase != 'C' and nucleobase != 'G' and nucleobase != 'T' and nucleobase != 'N':
            return "Error invalid character \"" + nucleobase + "\" found in string!"
    profile = dna_profile()
    profile.title = title
    profile.dna = dna
    profile.save()
    return 1

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
