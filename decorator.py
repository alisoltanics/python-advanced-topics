def validate_user(get):
    def validate(self, request):
        if user.is_suspended:
            raise SuspendedError
        get(self, request)
    return validate

class BookListAPIView(APIView):
    """Returns a list of Books data as API."""

    permission_classes = (IsAuthenticated, )

    @validate_user
    def get(self, request):
        pass