
# django-loggable
this library adds 'created_at', 'updated_at' and 'delete_at'  fields like a rail apps in django, also added soft delete method.


## install

    pip install django-loggable

## How to start
1.- Add to django-loggable in the django apps:

    INSTALLED_APPS = [  
        'django.contrib.admin',  
      'django.contrib.auth',    
            ... 
      'django-loggable'
      ...  
    ]
2.- Extends LoggableModel in the model to use:

    class MyModel(LoggeableModel):  
        field = models.CharField(max_length=20)  

3.- Add to django-admin:

    class ContactAdmin(LoggeableAdmin):  
        pass  
      ...
    admin.site.register(Contact, ContactAdmin)
