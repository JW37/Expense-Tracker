from django.core.management.base import BaseCommand
from finance.models import Category, SubCategory


DEFAULT_CATEGORIES = {
    'Income': [
        ('Sunday Offerings', ['Morning Service', 'Evening Service']),
        ('Tithes', ['Regular Tithe', 'Special Tithe']),
        ('Special Donations', ['Anonymous', 'Named Donation']),
        ('Festival Contributions', ['Christmas', 'Easter', 'Thanksgiving']),
        ('Building Fund', ['Construction', 'Renovation', 'Maintenance Fund']),
    ],
    'Expense': [
        ('Electricity', ['Monthly Bill', 'Generator']),
        ('Water', ['Monthly Bill', 'Borewell']),
        ('Pastor Salary', ['Head Pastor', 'Associate Pastor']),
        ('Staff Salary', ['Admin Staff', 'Cleaning Staff', 'Security']),
        ('Maintenance', ['Building', 'Equipment', 'Vehicles']),
        ('Charity', ['Food Distribution', 'Medical Aid', 'Education']),
        ('Repairs', ['Electrical', 'Plumbing', 'Structural']),
    ],
}


class Command(BaseCommand):
    help = 'Seed default categories and subcategories for FaithLedger'

    def handle(self, *args, **options):
        created_cats = 0
        created_subs = 0

        for cat_type, cat_list in DEFAULT_CATEGORIES.items():
            for cat_name, subcats in cat_list:
                cat, cat_created = Category.objects.get_or_create(
                    name=cat_name,
                    type=cat_type,
                    defaults={'is_active': True}
                )
                if cat_created:
                    created_cats += 1
                    self.stdout.write(f'  Created category: {cat_name} ({cat_type})')

                for sub_name in subcats:
                    sub, sub_created = SubCategory.objects.get_or_create(
                        category=cat,
                        name=sub_name,
                        defaults={'is_active': True}
                    )
                    if sub_created:
                        created_subs += 1

        self.stdout.write(self.style.SUCCESS(
            f'\n✅ Seeding complete!\n'
            f'   Categories created: {created_cats}\n'
            f'   Sub-categories created: {created_subs}'
        ))
