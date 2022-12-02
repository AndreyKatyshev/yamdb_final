from django.db.models import Avg
from django.utils import timezone
from rest_framework import serializers
from reviews.models import Category, Comment, Genre, Review, Title


class ReviewSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(
        read_only=True, slug_field='username')

    class Meta:
        model = Review
        fields = ('id', 'author', 'text', 'pub_date', 'score',)

    def validate(self, data):
        desired_review = Review.objects.filter(
            title_id=self.context['view'].kwargs.get('title_id'),
            author=self.context['request'].user
        )
        if self.context['request'].method == 'POST':
            if desired_review:
                raise serializers.ValidationError(
                    'Нельзя писать больше одного отзыва!')
        return data


class CommentSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(
        read_only=True, slug_field='username')

    class Meta:
        model = Comment
        fields = ('id', 'author', 'review', 'text', 'pub_date')
        read_only_fields = ('review',)


class RatingSerializer(serializers.ModelSerializer):
    #     rating = serializers.SerializerMethodField()

    #     class Meta:
    #         fields = '__all__'
    #         model = Score
    #         read_only_fields = ('title',)

    #     def get_rating(self, obj):
    pass


class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = ('name', 'slug')


class GenreSerializer(serializers.ModelSerializer):

    class Meta:
        model = Genre
        fields = ('name', 'slug')


class TitleCreateSerializer(serializers.ModelSerializer):
    category = serializers.SlugRelatedField(
        slug_field='slug', queryset=Category.objects.all(),
    )
    genre = serializers.SlugRelatedField(
        slug_field='slug', queryset=Genre.objects.all(), many=True
    )

    class Meta:
        model = Title
        fields = (
            'id', 'name', 'year', 'description', 'genre', 'category'
        )

    def validate_year(self, value):
        current_year = timezone.now().year
        if not 0 <= value <= current_year:
            raise serializers.ValidationError(
                'Не верный год создания произведения'
            )
        return value


class TitleSerializer(serializers.ModelSerializer):
    rating = serializers.SerializerMethodField()
    category = CategorySerializer()
    genre = GenreSerializer(many=True)

    class Meta:
        model = Title
        fields = (
            'id', 'name', 'year', 'rating', 'description', 'genre', 'category'
        )

    def get_rating(self, obj):
        rating = obj.reviews.aggregate(Avg('score')).get('score__avg')
        if not rating:
            return rating
        return round(rating, 1)
