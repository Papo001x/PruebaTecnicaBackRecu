import graphene
from graphene_django.types import DjangoObjectType
from ventas.models import Product,Customer,Sale
from django.db.models.functions import TruncMonth
from django.db.models import F, Sum, ExpressionWrapper, DecimalField


class ProductType(DjangoObjectType):
    class Meta:
        model = Product

class SaleStatsType(graphene.ObjectType):
    product = graphene.String()
    total_sales = graphene.Int()

class SaleType(DjangoObjectType):
    total_price = graphene.Float()  # campo extra

    class Meta:
        model = Sale

    def resolve_total_price(self, info):
        return float(self.product.price) * self.quantity
    
class SaleStatsType(graphene.ObjectType):
    product = graphene.String()
    total_sales = graphene.Int()

class SaleMonthStatsType(graphene.ObjectType):
    month = graphene.String()  # formato YYYY-MM
    total_sales_amount = graphene.Float()

class Query(graphene.ObjectType):
    all_products = graphene.List(ProductType)
    ventas_totales_por_producto = graphene.List(SaleStatsType)
    all_sales = graphene.List(SaleType)
    ventas_totales_por_producto = graphene.List(SaleStatsType)
    ventas_totales_por_mes = graphene.List(SaleMonthStatsType)

    def resolve_all_products(root, info):
        return Product.objects.all()

    def resolve_ventas_totales_por_producto(root, info):
        from django.db.models import Sum
        data = Sale.objects.values('product__name').annotate(total=Sum('quantity'))
        return [SaleStatsType(product=d['product__name'], total_sales=d['total']) for d in data]

    def resolve_all_sales(self, info):
        return Sale.objects.select_related('product').all()
    
    def resolve_ventas_totales_por_producto(root, info):
        data = (
            Sale.objects
            .values('product__name')
            .annotate(total=Sum('quantity'))
            .order_by('product__name')
        )
        return [
            SaleStatsType(product=item['product__name'], total_sales=item['total'])
            for item in data
        ]
    
    def resolve_ventas_totales_por_mes(root, info):
        data = (
            Sale.objects
            .annotate(month=TruncMonth('date'))
            .annotate(total=ExpressionWrapper(
                F('quantity') * F('product__price'),
                output_field=DecimalField()
            ))
            .values('month')
            .annotate(total_sales=Sum('total'))
            .order_by('month')
        )

        # Convertimos a formato legible
        return [
            SaleMonthStatsType(
                month=item['month'].strftime('%Y-%m'),
                total_sales_amount=float(item['total_sales'])
            )
            for item in data
        ]
schema = graphene.Schema(query=Query)
