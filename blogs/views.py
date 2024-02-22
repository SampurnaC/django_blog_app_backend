from .models import Blog
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import BlogSerializer
# from rest_framework import viewsets

# class BlogView(viewsets.ModelViewSet):
#     queryset = Blog.objects.all()
#     serializer_class = BlogSerializer

@api_view(['GET'])
def blogList(request):
    blogs = Blog.objects.all()
    serializer = BlogSerializer(blogs, many=True)
    return Response(serializer.data)

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
