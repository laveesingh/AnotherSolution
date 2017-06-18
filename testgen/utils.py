import random
import string


def generate_integer(context):
    x = int(context['context[from]'])
    y = int(context['context[to]'])
    return str(random.randint(x, y))

def generate_array(context):
    n = int(context['context[no_of_items]'])
    x = int(context['context[from]'])
    y = int(context['context[to]'])
    vertical = str(context['context[vertical]'])
    delim = ' '
    if vertical == "true":
        delim = '<br />'
    array = [str(random.randint(x, y)) for i in xrange(n)]
    return delim.join(array)


def generate_string(context):
    n = int(context['context[no_of_items]'])
    lower = context['context[lower]'] == "true"
    upper = context['context[upper]'] == "true"
    digits = context['context[digits]'] == "true"
    symbols = context['context[symbols]'] == "true"
    binary = context['context[binary]'] == "true"
    custom = context['context[custom]'] == "true"
    special_symbols = "~!@#$%^&*()_+`'\",./<>?\\|;:[]{}-="
    universals = ""
    if lower:
        universals += string.lowercase
    if upper:
        universals += string.uppercase
    if digits:
        universals += string.digits
    if symbols:
        universals += special_symbols
    if binary:
        universals = "01"
    if custom:
        universals = context['context[custom_text]']
    return ''.join(random.choice(universals) for i in xrange(n))


def generate_case_util(request_data):
    if request_data["case_type"] == "integer":
        content = generate_integer(context=request_data)
    elif request_data["case_type"] == "array":
        content = generate_array(context=request_data)
    elif request_data["case_type"] == "string":
        content = generate_string(context=request_data)
    else:
        content = "Not valid"
    return content