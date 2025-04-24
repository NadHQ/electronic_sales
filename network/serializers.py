from rest_framework import serializers

from network.models import Address, NetworkNode


class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = ["country", "city", "street", "building_number"]


class NetworkNodeSerializer(serializers.ModelSerializer):
    class Meta:
        model = NetworkNode
        exclude = ["debt"]
        read_only_fields = ["created_at"]
