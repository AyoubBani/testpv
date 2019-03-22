# -*- coding: utf-8 -*-
from django.views.generic import ListView

from mailer.models import Company, Contact
from django.db.models import Prefetch, Sum, Count


class IndexView(ListView):
    template_name = "mailer/index.html"

    contacts_with_orders = Prefetch(
        'contacts',
        queryset=Contact.objects.annotate(order_count=Count('orders'))
    )
    queryset = (Company.objects
                    .prefetch_related(contacts_with_orders)
                    .annotate(order_sum=Sum('orders__total'),
                              order_count=Count('orders'))
                    )
    # queryset = Company.objects.prefetch_related('contacts', 'orders')
    # model = Company
    paginate_by = 100
