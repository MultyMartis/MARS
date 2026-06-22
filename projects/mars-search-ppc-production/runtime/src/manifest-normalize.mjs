import { STAGE_ORDER } from './constants.mjs';

function emptyStageEntry(stageId) {
  return {
    stage_id: stageId,
    status: 'NOT STARTED',
    started_at: null,
    completed_at: null,
    approved_at: null,
    owner: null,
    required_artifacts: [],
    registered_artifacts: [],
    validator_result: null,
    blockers: [],
    operator_approval: { approved: false },
    degradation_approval: { approved: false },
    evidence_version: null,
  };
}

export function normalizeManifest(raw) {
  const m = { ...raw };

  m.schema_version = m.schema_version || '1.0.0';
  m.lifecycle_version = m.lifecycle_version || '1.0.0';
  m.organization_id = m.organization_id || m.organization || '';
  m.project_name = m.project_name || m.project_id || '';
  m.platform = m.platform || m.campaign_platform || 'Yandex Direct';
  m.timezone = m.timezone || 'UTC';
  m.lifecycle_status = m.lifecycle_status || (m.lifecycle_status === 'FROZEN' ? 'FROZEN' : 'ACTIVE');
  m.risk_mode = m.risk_mode || 'STANDARD';
  m.project_mode = m.project_mode || 'PRODUCTION';

  if (!m.stage_registry && m.stage_statuses) {
    m.stage_registry = {};
    for (const stageId of STAGE_ORDER) {
      const legacy = m.stage_statuses[stageId] || { status: 'NOT STARTED' };
      m.stage_registry[stageId] = {
        ...emptyStageEntry(stageId),
        status: legacy.status || 'NOT STARTED',
        started_at: legacy.started_at || legacy.updated_at || null,
        completed_at: legacy.completed_at || null,
        approved_at: legacy.approved_at || null,
        evidence_version: legacy.evidence_version || null,
        registered_artifacts: legacy.evidence_refs || [],
      };
    }
  }

  if (!m.artifact_registry && m.artifacts) {
    m.artifact_registry = { ...m.artifacts };
  }

  if (!m.approval_registry && m.operator_approvals) {
    m.approval_registry = { ...m.operator_approvals };
  }

  if (!m.degraded_mode_registry && m.degraded_evidence_approvals) {
    m.degraded_mode_registry = { ...m.degraded_evidence_approvals };
  }

  if (!m.blocker_registry && m.blockers) {
    m.blocker_registry = Array.isArray(m.blockers)
      ? m.blockers.map((b, i) => (typeof b === 'string' ? { id: `BLK-${i + 1}`, message: b } : b))
      : [];
  }

  if (!m.runtime_registry && m.runtime_versions) {
    m.runtime_registry = { ...m.runtime_versions };
  }

  m.current_lifecycle_stage = m.current_lifecycle_stage || m.current_stage || 'SPPC-01';
  m.next_allowed_actions = m.next_allowed_actions || [];
  m.forbidden_actions = m.forbidden_actions || [];

  return m;
}

export function getStageStatus(manifest, stageId) {
  const reg = manifest.stage_registry?.[stageId] || manifest.stage_statuses?.[stageId];
  return reg?.status || 'NOT STARTED';
}

export function getArtifact(manifest, artifactType) {
  return manifest.artifact_registry?.[artifactType] || manifest.artifacts?.[artifactType] || null;
}

export function completedStages(manifest) {
  const out = [];
  for (const stageId of STAGE_ORDER) {
    const st = getStageStatus(manifest, stageId);
    if (st === 'COMPLETED' || st === 'COMPLETED WITH APPROVED DEGRADATION') {
      out.push(stageId);
    }
  }
  return out;
}
