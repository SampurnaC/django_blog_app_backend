from .models import Blog, Category
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import BlogSerializer, CategorySerializer
from rest_framework import filters, generics
from rest_framework.pagination import PageNumberPagination
from django.shortcuts import get_object_or_404, redirect
from bs4 import BeautifulSoup
import requests
from PIL import Image
from django.contrib import messages


@api_view(['GET'])
def blogList(request):
    paginator = PageNumberPagination()
    paginator.page_size = 6
    blogs = Blog.objects.get_queryset().order_by('id')
    result_page = paginator.paginate_queryset(blogs, request)
    serializer = BlogSerializer(result_page, many=True)
    return paginator.get_paginated_response(serializer.data)

    


@api_view(['GET'])
def blogDetail(request,pk):
    blog = Blog.objects.get(id=pk)
    serializer = BlogSerializer(blog, many=False)
    return Response(serializer.data)

@api_view(['POST'])
def blogCreate(request):
    serializer = BlogSerializer(data=request.data)

    if serializer.is_valid():
        post = serializer.validated_data
        website = requests.get(request.data['url'])
        sourcecode = BeautifulSoup(website.text, 'html.parser')
        # image = sourcecode.find('img', class_='tB6UZ').get('src')
        image = sourcecode.find('img', class_='ApbSI').get('src')
        post['image'] = image
        # find_title = sourcecode.select('h1.la4U2')
        find_title = sourcecode.select('h1.z5s87')
        
        try:
            name = find_title[0].text.strip()
            post['name'] = name
        except IndexError as e:
            print(f"IndexError: {e}")
        # find_artist = sourcecode.select('a.N2odk')
        find_artist = sourcecode.select('a.BkSVh')
        
        try:
            artist = find_artist[0].text.strip() 
            post['artist'] = artist
        except IndexError as e:
            print(f"IndexError: {e}")
        serializer.save()

    return Response(serializer.data)


@api_view(['PUT'])
def blogUpdate(request, pk):
    blog = Blog.objects.get(id=pk)
    serializer = BlogSerializer(instance=blog, data=request.data)

    if serializer.is_valid():
        serializer.save()
    
    return Response(serializer.data)

@api_view(['DELETE'])
def blogDelete(request, pk):
    blog = Blog.objects.get(id=pk)
    blog.delete()

    return Response('Deleted successfully')


@api_view(['GET'])
def blogSearch(request):
    q = request.GET['search']
    blog = Blog.objects.filter(name__icontains=q)
    serializer = BlogSerializer(blog, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def blogPaginate(request):
    paginator = PageNumberPagination()
    paginator.page_size = 1
    blogs = BLog.objects.all()
    result_page = paginator.paginate_queryset(blogs, request)
    serializer = BlogSerializer(result_page, many=True)
    return paginator.get_paginated_response(serializer.data)


@api_view(['GET'])
def categoryLists(request):
    categories = Category.objects.all()
    serializer = CategorySerializer(categories, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def categoryBlogs(request, slug):
    category_blogs = Blog.objects.filter(category=slug)
    serializer = BlogSerializer(category_blogs, many=True)
    return Response(serializer.data)
