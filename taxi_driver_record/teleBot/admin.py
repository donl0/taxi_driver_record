from django.contrib import admin

# Register your models here.
from django.contrib import admin
from django.contrib.admin import AdminSite
from .import models


class MyAdminSite(AdminSite):

    def get_app_list(self, request):
        """
        Return a sorted list of all the installed apps that have been
        registered in this site.
        """
        app_dict = self._build_app_dict(request)

        # Sort the apps alphabetically.
        app_list = sorted(app_dict.values(), key=lambda x: x['name'].lower())

        # Sort the models alphabetically within each app.
        #for app in app_list:
        #    app['models'].sort(key=lambda x: x['name'])

        return app_list
admin.site = MyAdminSite()


class AllUsersSite(admin.ModelAdmin):
    from django.db import models


    #model = models.Requests
    list_display = ['pk', 'fio']


class PhoneNumbersSite(admin.ModelAdmin):
    from django.db import models


    #model = models.Requests
    list_display = ['pk', 'phone_num', 'owner']

# class RelativeOwnerPhoneSite(admin.ModelAdmin):
#     from django.db import models
#
#
#     #model = models.Requests
#     list_display = ['pk', 'name']


admin.site.register(models.AllUsers, AllUsersSite)
admin.site.register(models.PhoneNumbers, PhoneNumbersSite)
#admin.site.register(models.RelativeOwnerPhone, RelativeOwnerPhoneSite)