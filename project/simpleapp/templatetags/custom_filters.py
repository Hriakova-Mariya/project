from django import template

register = template.Library()

CURRENCIES_SYMBOLS = {
   'rub': 'Р',
   'usd': '$',
}

@register.filter()
def currency(value):
    postfix = CURRENCIES_SYMBOLS['rub']

    return f'{value} {postfix}'
