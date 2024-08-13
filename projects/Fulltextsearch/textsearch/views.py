from django.shortcuts import render
from django.db.models import Q
from .models import Product
from django.views.decorators.cache import cache_page
from django.core.cache import cache
from django.contrib.postgres.search import (
    SearchVector,
    SearchQuery,
    SearchRank,
    TrigramSimilarity,
)

@cache_page(60 * 1)
def index(request):
    search = request.GET.get("search")
    if search:
        # query = SearchQuery(search)
        # vector = SearchVector("title", weight="A")
        # vector = (
        #     SearchVector("category", weight="B")
        #     + SearchVector("brand", weight="C")
        #     + SearchVector("sku", weight="D")
        # )
        # rank = SearchRank(vector, query)

        # products = Product.objects.filter(
        #     title__search=search
        # )  # we can apply search for every field --step1

        # products = Product.objects.annotate(
        #     search=SearchVector("title", "category", "description")
        # ).filter(search=search)

        # products = Product.objects.annotate(
        #     search=SearchVector("title")
        #     + SearchVector("category")
        #     + SearchVector("description")
        # ).filter(search=search)

        # products = Product.objects.annotate(
        #     search=SearchVector("title")
        #     + SearchVector("category")
        #     + SearchVector("description")
        # ).filter(search=query)

        # search product by rank
        # query = SearchQuery(search)
        # vector = SearchVector("title", "category", "brand", "sku")
        # rank = SearchRank(vector,query)
        # products = (
        #     Product.objects.annotate(rank=rank).filter(rank__gte=0.05).order_by("-rank")
        # )

        # Search product by weight then rank
        
        # query = SearchQuery(search)
        # # vector = SearchVector("title", "category", "brand", "sku")
        # vector = (SearchVector("title", weight = "A")+
        #           SearchVector("category",weight = "B")+
        #           SearchVector( "brand",weight = "C")+
        #           SearchVector("sku", weight = "D"))
        # rank = SearchRank(vector, query)
        # products = (
        #     Product.objects.annotate(rank=rank).order_by("-rank")
        # )

        # Trigramsimilarity search
        query = SearchQuery(search)
        vector = SearchVector("title", "category", "description", "brand")
        rank = SearchRank(vector, query)
        products = (
            Product.objects.annotate(
                rank=rank,
                similarity = TrigramSimilarity("title", search)
                + TrigramSimilarity("category", search)
                + TrigramSimilarity("description", search)
                + TrigramSimilarity("brand", search)
            )
            .filter(Q(rank__gte=0.1) | Q(similarity__gte=0.1))
            .distinct()
            .order_by("-rank", "-similarity")
        )

    else:
        products = Product.objects.all()
    
    # if (min_price := float(request.GET.get('min_price'))) and (max_price := float(request.GET.get('max_price'))):
    #     products = products.filter(price__gte=min_price, price__lte=max_price).order_by('price') 
        
    # if brand:=request.GET.get('brand'):
    #    products = products.filter(brand=brand).order_by('price')
    # if category:=request.GET.get('category'):
    #    products = products.filter(category=category).order_by('price') 
    if request.GET.get('brand'):
        products = products.filter(
            brand__icontains = request.GET.get('brand')
        ).order_by('price')

    if request.GET.get('category'):
        
        products = products.filter(
            category__icontains = request.GET.get('category')
        ).order_by('price')   
    brands=[]   
    categories = []
    if cache.get('brands'):
        brands = cache.get('brands')
    else:
        cache.set("brands",Product.objects.all().distinct('brand').order_by('brand'),60 * 10)
        
    if cache.get("categories"):
        categories = cache.get('categories')
    else:
        cache.set("categories",
               Product.objects.all().distinct('category').order_by('category'), 60 * 10 )
        
    # brands = Product.objects.all().distinct('brand').order_by('brand')
    categories = Product.objects.all().distinct('category').order_by('category')
    context = {"products": products, "search": search,"brands":brands,"categories":categories}
    return render(request, "index.html", context)
