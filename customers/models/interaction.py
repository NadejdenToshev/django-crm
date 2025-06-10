from django.db import models
from .customer import Customer

class Interaction(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name='interactions')
    date = models.DateTimeField(auto_now_add=True)
    note = models.TextField()
    attachment = models.FileField(upload_to='attachments/', blank=True, null=True)

    def __str__(self):
        return f"{self.customer.name} - {self.date.strftime('%Y-%m-%d')}"