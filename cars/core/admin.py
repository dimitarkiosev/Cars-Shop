from django.contrib import admin

from cars.core.models import CarLike, CarComment


@admin.register(CarLike)
class CarLikeAdmin(admin.ModelAdmin):
    list_display = ('id', 'car', 'user')
    list_filter = ('car', 'user',)

@admin.register(CarComment)
class CarCommentAdmin(admin.ModelAdmin):
    list_display = ('id', 'car', 'user', 'text', )
    list_filter = ('car', 'user', )
