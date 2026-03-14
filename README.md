# Cerberus-Auth
"A Multi-Tenant, Hybrid-RBAC Authorization Engine for Distributed Architectures."

🎯 The Mission
In modern enterprise ecosystems, authorization is often an afterthought, hardcoded into business logic or scattered across microservices. This creates "Security Debt" and makes compliance auditing a nightmare.

This project provides a centralized Policy Decision Point (PDP) that decouples identity management from application logic. It is designed specifically for GRC-heavy environments where "Who has access to what" must be immutable, auditable, and performant.

🏗️ Architectural Core
The system utilizes a Hybrid-RBAC model. While it manages traditional Role-Based Access Control at its core, it is architected to support Attribute-Based (ABAC) constraints, allowing for context-aware permissions (e.g., restricting access based on IP range, time of day, or resource ownership).

🚀 Key Features
True Multi-Tenancy: Data isolation at the schema level, ensuring that tenant permissions never leak across organizational boundaries.

Contextual Policy Engine: Beyond simple roles, it supports JSONB-based "Conditions" to evaluate real-time attributes (ABAC).

Audit-First Design: Built-in logging for every authorization decision (Allow/Deny), providing a ready-made trail for SOC2 and ISO 27001 compliance.

Performance Optimized: Implements a layered caching strategy to ensure the authorization check doesn't become the bottleneck of the API.

Developer First: Clean RESTful API (DRF) designed to be consumed as a sidecar or a dedicated middleware service.

🛡️ Security Posture
Zero-Trust Ready: Encourages the principle of least privilege.

Fail-Closed Logic: The engine is designed to deny access by default if any part of the policy evaluation fails.

Immutable Logs: (Planned) Integration with append-only ledger storage for audit integrity.
