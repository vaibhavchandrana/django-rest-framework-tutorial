from django.contrib import admin
from movies_app.models import WatchList,StreamingPlateform,Reviews
# Register your models here.
admin.site.register(WatchList)
admin.site.register(StreamingPlateform)
admin.site.register(Reviews)