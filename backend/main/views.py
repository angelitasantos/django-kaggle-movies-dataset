from django.shortcuts import render
import sys
sys.path.append("..")
from data.import_data import Movies
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


def home(request):
    movies = Movies.importDataMovies()
    page_num = request.GET.get('page', 1)
    paginator = Paginator(movies, 1984)
    
    try:
        page_obj = paginator.page(page_num)
    except PageNotAnInteger:
        page_obj = paginator.page(1)
    except EmptyPage:
        page_obj = paginator.page(paginator.num_pages)

    return render(request, 'index.html', {'page_obj': page_obj})