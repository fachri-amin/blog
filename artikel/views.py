from django.views.generic import (
    ListView, 
    DetailView, 
    CreateView,
    UpdateView,
    DeleteView,
)
from django.urls import reverse_lazy

# Create your views here.
from  .models import ArtikelModel
from .forms import ArtikelForm

class ArtikelUpdate(UpdateView):
    model = ArtikelModel
    template_name = 'artikel/artikel_update.html'
    form_class = ArtikelForm

class ArtikelDelete(DeleteView):
    model = ArtikelModel
    template_name = 'artikel/artikel_delete_confirm.html'
    success_url = reverse_lazy('artikel:artikelmanage')

class ArtikelManage(ListView):
    model = ArtikelModel
    template_name = 'artikel/artikel_manage.html'
    context_object_name = 'artikel_list'
    ordering = ['-id']

class ArtikelTambah(CreateView):
    template_name = 'artikel/artikel_tambah.html'
    form_class = ArtikelForm

class LatestArtikelPerKategori():
    model = ArtikelModel

    def latest_artikel_per_kategori(self):
        kategori_list = self.model.objects.values_list('kategori', flat=True).distinct() # mengambil nilai dari fields kategori. distinct untuk tetap menghitung satu nilai kategori yang sama
        queryset = [] #untuk menampung setiap artikel terakhir pada masing masing kategori
        for i in kategori_list:             
            artikel = self.model.objects.filter(kategori=i).latest('id')
            queryset.append(artikel) #karena query set adalah list maka datanya bisa ditambahkan dengan append
        return queryset


class ArtikelKategori(ListView):
    model = ArtikelModel
    template_name = 'artikel/artikel_kategori.html'
    context_object_name = 'artikel_list'
    paginate_by = 3
    ordering =['-id']
    def get_queryset(self):
        self.queryset = self.model.objects.filter(kategori=self.kwargs['kategori'])
        return super().get_queryset()

    def get_context_data(self, *args, **kwargs):
        kategori_list = self.model.objects.values_list('kategori', flat=True).distinct().exclude(kategori=self.kwargs['kategori'])
        self.kwargs.update({'kategori_list':kategori_list})
        kwargs = self.kwargs
        return super().get_context_data(*args, **kwargs)

class ArtikelList(ListView):
    model = ArtikelModel
    template_name = 'artikel/artikel_list.html'
    context_object_name = 'artikel_list'
    paginate_by = 3
    ordering = ['-id']

    def get_context_data(self, *args, **kwargs):
        kategori_list = self.model.objects.values_list('kategori', flat=True).distinct()
        self.kwargs.update({'kategori_list':kategori_list})
        kwargs = self.kwargs
        return super().get_context_data(*args, **kwargs)

class ArtikelDetail(DetailView):
    template_name = 'artikel/artikel_detail.html'
    model = ArtikelModel

    def get_context_data(self, *args, **kwargs):
        kategori_list = self.model.objects.values_list('kategori', flat=True).distinct()
        artikel_serupa = self.model.objects.filter(kategori= self.object.kategori).exclude(id=self.object.id)
        self.kwargs.update({
            'kategori_list':kategori_list,
            'artikel_serupa': artikel_serupa,
        })
        kwargs = self.kwargs
        return super().get_context_data(*args, **kwargs)