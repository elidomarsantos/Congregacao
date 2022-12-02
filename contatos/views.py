from django.shortcuts import render
from django.contrib import messages
from urllib.request import Request
from django.http import HttpResponseNotAllowed
from django.shortcuts import redirect, render, get_object_or_404, redirect
from django.http import HttpResponse
from contatos.forms import Form_Contatos
from django.contrib.auth.decorators import login_required
from .models import Contatos
from openpyxl import load_workbook
import pandas as pd 

@login_required
def add_contatos(request):
        if request.method == 'POST':
            contatos = Form_Contatos(request.POST)
            
            if contatos.is_valid() :
                contatos.save()
                contatos = Form_Contatos()

                messages.info(request, 'Inserido com sucesso')
                return redirect('/contatos/view_contatos')
                

        else:
            contatos = Form_Contatos()
        
        return render(request, 'cp/add_contatos.html', {'contatos': contatos})   

@login_required
def view_contatos(request):
    nome = request.GET.get('nome')
    contatos =Contatos.objects.all()
    imprimir = Contatos.objects.filter().values_list()
    df = pd.DataFrame(imprimir)
    df.to_excel("static/Contatos.xlsx", header=False, index=False)
    
    if nome:
        contatos = Contatos.objects.filter(nome__icontains=nome)
     
    else:
        return render(request, 'cp/view_contatos.html', {'contatos': contatos})

    return render(request, 'cp/view_contatos.html', {'contatos': contatos})   

@login_required
def editar_contato(request, id):
    contato = get_object_or_404(Contatos, pk=id)
    form = Form_Contatos(instance=contato)
 
    if request.method == 'POST':
        form = Form_Contatos(request.POST, instance=contato)
         
        if form.is_valid():
            contato.save()
            messages.info(request, 'Editado com sucesso')
            return redirect('/contatos/view_contatos')
   
        else:
            return render(request, 'cp/edit_contatos.html', {'form':form ,'contato': contato})  


    return render(request, 'cp/edit_contatos.html', {'form':form ,'contato': contato})  

@login_required
def deletar_contato(request, id):
    del_contato = get_object_or_404(Contatos, pk=id)
   
    if request.method == 'POST':
        del_contato.delete()

        messages.info(request, 'Apagado com sucesso')
        return redirect('/contatos/view_contatos')

    return render(request, 'cp/deletar_contato.html')         


