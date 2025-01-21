from django.contrib import admin
from .models import User, Coords, Level, Pereval, Image

class ImageInline(admin.TabularInline):
    model = Image
    extra = 1
    fk_name = 'pereval'  # Явное указание связи

@admin.register(Pereval)
class PerevalAdmin(admin.ModelAdmin):
    list_display = ('title', 'beauty_title', 'status', 'add_time')
    list_filter = ('status', 'add_time')
    search_fields = ('title', 'beauty_title')
    inlines = [ImageInline]

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('email', 'fam', 'name', 'phone')
    search_fields = ('email', 'fam')

@admin.register(Coords)
class CoordsAdmin(admin.ModelAdmin):
    list_display = ('latitude', 'longitude', 'height')

@admin.register(Level)
class LevelAdmin(admin.ModelAdmin):
    list_display = ('winter', 'summer', 'autumn', 'spring')

@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    list_display = ('title', 'pereval')