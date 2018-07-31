from rest_framework import serializers
from restaurants.models import Restaurant
#from django.http import JsonResponse, Response

class RestaurantListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Restaurant
        fields = [
			'id',
        	'owner',
			'name',
        	'description',
        	'opening_time',
        	'closing_time',
        	]

class RestaurantRetreiveSerializer(serializers.ModelSerializer):
    class Meta:
        model = Restaurant
        fields = [
			'id',
        	'owner',
			'name',
        	'description',
        	'opening_time',
        	'closing_time',
        	]

class RestaurantUpdateSerializer(serializers.ModelSerializer):
	class Meta:
		model = Restaurant
		fields = [
			'id',
			'owner',
			'name',
			'description',
			'opening_time',
			'closing_time',]
		read_only_fields = ['id', 'owner',]

	# def update(self, request, *args, **kwargs):
	# 	instance = self.get_object()
	# 	instance.name = request.data.get('name')
	# 	instance.description = request.data.get('description')
	# 	instance.opening_time = request.data.get('opening_time')
	# 	instance.closing_time = request.data.get('closing_time')
	# 	instance.save()

	# 	serializer = self.get_serializer(instance)
	# 	serializer.is_valid(raise_exception=True)
	# 	self.perform_update(serializer)
	# 	return Response(serializer.data)