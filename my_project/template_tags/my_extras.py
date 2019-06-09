from django import template
register=template.library()

def cut(value,arg):
    return value.replace(arg,"ABC")
register.filter('cut1',cut)
