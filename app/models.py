
from tortoise import fields
from tortoise.models import Model

class Product(Model):
    id = fields.IntField(pk=True)
    name = fields.CharField(max_length=100)
    price = fields.DecimalField(max_digits=10, decimal_places=2)
    stockQnt = fields.IntField()
    
    def __str__(self):
        return f"Product(id={self.id}, name={self.name}, price={self.price}, stockQnt={self.stockQnt})"