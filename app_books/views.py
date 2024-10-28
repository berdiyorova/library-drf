from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from app_books.models import BookModel, AuthorModel
from app_books.serializers import BookModelSerializer, AuthorModelSerializer

@api_view(['GET', 'POST'])
def author_list_create_view(request):
    if request.method == 'GET':
        authors = AuthorModel.objects.all()
        data = AuthorModelSerializer(authors, many=True).data
        return Response(data=data, status=status.HTTP_200_OK)

    elif request.method == 'POST':
        serialized_data = AuthorModelSerializer(data=request.data)
        serialized_data.is_valid(raise_exception=True)

        AuthorModel.objects.create(**serialized_data.data)
        return Response(
            {
                'success': True,
                'message': 'Author is added',
                'data': serialized_data.data,
            },
            status=status.HTTP_201_CREATED
        )


@api_view(['GET', 'POST'])
def book_list_create_view(request):
    if request.method == 'GET':
        books = BookModel.objects.all()
        data = BookModelSerializer(books, many=True).data
        return Response(data=data, status=status.HTTP_200_OK)

    elif request.method == 'POST':
        serialized_data = BookModelSerializer(data=request.data)
        serialized_data.is_valid(raise_exception=True)

        serialized_data.save()
        return Response(
            {
                'success': True,
                'message': 'Book is added',
                'data': serialized_data.data,
            },
            status=status.HTTP_201_CREATED
        )
