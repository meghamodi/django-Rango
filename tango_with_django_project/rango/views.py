from django.http import HttpResponse
from django.template import RequestContext
from django.shortcuts import render_to_response
from rango.models import Category
from rango.models import Page


def index(request):
    context = RequestContext(request)
     # Request the context of the request.
    # The context contains information such as the client's machine details, for example.
    category_list = Category.objects.order_by('-likes')[:5]
    context_dict = {'categories': category_list}
    # Construct a dictionary to pass to the template engine as its context.
    # Note the key boldmessage is the same as {{ boldmessage }} in the template!
    for category in category_list:
        category.url = category.name.replace(' ', '_')
# Render the response and return to the client.
    return render_to_response('rango/index.html', context_dict, context)

def about(request):
    return render_to_response('rango/about.html', request)
    return HttpResponse("Rango Says: Here is the about page.<br /><a href='/rango/'>Index</a>")

def category(request, category_name_url):

    context = RequestContext(request)

    category_name = category_name_url.replace('_', ' ')
# Create a context dictionary which we can pass to the template rendering engine.
# We start by containing the name of the category passed by the user.
    context_dict = {'category_name': category_name}
    try:
# Can we find a category with the given name?
# If we can't, the .get() method raises a DoesNotExist exception.
# So the .get() method returns one model instance or raises an exception.
        category = Category.objects.get(name=category_name)
# Retrieve all of the associated pages.
# Note that filter returns >= 1 model instance.
        pages = Page.objects.filter(category=category)
        context_dict['pages'] = pages
# We also add the category object from the database to the context dictionary.
# We'll use this in the template to verify that the category exists.
        context_dict['category'] = category
    except Category.DoesNotExist:
# We get here if we didn't find the specified category.
# Don't do anything - the template displays the "no category" message for us.
        pass
# Go render the response and return it to the client.
    return render_to_response('rango/category.html', context_dict, context)
