from django.shortcuts import redirect, render
from .models import Versao

def home(request):
    nome='sobre'
    return render(request, 'logicgirl/sobre.html', {'nome':nome})

def sugestao(request):
    nome='avaliacao'
    return render(request, 'logicgirl/sugestao.html', {'nome':nome})
    
def reverter(lista):
    saida=[]
    for i in lista:
        saida.insert(0,i)
    return saida

def downloads(request):
    nome='downloads'
    versoes = reverter(Versao.objects.all())
    return render(request, 'logicgirl/downloads.html', {'nome':nome,'versoes':versoes})

def equipe(request):
    nome='equipe'
    return render(request, 'logicgirl/equipe.html', {'nome':nome})

def sobre(request):
    return redirect('home')

def baixar(request,id):
    if Versao.objects.filter(pk=id):
        baixar = Versao.objects.get(pk=id)
        baixar.qtd_down+=1
        baixar.save()
        return redirect(baixar.arq)
    else:
        return redirect("downloads")