from rest_framework import serializers
from .models import Cliente


class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = ["id", "nome", "data_nascimento", "endereco", "telefone", "cpf", "email", "status"]
        read_only_fields = ["id", "criado_em"]
