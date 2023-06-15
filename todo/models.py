from django.db import models

# Create your models here.


class Item(models.Model):
    """
    Null = false makes sure to create a name
    Blank = false attribute will make sure that entering a name is compulsory 
    and it won't remain empty Default = false makes sure that todo items there
    are not crossed or referenced are marked by default undone.
    """
    name = models.CharField(max_length=50, null=False, blank=False)
    done = models.BooleanField(null=False, blank=False, default=False)
    # allows the todo items added to the list be displayed with the name that
    # has been entered by the
    # admin and not called object item 1 , object item 2
    # (see Models part 2 video)

    def __str__(self):
        return self.name
