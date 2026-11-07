# OAuth website review evidence ? November 7, 2026

## Evidence and factual boundaries

Reviewed the separate private repository read-only: ops/backup/backup.py, rclone_offhost.py, schedule.py, V2_ENCRYPTED_BACKUP_RUNBOOK.md and the sanitized November 2 synthetic recovery evidence. No private config or credential contents were opened. Backup encryption, local decrypt verification, manifest checks, immutable exact-file upload, readback and synthetic restore are implemented/tested. Vault custody, dual control, approved retention and unattended production operation are not established. Current local verification requires a private identity, so a public-only worker claim was removed.

The intended drive.file scope is documented, not independently confirmed against the live remote or OAuth grant. An existing folder path does not prove accessibility under drive.file. Verify this privately before submission; never paste tokens into evidence.

## Google checklist

- Content: identity/purpose, data access/use/storage/sharing, exact intended scope, tokens, encryption, recovery, metadata/logs, retention, deletion, choices/revocation and applicable Limited Use requirements are addressed.
- Navigation: home and footer link to /privacy on the same host; terms and branding are consistent.
- Public access: existing deployed /privacy returned HTTP 200 without login. Updated source has not been deployed. Recheck all pages after deployment.
- Consent URL match: pending operator inspection; no Cloud settings were accessed.
- Domain ownership verification: pending operator evidence.
- Public legal operator identity and contact email: unresolved. No invented address or bracketed placeholders remain. Explicit review notices prevent treating this edition as submission-ready.
- Retention: recommendations are distinguished from active commitments; operator approval needed for actual durations.
- Layout: dark design and responsive grid preserved; long scope URLs wrap. Browser access host was unavailable, so rendered desktop/mobile QA remains pending. Static CSS checks alone do not establish visual quality.
- No deployment, push or Google submission performed. Private application unchanged by this task.

## Sources reviewed

- https://support.google.com/cloud/answer/13464321
- https://developers.google.com/identity/verification/authentication-policy-compliance
- https://developers.google.com/workspace/drive/api/guides/api-specific-auth
- https://developers.google.com/terms/api-services-user-data-policy
- https://rclone.org/drive/#scopes

## Operator verification after deployment

- https://agentflow-oauth-site.vercel.app/
- https://agentflow-oauth-site.vercel.app/privacy
- https://agentflow-oauth-site.vercel.app/terms

Check unauthenticated access, status 200, actual new text, navigation, desktop and 375px mobile layouts, no horizontal overflow, and exactly matching OAuth consent privacy URL. Replace these URLs consistently if adopting an owned custom domain. Verify contact email reachability. Then decide whether to resubmit; Google approval is not guaranteed.

## Local check results

Dependency-free static check passed for all 3 pages, every internal link and fragment, metadata, 20 policy sections, Vercel clean URL configuration and responsive CSS rules. Gitleaks v8.24.3 directory scan: no leaks found (28.15 KB scanned). Staged whitespace check passed. Rendered layout and updated deployed routes remain operator checks.
