/**
 * Thin re-export shim so D6D producer imports stay stable.
 */
export {
  evaluateDeliveryEligibility,
  isStaleAge,
  runBoundedActivationLifecycle,
  validateLifecycleCharter,
  D6C_ALLOWED_WORKFLOW_ID,
  D6C_EXPECTED_VERSION_ID,
  STALE_AFTER_SECONDS,
  LIFECYCLE_STATES,
  DELIVERY_ELIGIBILITY,
} from './client-ops-activation-lifecycle.mjs';
