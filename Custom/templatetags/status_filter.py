from django import template
register = template.Library()

@register.filter(name="status_reporter")
def status_reporter(status):
	if status == "0":
		corresponding_status = 'Completed'
	elif status == "1":
		corresponding_status = 'Almost there'
	elif status == "2":
		corresponding_status = 'Under progression'
	elif status == "3":
		corresponding_status = 'Initialized'
	return corresponding_status				