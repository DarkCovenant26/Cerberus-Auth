from ninja import NinjaAPI
from ninja.openapi.docs import Swagger, Redoc

api = NinjaAPI(
    title="Cerberus-Auth",
    description=(
        "A Multi-Tenant, Hybrid-RBAC Authorization Engine for Distributed Architectures. "
        "This is the central Policy Decision Point (PDP) — every authorization check flows through here."
    ),
    version="0.1.0",
    docs=Swagger(settings={"persistAuthorization": True}),
    docs_url="/docs/",
)


@api.get("/health", tags=["system"], summary="Health check")
def health_check(request) -> dict:
    """
    Returns 200 if the service is up.
    Downstream services can hit this before making authorization decisions.
    """
    return {"status": "ok", "service": "cerberus-auth"}
