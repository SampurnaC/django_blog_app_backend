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

# from rest_framework import viewsets

# class BlogView(viewsets.ModelViewSet):
#     queryset = Blog.objects.all()
#     serializer_class = BlogSerializer


# @api_view(['GET'])
# def blogLists(request):
#     blogs = Blog.objects.all()
#     serializer = BlogSerializer(blogs, many=True)
#     return Response(serializer.data)


@api_view(['GET'])
def blogList(request):
    paginator = PageNumberPagination()
    paginator.page_size = 6

    blogs = Blog.objects.get_queryset().order_by('id')
    # blogs = Blog.objects.all()

    result_page = paginator.paginate_queryset(blogs, request)

    serializer = BlogSerializer(result_page, many=True)
    # return Response(serializer.data)
    return paginator.get_paginated_response(serializer.data)


@api_view(['GET'])
def blogDetail(request,pk):
    blog = Blog.objects.get(id=pk)
    serializer = BlogSerializer(blog, many=False)
    return Response(serializer.data)

@api_view(['POST'])
def blogCreate(request):
    # breakpoint()
    serializer = BlogSerializer(data=request.data)

    # file = request.data['image']
    if serializer.is_valid():

        # post = serializer.save(commit=False)
        post = serializer.validated_data
        # website = requests.get(request.data['url'])
        # breakpoint()



        website = requests.get(request.data['url'])

        sourcecode = BeautifulSoup(website.text, 'html.parser')


        image = sourcecode.find('img', class_='tB6UZ').get('src')


        # find_image = sourcecode.select('meta[content^="https://unsplash.com/photos/"]')

        
        # try:
        #     image = find_image[0]['content']
        #     # imgsize = Image.open(requests.get(img['src'], stream=True).raw)

        # except:
        #     messages.error(request, 'Requested image is not on Flickr!')
        #     return redirect('blog-list')
        post['image'] = image
        


        # sourcecode.select('.MorZF')


        find_title = sourcecode.select('h1.la4U2')
        try:
            # breakpoint()
            name = find_title[0].text.strip()
            post['name'] = name
            # serializer.name=name
            # serializer.update(name=name)

        except IndexError as e:
            print(f"IndexError: {e}")

        



        find_artist = sourcecode.select('a.N2odk')
        try:

            artist = find_artist[0].text.strip() 
            # post.artist = artist
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

# class BlogsAPIView(generics.ListCreateAPIView):
#     search_fields = ['name']
#     filter_backends = (filters.SearchFilter,)
#     queryset = Blog.objects.all()
#     serializer_class = BlogSerializer

@api_view(['GET'])
def blogSearch(request):
    q = request.GET['search']
    blog = Blog.objects.filter(name__icontains=q)
    serializer = BlogSerializer(blog, many=True)
    return Response(serializer.data)

@api_view(['GET'])

# @permission_classes([AllowAny,])

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
