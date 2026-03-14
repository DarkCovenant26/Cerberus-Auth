from django_tenants.models import TenantMixin, DomainMixin
from django.db import models


class Tenant(TenantMixin):
    """
    Represents an organization/tenant in the system.

    django-tenants creates a dedicated PostgreSQL schema for each Tenant
    instance, ensuring hard data isolation between organizations.
    Every table in TENANT_APPS is replicated per schema.
    """

    name = models.CharField(max_length=255, unique=True)
    slug = models.SlugField(max_length=100, unique=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    # TenantMixin requires this — automatically creates the schema on save
    auto_create_schema = True

    class Meta:
        verbose_name = "Tenant"
        verbose_name_plural = "Tenants"

    def __str__(self) -> str:
        return self.name


class Domain(DomainMixin):
    """
    Maps a hostname to a Tenant.

    django-tenants resolves the incoming request's Host header against this
    table to determine which schema (tenant) to activate for the request.

    Example: api.acme.com  →  Tenant(slug='acme')
    """

    class Meta:
        verbose_name = "Domain"
        verbose_name_plural = "Domains"

    def __str__(self) -> str:
        return self.domain
