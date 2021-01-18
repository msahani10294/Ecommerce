from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=20)

    @staticmethod
    def get_all_categories():
        return Category.objects.all()


    def __str__(self):
        return self.name

class Product(models.Model):

    name  = models.CharField(max_length=200)
    price = models.IntegerField(default=0)
    description = models.CharField(max_length=200)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    image  = models.ImageField(upload_to='media/')

    def __str__(self):
        return str(self.name)

