from car.models import Car

from rest_framework.renderers import JSONRenderer

from car.serializers import CarSerializer
import io
from rest_framework.parsers import JSONParser


def serialize_car_object(car: Car) -> bytes:
    serializer = CarSerializer(instance=car)
    json_data = JSONRenderer().render(serializer.data)
    return json_data


def deserialize_car_object(json: bytes):
    stream = io.BytesIO(json)
    data = JSONParser().parse(stream)
    serializer = CarSerializer(data=data)
    if serializer.is_valid(raise_exception=True):
        car = serializer.save()
        return car
    return None
