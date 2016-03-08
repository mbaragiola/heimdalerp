from rest_framework.serializers import HyperlinkedModelSerializer

from invoice.serializers import ClientSerializer
from invoice.serializers import CompanyInvoiceSerializer
from invoice_ar import models


class ClientARSerializer(HyperlinkedModelSerializer):
    client = ClientSerializer()

    class Meta:
        model = models.ClientAR
        fields = (
            'url',
            'id',
            'client',
            'dni',
            'cuit',
            'cuil'
        )
        extra_kwargs = {
            'url': {
                'view_name': 'api:invoice_ar:clientar-detail'
            }
        }


class CompanyInvoiceARSerializer(HyperlinkedModelSerializer):
    company = CompanyInvoiceSerializer()

    class Meta:
        model = models.CompanyInvoiceAR
        fields = (
            'url',
            'id',
            'company',
            'cuit',
            'iibb'
        )
        extra_kwargs = {
            'url': {
                'view_name': 'api:invoice_ar:companyinvoicear-detail'
            }
        }