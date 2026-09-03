"""Closed catalog of iSEO Sales PG operations for Operational.v3.dev / agents."""

from __future__ import annotations

import json
from typing import Any, Mapping, Sequence

ALLOWED_OPS: tuple[str, ...] = (
    "register_inbound_event",
    "upsert_lead",
    "append_lead_event",
    "change_lead_status",
    "enqueue_delivery",
    "enqueue_job",
    "get_lead",
    "list_pending_leads",
    "claim_jobs",
    "mark_inbound_processed",
    "record_error",
    "get_active_config",
    "list_delivery_recipients",
    "claim_pending_deliveries",
    "mark_delivery_result",
    "process_gmail_inbound_commit",
)


class IseoSalesOps:
    """Parameterised wrappers around app_iseo_sales.* functions.

    `executor` must implement:
      call_json(sql: str, params: Sequence[Any] | None = None) -> Any
    returning decoded JSON (dict/list/scalar). Never expose a free-form SQL API.
    """

    def __init__(self, executor: Any):
        self._ex = executor

    def allowed_ops(self) -> tuple[str, ...]:
        return ALLOWED_OPS

    def _call(self, fn_sql: str, params: Sequence[Any] | None = None) -> Any:
        return self._ex.call_json(fn_sql, params)

    def process_gmail_inbound_commit(self, **kwargs: Any) -> dict:
        """Atomic commit point: inbound + lead + event + delivery intents."""
        keys = (
            "source_id",
            "lead_id",
            "payload",
            "raw_text",
            "correlation_id",
            "gmail_thread_id",
            "received_at",
            "subject",
            "from_email",
            "normalized_hash",
            "parser_version",
            "workflow_version",
            "client_name",
            "primary_contact",
            "contact_type",
            "phone",
            "email",
            "messenger",
            "site",
            "service",
            "summary",
            "source",
            "manager_status",
            "form_metadata",
            "data_contract_version",
            "enqueue_telegram",
            "card_payload",
            "event_type",
        )
        args = [kwargs.get(k) for k in keys]
        # jsonb fields
        for i, k in enumerate(keys):
            if k in ("payload", "form_metadata", "card_payload") and args[i] is not None:
                if not isinstance(args[i], str):
                    args[i] = json.dumps(args[i])
        sql = """
        SELECT app_iseo_sales.process_gmail_inbound_commit(
          %s,%s,%s::jsonb,%s,%s,%s,%s::timestamptz,%s,%s,%s,%s,%s,
          %s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s::jsonb,%s,%s,%s::jsonb,%s
        )
        """
        return self._call(sql, args)

    def mark_inbound_processed(
        self,
        source_id: str,
        status: str = "processed",
        lead_id: str | None = None,
        source_system: str = "gmail",
        error_message: str | None = None,
    ) -> dict:
        return self._call(
            "SELECT app_iseo_sales.mark_inbound_processed(%s,%s,%s,%s,%s)",
            (source_system, source_id, status, lead_id, error_message),
        )

    def record_error(self, **kwargs: Any) -> dict:
        ctx = kwargs.get("context_sanitized") or {}
        if not isinstance(ctx, str):
            ctx = json.dumps(ctx)
        return self._call(
            """
            SELECT app_iseo_sales.record_error(
              %s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s::jsonb
            )
            """,
            (
                kwargs.get("app_component", "operational"),
                kwargs.get("workflow_version"),
                kwargs.get("n8n_execution_id"),
                kwargs.get("correlation_id"),
                kwargs.get("entity_type"),
                kwargs.get("entity_id"),
                kwargs.get("error_class"),
                kwargs.get("provider"),
                kwargs.get("code"),
                kwargs.get("http_status"),
                kwargs.get("stage"),
                kwargs.get("retryable", False),
                kwargs.get("message_sanitized"),
                ctx,
            ),
        )

    def get_active_config(self, keys: Sequence[str] | None = None) -> dict:
        return self._call(
            "SELECT app_iseo_sales.get_active_config(%s::text[])",
            (list(keys) if keys else None,),
        )

    def list_delivery_recipients(self, delivery_type: str = "lead_card") -> dict:
        return self._call(
            "SELECT app_iseo_sales.list_delivery_recipients(%s)",
            (delivery_type,),
        )

    def claim_pending_deliveries(
        self, worker_id: str, limit: int = 10, lease_seconds: int = 120
    ) -> dict:
        return self._call(
            "SELECT app_iseo_sales.claim_pending_deliveries(%s,%s,%s)",
            (worker_id, limit, lease_seconds),
        )

    def mark_delivery_result(
        self,
        delivery_id: str,
        status: str,
        external_message_id: str | None = None,
        telegram_chat_id: str | None = None,
        error_id: int | None = None,
        retry_after_seconds: int | None = None,
    ) -> dict:
        return self._call(
            "SELECT app_iseo_sales.mark_delivery_result(%s,%s,%s,%s,%s,%s)",
            (
                delivery_id,
                status,
                external_message_id,
                telegram_chat_id,
                error_id,
                retry_after_seconds,
            ),
        )

    def change_lead_status(
        self,
        lead_id: str,
        expected_version: int,
        from_status: str,
        to_status: str,
        actor_type: str = "workflow",
        actor_id: str | None = None,
        idempotency_key: str | None = None,
        correlation_id: str | None = None,
        close_reason: str | None = None,
        notes: str | None = None,
    ) -> dict:
        return self._call(
            "SELECT app_iseo_sales.change_lead_status(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",
            (
                lead_id,
                expected_version,
                from_status,
                to_status,
                actor_type,
                actor_id,
                idempotency_key,
                correlation_id,
                close_reason,
                notes,
            ),
        )

    def get_lead(self, lead_id: str) -> dict:
        return self._call("SELECT app_iseo_sales.get_lead(%s)", (lead_id,))

    def enqueue_job(
        self,
        job_type: str,
        payload: Mapping[str, Any] | None = None,
        *,
        priority: int = 100,
        available_at: str | None = None,
        dedupe_key: str | None = None,
        correlation_id: str | None = None,
        lead_id: str | None = None,
    ) -> dict:
        pl = json.dumps(payload or {})
        return self._call(
            """
            SELECT app_iseo_sales.enqueue_job(
              %s, %s::jsonb, %s, %s::timestamptz, %s, %s, %s
            )
            """,
            (
                job_type,
                pl,
                priority,
                available_at,
                dedupe_key,
                correlation_id,
                lead_id,
            ),
        )
