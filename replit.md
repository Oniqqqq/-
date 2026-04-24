# Workspace

## Overview

pnpm workspace monorepo using TypeScript. Each package manages its own dependencies.

## Stack

- **Monorepo tool**: pnpm workspaces
- **Node.js version**: 24
- **Package manager**: pnpm
- **TypeScript version**: 5.9
- **API framework**: Express 5
- **Database**: PostgreSQL + Drizzle ORM
- **Validation**: Zod (`zod/v4`), `drizzle-zod`
- **API codegen**: Orval (from OpenAPI spec)
- **Build**: esbuild (CJS bundle)

## Key Commands

- `pnpm run typecheck` — full typecheck across all packages
- `pnpm run build` — typecheck + build all packages
- `pnpm --filter @workspace/api-spec run codegen` — regenerate API hooks and Zod schemas from OpenAPI spec
- `pnpm --filter @workspace/db run push` — push DB schema changes (dev only)
- `pnpm --filter @workspace/api-server run dev` — run API server locally

## Artifacts

- **myhealthprac** (`artifacts/myhealthprac`) — Local 1:1 static copy of https://www.myhealthprac.com/. Files extracted from the user-provided archive into `static/` and served by a tiny Express static server (`server.mjs`). All third-party assets (Webflow CSS/JS, GSAP, Lenis, Swiper, Three.js, Vanta, images) are bundled locally so the site runs offline.
  - The server returns 404 for missing files (no SPA fallback), so missing JS chunks don't get an HTML body that breaks the parser.
  - 13 dynamic `webflow.achunk.<hash>.js` files were re-fetched from `cdn.prod.website-files.com` (they weren't in the archive) so the Webflow runtime fully loads locally.
  - Remaining browser console errors come from third-party tracking SDKs (Facebook Pixel, GTM) calling live endpoints — they don't affect the visual rendering.
  - jQuery is injected synchronously near the top of `<head>` so OwlCarousel (which is async-loaded earlier in the document than jQuery in the snapshot) doesn't crash with `$.fn` undefined.
  - The page snapshot tool HTML-encoded characters inside `<script>` tags (`=&gt;`, `&amp;&amp;`, `&lt;`, `&gt;`). Browsers don't decode entities inside `<script>` content, so all inline scroll/animation scripts (Lenis init, GSAP letters-slide-up, ScrollTrigger setup, circle rotation) silently failed with syntax errors. Decoded these entities directly in `static/index.html` so animations work. If the static folder is ever re-extracted from the ZIP, run the same decode step again.

See the `pnpm-workspace` skill for workspace structure, TypeScript setup, and package details.
