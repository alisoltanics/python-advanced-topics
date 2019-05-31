def validate_user(get):
    def validate(self, request):
        if user.is_suspended:
            raise SuspendedError
        get(self, request)
    return validate

class TopicsListAPIView(APIView):
    """Returns a list of Topics data as API."""

    permission_classes = (IsAuthenticated, )

    @validate_user
    def get(self, request):
        pass