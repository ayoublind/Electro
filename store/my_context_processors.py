
from .models import Categorie


def include_categories(request):
    #perform your logic to create your list of groups
    categories = Categorie.objects.order_by('-designation')
    return {'categories':categories}