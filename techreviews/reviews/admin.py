from django.contrib import admin
from .models import TechType, TechProduct, TechReview


admin.site.register(TechType)
admin.site.register(TechProduct)
admin.site.register(TechReview)
