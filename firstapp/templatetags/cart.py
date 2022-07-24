from django import template

register = template.Library()

@register.filter(name='multiply')
def multiply(number , number1):
    return number * number1

@register.filter(name='is_in_cart')
def is_in_cart(items, cart):
    keys = cart.keys()
    for id in keys:
        if int(id) == items.id:
            return True
    return False

@register.filter(name='is_empty')
def is_empty(items, cart):
    if not cart:
        return False
    else:
        return True

@register.filter(name='cart_quantity')
def cart_quantity(items, cart):
    keys = cart.keys()
    for id in keys:
        if int(id) == items.id:
            return cart.get(id)
    return 0

@register.filter(name='total_price')
def total_price(items, cart):
    return items.price * cart_quantity(items, cart)

@register.filter(name='total_cart_price')
def total_cart_price(items , cart):
    sum = 0
    for i in items:
        sum += total_price(i , cart)
    return sum

@register.filter(name='total')
def total(items , cart):
    if is_empty(items, cart):
        sum = 100 + total_cart_price(items, cart)
    else:
        sum = 0
    return sum