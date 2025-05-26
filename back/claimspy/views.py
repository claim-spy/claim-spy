from django.forms import ValidationError
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from rest_framework.response import Response
from rest_framework import status

from claimspy.serializers import UserSerializer

from .models import User
from rest_framework_simplejwt.tokens import RefreshToken, TokenError

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (IsAuthenticated,)

    @action(detail=False, methods=['post'], permission_classes=())
    def logout(self, request):
        try:
            refresh_token = request.data["refresh"]
            token = RefreshToken(refresh_token)
            token.blacklist()
            return Response({}, status=status.HTTP_205_RESET_CONTENT)
        except KeyError:
            return Response({"error": "Refresh token required"}, status=status.HTTP_400_BAD_REQUEST)
        except TokenError:
            return Response({"error": "Invalid or expired token"}, status=status.HTTP_400_BAD_REQUEST)

    @action(detail=False, methods=['post'], permission_classes=())
    def authenticate(self, request):
        try:
            user = User.objects.filter(email=request.data.get('email')).first()
            if user and user.check_password(request.data.get('password')):
                refresh = RefreshToken.for_user(user)
                return Response({
                    'refresh': str(refresh),
                    'access': str(refresh.access_token),
                    'user': UserSerializer(user).data
                })
            else:
                raise ValidationError("Invalid credentials")
        except ValidationError as e:
            return Response({'error': e}, status=status.HTTP_400_BAD_REQUEST)

    @action(detail=False, methods=['get'])
    def me(self, request):
        try:
            user = UserSerializer(request.user)
            return Response(user.data)
        except ValidationError as e:
            return Response({'error': e}, status=status.HTTP_400_BAD_REQUEST)
