class Employee(models.Model):
    fullname = models.CharField(max_length=101, verbose_name="Сотрудник")
    avatar = models.FileField(verbose_name="Аватар")

    def __str__(self):

        return self.fullname


class Product(models.Model):
    name = models.CharField(max_length=202, verbose_name="Название товара")
    price = models.IntegerField(verbose_name="Цена товара")
