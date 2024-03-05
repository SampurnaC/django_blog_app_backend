from .models import Blog, Category
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import BlogSerializer, CategorySerializer
from rest_framework import filters, generics
from rest_framework.pagination import PageNumberPagination
from django.shortcuts import get_object_or_404

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
