from category.models import Category


def navigation_links(request):
    links = Category.objects.all()
    return dict(links=links)
