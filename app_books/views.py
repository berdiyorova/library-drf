from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response

from app_books.models import BookModel, AuthorModel
from app_books.serializers import BookModelSerializer, AuthorModelSerializer

@api_view(['GET', 'POST'])
def author_list_create_view(request):
    """
    Get authors list or add new author to database
    :param request:
    :return:
    """
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


@api_view(['GET', 'PUT', 'PATCH', 'DELETE'])
def author_detail(request, pk):
    """
    Get author by id and update or delete the author
    :param request:
    :param pk:
    :return:
    """
    author = get_object_or_404(AuthorModel, pk=pk)

    if request.method == 'GET':
        data = AuthorModelSerializer(author).data
        return Response(data=data, status=status.HTTP_200_OK)

    elif request.method == 'PUT':
        serialized_data = AuthorModelSerializer(author, data=request.data)
        serialized_data.is_valid(raise_exception=True)

        serialized_data.save()
        return Response(
            {
                'success': True,
                'message': 'Author is updated',
                'data': serialized_data.data,
            },
            status=status.HTTP_200_OK
        )

    elif request.method == 'PATCH':
        serialized_data = AuthorModelSerializer(author, data=request.data, partial=True)
        serialized_data.is_valid(raise_exception=True)

        serialized_data.save()
        return Response(
            {
                'success': True,
                'message': 'Author is partially updated',
                'data': serialized_data.data,
            },
            status=status.HTTP_200_OK
        )

    elif request.method == 'DELETE':
        author.delete()
        return Response(
            {
                'success': True,
                'message': 'Author is deleted',
            },
            status=status.HTTP_204_NO_CONTENT
        )


# -----------------------------------------------------------------------------------------------------------


@api_view(['GET', 'POST'])
def book_list_create_view(request):
    """
    Get books list or create new book
    :param request:
    :return:
    """
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


@api_view(['GET', 'PUT', 'PATCH', 'DELETE'])
def book_detail(request, pk):
    """
    Get book by id and update or delete the book
    :param request:
    :param pk:
    :return:
    """
    book = get_object_or_404(BookModel, pk=pk)

    if request.method == 'GET':
        data = BookModelSerializer(book).data
        return Response(data=data, status=status.HTTP_200_OK)

    elif request.method == 'PUT':
        serialized_data = BookModelSerializer(book, data=request.data)
        serialized_data.is_valid(raise_exception=True)

        serialized_data.save()
        return Response(
            {
                'success': True,
                'message': 'Book is updated',
                'data': serialized_data.data,
            },
            status=status.HTTP_200_OK
        )

    elif request.method == 'PATCH':
        serialized_data = BookModelSerializer(book, data=request.data, partial=True)
        serialized_data.is_valid(raise_exception=True)

        serialized_data.save()
        return Response(
            {
                'success': True,
                'message': 'Book is partially updated',
                'data': serialized_data.data,
            },
            status=status.HTTP_200_OK
        )

    elif request.method == 'DELETE':
        book.delete()
        return Response(
            {
                'success': True,
                'message': 'Book is deleted',
            },
            status=status.HTTP_204_NO_CONTENT
        )
