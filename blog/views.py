from django.views.generic import TemplateView
from artikel.views import LatestArtikelPerKategori

class HomeView(TemplateView, LatestArtikelPerKategori):
    template_name = 'index.html'

    def get_context_data(self):
        queryset = self.latest_artikel_per_kategori()
        context = {
            'artikel_list': queryset
        }

        return context