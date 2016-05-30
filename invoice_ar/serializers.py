from rest_framework.serializers import HyperlinkedModelSerializer

from contact.models import Contact
from invoice.serializers import (CompanyInvoiceSerializer,
                                 ContactInvoiceSerializer)
from invoice.models import ContactInvoice
from invoice_ar import models
from persons.models import PhysicalAddress


class ContactInvoiceARSerializer(HyperlinkedModelSerializer):
    invoice_contact = ContactInvoiceSerializer()

    class Meta:
        model = models.ContactInvoiceAR
        fields = (
            'url',
            'id',
            'invoice_contact',
            'id_type',
            'id_number'
        )
        extra_kwargs = {
            'url': {
                'view_name': 'api:invoice_ar:contactinvoicear-detail'
            }
        }

    def create(self, validated_data):
        invoice_contact_data = validated_data['invoice_contact']
        contact_contact_data = invoice_contact_data.pop('contact_contact')
        home_address_data = contact_contact_data.get('home_address', None)
        if home_address_data is not None and (
            home_address_data['home_address'] is not ''
        ):
            home_address = PhysicalAddress.objects.create(
                **home_address_data
            )
            contact_contact_data['home_address'] = home_address

        contact_contact = Contact.objects.create(
            **contact_contact_data
        )
        invoice_contact_data['contact_contact'] = contact_contact

        fiscal_address_data = invoice_contact_data.pop('fiscal_address')
        fiscal_address = PhysicalAddress.objects.create(
            **fiscal_address_data
        )
        invoice_contact_data['fiscal_address'] = fiscal_address
        invoice_contact = ContactInvoice.objects.create(
            **invoice_contact_data
        )
        validated_data['invoice_contact'] = invoice_contact
        invoicear_contact = models.ContactInvoiceAR.objects.create(
            **validated_data
        )
        return invoicear_contact

    def update(self, instance, validated_data):
        invoice_contact_data = validated_data.pop('invoice_contact_data')
        contact_contact_data = invoice_contact_data.pop('contact_contact')
        home_address_data = contact_contact_data.get('home_address', None)
        if home_address_data is not None and (
            home_address_data['home_address'] is not ''
        ):
            home_address = PhysicalAddress.objects.update_or_create(
                **home_address_data
            )
            contact_contact_data['home_address'] = home_address

        contact_contact = Contact.objects.update_or_create(
            **contact_contact_data
        )
        invoice_contact_data['contact_contact'] = contact_contact

        fiscal_address_data = invoice_contact_data.pop('fiscal_address')
        fiscal_address = PhysicalAddress.objects.update_or_create(
            **fiscal_address_data
        )
        invoice_contact_data['fiscal_address'] = fiscal_address
        invoice_contact = ContactInvoice.objects.update_or_create(
            **invoice_contact_data
        )
        validated_data['invoice_contact'] = invoice_contact
        instance.update(**validated_data)
        return instance


class CompanyInvoiceARSerializer(HyperlinkedModelSerializer):
    invoice_company = CompanyInvoiceSerializer()

    class Meta:
        model = models.CompanyInvoiceAR
        fields = (
            'url',
            'id',
            'invoice_company',
            'cuit',
            'iibb'
        )
        extra_kwargs = {
            'url': {
                'view_name': 'api:invoice_ar:companyinvoicear-detail'
            }
        }
