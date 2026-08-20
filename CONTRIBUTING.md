# NIDDE — CONTRIBUTING GUIDE
Project: NIDDE  
Phase: 00 — ARCHITECTURE  
Status: ACTIVE  
Implementation: CONTROLLED  
Authority: AG-01 → AG-13

## 1. Purpose
Defines how all contributors must interact with the NIDDE repository.  
All work must preserve AG-07 Security and the boundaries in `NIDDE_MASTER_FILE_MANIFEST.md`.

## 2. Core Rules
1.  **Architecture First**: No code implementation until AG-03 → AG-13 are marked `VERIFIED`.
2.  **Single Source of Truth**: Only 1 canonical file per AG gate. Mark superseded files as `STATUS: SUPERSEDED`.
3.  **Repository Boundaries**: Respect folders: `backend/`, `database/`, `shared/`, `android/`, `admin/`, `tests/`, `docs/`, `infrastructure/`, `.github/`
4.  **No Orphan Files**: Every file must have a defined owner, boundary, and purpose.

## 3. Security Rules — AG-07
Strictly FORBIDDEN to commit:
- `passwords`, `API keys`, `JWT secrets`, `private keys`, `certificates`
- Real environment files: `.env`, `.env.local`, `.env.production`
- `payment secrets`, `webhook secrets`, `KYC documents`, `DB dumps`
- Any production credentials or sensitive personal data

Use `.env.example` with placeholders only.

## 4. Change Control Process
Any change affecting auth, roles, payment, KYC, API, DB, or CI/CD must:
1.  Identify affected AG gate(s)
2.  Update the canonical AG document
3.  Update `NIDDE_MASTER_FILE_MANIFEST.md` if file list changes
4.  Pass cross-gate consistency check before merge

## 5. Commit Checklist
Before committing, verify:
- [ ] No secrets or credentials included
- [ ] No real .env file included  
- [ ] Change follows the approved architecture
- [ ] No boundary violation between backend/android/database
- [ ] Documentation updated if needed

## 6. Verification
All merges to main must pass architecture verification.  
Conflicts are resolved using the Source-of-Truth Order in `NIDDE_MASTER_FILE_MANIFEST.md`.

## 7. Contact
For architecture or security questions, refer to `AG-07` and `NIDDE_PROJECT_CONTROL.md`.

---
NIDDE — Architecture First. Server Authority. Controlled Implementation.
