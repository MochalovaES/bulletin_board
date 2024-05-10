from rest_framework import serializers

from ads.models import Comment, Ad


# TODO Сериалайзеры. Предлагаем Вам такую структуру, однако вы вправе использовать свою

class CommentSerializer(serializers.ModelSerializer):
    """"Класс-сериализатор для модели Comment"""
    author_first_name = serializers.CharField(source="author.first_name", read_only=True)
    author_last_name = serializers.CharField(source="author.last_name", read_only=True)
    author_image = serializers.CharField(source="author.image", read_only=True)

    class Meta:
        model = Comment
        fields = '__all__'

    def get_author_image(self, obj):
        request = self.context.get("request")
        if obj.author.image:
            return request.build_absolute_uri(obj.author.image.url)


class AdSerializer(serializers.ModelSerializer):
    """Класс-сериализатор для модели Ad"""
    class Meta:
        model = Ad
        fields = ('pk', 'title', 'price', 'description', 'created_at')


class AdDetailSerializer(serializers.ModelSerializer):
    """Класс-сериализатор для просмотра детальной информации по объявлению"""
    author_first_name = serializers.CharField(source="author.first_name", read_only=True)
    author_last_name = serializers.CharField(source="author.last_name", read_only=True)
    author_email = serializers.CharField(source="author.email", read_only=True)
    author_phone = serializers.CharField(source="author.phone", read_only=True)

    class Meta:
        model = Ad
        fields = '__all__'
