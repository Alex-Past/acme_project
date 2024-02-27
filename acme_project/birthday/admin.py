from django.contrib import admin


from .models import Birthday, Tag

# ...и регистрируем её в админке:
admin.site.register(Birthday)
admin.site.register(Tag)