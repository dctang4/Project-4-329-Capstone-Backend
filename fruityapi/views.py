from django.http import JsonResponse
from django.views import View 

from .models import Fruity
from django.core.serializers import serialize
from json import loads

# Create your views here.
class FruityView(View):
  def get(self, request):
    # Serialize the data into JSON then turn the JSON into a dict
    all = loads(serialize('json', Fruity.objects.all()))
    # Send the JSON response
    return JsonResponse(all, safe=False)

  def post(self, request):
    # Turn the body into a dict
    body = loads(request.body.decode("utf-8"))
    #create the new item
    newrecord = Fruity.objects.create(
      name=body['name'], 
      type=body['type'],
      description=body['description'], 
      price=body['price'],
    )
    # Turn the object to json to dict, put in array to avoid non-iterable error
    data = loads(serialize('json', [newrecord]))
    # send json response with new object
    return JsonResponse(data, safe=False)

class OneFruityView(View):
  def get(self, request, param):
    # Filter and find a single item then serialize the data into JSON then turn the JSON into a dict
    one = loads(serialize("json", Fruity.objects.filter(name=param)))
    # Send the JSON response
    return JsonResponse(one, safe=False)

  def put(self, request, param):
    # Turn the body into a dict
    body = loads(request.body.decode("utf-8"))
    # update the item
    Fruity.objects.filter(name=param).update(
      name=body['name'], 
      type=body['type'],
      description=body['description'], 
      price=body['price'],
    )
    newrecord = Fruity.objects.filter(name=param)
    # Turn the object to json to dict, put in array to avoid non-iterable error
    data = loads(serialize('json', newrecord))
    # send json response with updated object
    return JsonResponse(data, safe=False)

  def delete(self, request, param):
    # delete the item, get all remaining records for response
    Fruity.objects.filter(name=param).delete()
    newrecord = Fruity.objects.all()
    # Turn the results to json to dict, put in array to avoid non-iterable error
    data = loads(serialize('json', newrecord))
    # send json response with updated object
    return JsonResponse(data, safe=False)