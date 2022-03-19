from datetime import date

from django import template

register = template.Library()


@register.filter(name='find_date_of_birth')
def find_age(input_year):
    today_year = date.today().year

    return today_year - input_year
