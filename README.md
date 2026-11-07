# AgentFlow AI Backup public information site

Standalone static HTML/CSS. No build command, backend, JavaScript dependencies or authorization endpoint. Deploy only this directory using Vercel?s Other framework. Deployment is operator-controlled.

## Routes

`vercel.json` enables clean URLs: `/` serves index.html, `/privacy` serves privacy.html and `/terms` serves terms.html. The homepage and footer link to `/privacy`. Set the OAuth consent privacy URL to the exact deployed canonical URL, including consistent slash handling. Do not change consent settings as part of this source update.

## Publication blockers

The source deliberately discloses unresolved operator identity/contact information rather than fabricating an email. Supply a verified operator name and reachable public contact email on all pages before resubmission. Approve retention periods for archives, tokens, manifests and logs. Confirm the actual remote grant is exactly drive.file without exposing credentials. The adapter consumes an existing remote and does not enforce scope. Confirm domain ownership and eligibility for Google verification; the current vercel.app address alone is not evidence of ownership verification.

## Local validation

Run `python check_site.py`. Review desktop and mobile rendering in a browser before deployment. Review the entire public directory for secrets; never add credentials, private keys or backup artifacts. After deploying, check the three URLs in VERIFICATION.md without authentication. Google makes the verification decision.
