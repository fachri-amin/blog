from django.urls import path

from .views import (
    ArtikelList, 
    ArtikelDetail, 
    ArtikelKategori,
    ArtikelTambah,
    ArtikelManage,
    ArtikelDelete,
    ArtikelUpdate,
)
app_name = 'artikel'
urlpatterns = [
    path('update/<int:pk>', ArtikelUpdate.as_view(), name='artikelupdate'),
    path('delete/<int:pk>', ArtikelDelete.as_view(), name='artikeldelete'),
    path('manage/', ArtikelManage.as_view(), name='artikelmanage'),
    path('tambah/', ArtikelTambah.as_view(), name='artikeltambah'),
    path('', ArtikelList.as_view(), name='artikellist'),
    path('<int:page>', ArtikelList.as_view(), name='artikellist'),
    path('detail/<str:slug>', ArtikelDetail.as_view(), name='artikeldetail'),
    path('kategorilist/<str:kategori>', ArtikelKategori.as_view(), name='artikelkategori'),
    path('kategorilist/<str:kategori>/<int:page>', ArtikelKategori.as_view(), name='artikelkategori'),
]