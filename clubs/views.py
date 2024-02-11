from django.shortcuts import render
from common.models import ClubInfo

def clubs(request):
    info = ClubInfo.objects.filter().order_by('club_name')

    context={'clubs':info}
    return render(request, 'clubs/index2.html', context)



def club_list(request, aid):
    if aid == 1:
        info = ClubInfo.objects.filter(club_category="교양분과").order_by('club_name')
        context = {'clubs': info, 'category':"교양분과", 'description':"교양분과 어쩌고"}
    if aid == 2:
        info = ClubInfo.objects.filter(club_category="연대사업분과").order_by('club_name')
        context = {'clubs': info, 'category':"연대사업분과", 'description':"연대사업분과 어쩌고"}
    if aid == 3:
        info = ClubInfo.objects.filter(club_category="연행예술분과").order_by('club_name')
        context = {'clubs': info, 'category':"연행예술분과", 'description':"연행예술분과 어쩌고"}
    if aid == 4:
        info = ClubInfo.objects.filter(club_category="종교분과").order_by('club_name')
        context = {'clubs': info, 'category':"종교분과", 'description':"종교분과 어쩌고"}
    if aid == 5:
        info = ClubInfo.objects.filter(club_category="창작전시분과").order_by('club_name')
        context = {'clubs': info, 'category':"창작전시분과", 'description':"창작전시분과 어쩌고"}
    if aid == 6:
        info = ClubInfo.objects.filter(club_category="체육분과").order_by('club_name')
        context = {'clubs': info, 'category':"체육분과", 'description':"체육분과 어쩌고"}
    if aid == 7:
        info = ClubInfo.objects.filter(club_category="학술분과").order_by('club_name')
        context = {'clubs': info, 'category':"학술분과", 'description':"학술분과 어쩌고"}

    return render(request, 'clubs/index.html', context)


def club_description(request, bid):
    info = ClubInfo.objects.filter(id=bid)
    context = {'clubs': info,}
    return render(request, 'clubs/index3.html', context)