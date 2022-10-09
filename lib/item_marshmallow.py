from .extension import ma

class ItemSchema(ma.Schema):
    class Meta:
        fields = ('id', 'name', 'amount', 'cost',)