from django.shortcuts import render
from django.db.models import F,ExpressionWrapper,DecimalField
from django.http import HttpResponseRedirect
from django.views import View
from django.forms import ModelForm
from django.urls import reverse

from .models import Tesouro
# Create your views here.
class ListarTesouros(View):
    def get(self,request):
        lst_tesouros = Tesouro.objects.annotate(valor_total=ExpressionWrapper(F('quantidade')*F('preco'),\
                            output_field=DecimalField(max_digits=10,\
                                                    decimal_places=2,\
                                                     blank=True)\
                                                    )\
                            )
        valor_total = 0
        for tesouro in lst_tesouros:
            valor_total += tesouro.valor_total
        return render(request,"lista_tesouros.html",{"lista_tesouros":lst_tesouros,
                                                     "total_geral":valor_total})
class TesouroForm(ModelForm):
    class Meta:
        model = Tesouro
        fields = ['nome', 'quantidade', 'preco', 'img_tesouro']
        labels = {
            "img_tesouro": "Imagem"
        }

class SalvarTesouro(View):
    def get_tesouro(self,id):
        if id:
            return Tesouro.objects.get(id=id)
        return None

    def get(self,request,id=None):
        return render(request,"salvar_tesouro.html",{"tesouroForm":TesouroForm(instance=self.get_tesouro(id))})

    def post(self,request,id=None):
        form = TesouroForm(request.POST,request.FILES, instance=self.get_tesouro(id))

        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('lista_tesouros') )
        else:
            return render(request,"salvar_tesouro.html",{"tesouroForm":form})

class RemoverTesouro(View):
    def get(self,request,id):
        Tesouro.objects.get(id=id).delete()
        return HttpResponseRedirect(reverse('lista_tesouros') )
