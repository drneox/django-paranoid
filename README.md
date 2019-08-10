
# django-paranoid
this library adds 'created_at', 'updated_at' and 'delete_at'  fields like a rail apps in django, also added soft delete method.


## install

    pip install django-paranoid

## How to start
1.- Add to django-paranoid in the django apps:

    INSTALLED_APPS = [
        'django.contrib.admin',
      'django.contrib.auth',
            ...
      'django-paranoid'
      ...
    ]
2.- Extends ParanoidModel in the model to use:

    from django_paranoid.models import ParanoidModel

    class MyModel(ParanoidModel):
        field = models.CharField(max_length=20)

3.- Add to django-admin:

    from django_paranoid.admin import ParanoidAdmin

    class MyModelAdmin(ParanoidAdmin):
        pass
      ...
    admin.site.register(MyModel, MyModelAdmin)
    
    
## Soft Delete
    
    m = MyModel.objects.last()
    m.delete()
    

This only applies soft delete, so the record will remain in the database, but it will not be visible for normal queries:
    
    m = MyModel.objects.last()
    >>> m
    >>>

Now the record has a deleted_at field and if do you want show the delete record you could using 'objects_with_deleted':

    m = MyMode.objects_with_deleted.last()
    >>> m
    <MyModel: name>
    >>> m.deleted_at
    datetime.datetime(2019, 8, 10, 6, 16, 44, 633727, tzinfo=<UTC>)

    
