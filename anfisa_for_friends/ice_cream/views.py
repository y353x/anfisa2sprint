from django.shortcuts import get_object_or_404, get_list_or_404, render
from ice_cream.models import IceCream


def ice_cream_detail(request, pk):
    template = 'ice_cream/detail.html'
    ice_cream = get_object_or_404(
        IceCream.objects.values('title', 'description').filter(is_published=True), pk=pk
        )
    context = {'ice_cream': ice_cream}
    return render(request, template, context)


def ice_cream_list(request):
    template = 'ice_cream/list.html'
    ice_creams = get_list_or_404(
        IceCream.objects.values('id', 'title', 'description')
    )
    context = {'ice_cream_list': ice_creams}
    return render(request, template, context)
