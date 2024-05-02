from . models import Category

def menu_links(request):
    lynks = Category.objects.all()
    return dict(links=lynks)
