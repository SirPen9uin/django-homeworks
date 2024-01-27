from django.contrib.auth.models import User
from rest_framework import serializers

from advertisements.models import Advertisement, FavoriteAdvertisement


class UserSerializer(serializers.ModelSerializer):
    """Serializer для пользователя."""

    class Meta:
        model = User
        fields = ('id', 'username', 'first_name',
                  'last_name',)


class AdvertisementSerializer(serializers.ModelSerializer):
    """Serializer для объявления."""

    creator = UserSerializer(
        read_only=True,
    )

    is_favorited = serializers.SerializerMethodField()

    class Meta:
        model = Advertisement
        fields = ('id', 'title', 'description', 'creator',
                  'status', 'created_at', 'is_favorited')

    def create(self, validated_data):
        """Метод для создания"""
        validated_data["creator"] = self.context["request"].user
        return super().create(validated_data)

    def validate(self, data):
        """Метод для валидации. Вызывается при создании и обновлении."""
        user = self.context['request'].user
        if Advertisement.objects.all().filter(creator=self.context['request'].user, status='OPEN').count() >= 5 and data.get('status') not in ['CLOSED', 'DRAFT']:
            raise serializers.ValidationError('У нас не может быть больше 5 открытых объявлений')
        return data

    def get_is_favorited(self, obj):
        user = self.context['request'].user
        if user.is_authenticated:
            return FavoriteAdvertisement.objects.filter(user=user, advertisement=obj).exists()
        return False


class FavoriteAdvertisementSerializer(serializers.ModelSerializer):
    title = serializers.CharField(source='advertisement.title', read_only=True)
    description = serializers.CharField(source='advertisement.description', read_only=True)
    creator = serializers.PrimaryKeyRelatedField(source='advertisement.creator', read_only=True)
    status = serializers.CharField(source='advertisement.status', read_only=True)
    created_at = serializers.DateTimeField(source='advertisement.created_at', read_only=True)

    is_favorited = serializers.BooleanField(default=True)

    class Meta:
        model = FavoriteAdvertisement
        fields = ['advertisement', 'title', 'description', 'creator', 'status', 'created_at', 'is_favorited']
