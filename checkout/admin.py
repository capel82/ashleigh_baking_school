from django.contrib import admin
from .models import Order, OrderLineItem

#allowing order items to be edited in the admin
class OrderLineItemAdminInline(admin.TabularInline):
    model = OrderLineItem
    readonly_fields = ('lineitem_total',)


class OrderAdmin(admin.ModelAdmin):
    inlines = (OrderLineItemAdminInline,)

    #fields that cannot be edited'readonly_fields'
    readonly_fields = ('order_number', 'date',
                       'grand_total', 'original_bag',
                       'stripe_pid')

    #fields that can be edited.
    fields = ('order_number', 'date', 'full_name',
              'email', 'phone_number', 'country',
              'postcode', 'town_or_city', 'street_address1',
              'street_address2', 'county','grand_total',
              'orginal_bag', 'stripe_pid',)

    list_display = ('order_number', 'date', 'full_name',
                    'street_address1','town_or_city','grand_total',)

    ordering = ('-date',)

admin.site.register(Order, OrderAdmin)