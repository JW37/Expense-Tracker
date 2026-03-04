from django.db import models
from django.contrib.auth.models import User


class Category(models.Model):
    TYPE_CHOICES = [('Income', 'Income'), ('Expense', 'Expense')]

    name = models.CharField(max_length=100)
    type = models.CharField(max_length=10, choices=TYPE_CHOICES)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = 'Categories'
        ordering = ['type', 'name']

    def __str__(self):
        return f"{self.name} ({self.type})"

    def can_delete(self):
        return not self.transaction_set.exists()


class SubCategory(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='subcategories')
    name = models.CharField(max_length=100)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'SubCategories'
        ordering = ['name']

    def __str__(self):
        return f"{self.category.name} > {self.name}"


class Transaction(models.Model):
    TYPE_CHOICES = [('Income', 'Income'), ('Expense', 'Expense')]
    STATUS_CHOICES = [('Paid', 'Paid'), ('Pending', 'Pending')]

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField()
    transaction_type = models.CharField(max_length=10, choices=TYPE_CHOICES)
    amount = models.DecimalField(max_digits=12, decimal_places=2)
    category = models.ForeignKey(Category, on_delete=models.PROTECT)
    subcategory = models.ForeignKey(SubCategory, on_delete=models.SET_NULL, null=True, blank=True)
    notes = models.TextField(blank=True)
    is_pending = models.BooleanField(default=False)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='Paid')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-date', '-created_at']

    def __str__(self):
        return f"{self.transaction_type} - {self.amount} on {self.date}"

    def save(self, *args, **kwargs):
        if self.is_pending:
            self.status = 'Pending'
        else:
            self.status = 'Paid'
        super().save(*args, **kwargs)
