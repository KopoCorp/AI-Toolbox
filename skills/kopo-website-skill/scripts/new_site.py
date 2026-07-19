#!/usr/bin/env python3
"""
Kopo Website Scaffolder
=======================

Generates a new Kopo website by copying the skill's assets, CSS and JS
and filling in the chosen HTML template (landing | internal | legal).

Usage:
    python new_site.py --config config.json --out /path/to/output
    python new_site.py --template landing --brand "Kopo Cloud" --out ./mysite
    python new_site.py --interactive

The config.json file follows this structure (site copy stays in French):
{
    "template": "landing",                # landing | internal | legal
    "brand_name": "Kopo Cloud",
    "page_title": "Kopo Cloud · Stockage souverain",
    "meta_desc": "...",
    "contact_email": "contact@kopo.systems",
    "footer_tagline": "...",
    "year": 2026,
    "hero": { "eyebrow": "...", "title_html": "...", "sub": "...",
              "cta_primary": "...", "cta_secondary": "..." },
    "manifesto_html": "...",
    "features": [ { "icon": "shield", "title": "...", "desc": "..." }, ... ],
    "infra": { "title": "...", "lead": "...",
               "features": [ { "icon": "...", "title": "...", "desc": "..." } ] },
    "stats": [ { "num": 99.9, "unit": "%", "label": "...", "decimals": 1 } ],
    "pricing": { "title": "...",
                 "tiers": [ { "name": "...", "amount": "9", "desc": "...",
                              "featured": false, "features": [...], "muted": [...],
                              "cta": "Choisir" } ] },
    "faq": { "title": "...", "items": [ { "q": "...", "a": "..." } ] },
    "cta_band": { "title": "...", "sub": "...", "button": "..." }
}
"""

import argparse
import json
import shutil
import sys
from pathlib import Path

# Skill root = parent of this scripts/ folder
SKILL_ROOT = Path(__file__).resolve().parent.parent

# === Icônes Lucide-style (stroke 2px) ======================================
ICON_LIB = {
    "shield":   '<path d="M12 2l8 4v6c0 5-3.5 9.5-8 10-4.5-.5-8-5-8-10V6l8-4z" stroke="currentColor" stroke-width="2" stroke-linejoin="round"/>',
    "lock":     '<rect x="3" y="11" width="18" height="11" rx="2" stroke="currentColor" stroke-width="2"/><path d="M7 11V7a5 5 0 0110 0v4" stroke="currentColor" stroke-width="2"/>',
    "cloud":    '<path d="M17.5 19a4.5 4.5 0 100-9h-1.8A7 7 0 104 14.9" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>',
    "mail":     '<rect x="2" y="4" width="20" height="16" rx="2" stroke="currentColor" stroke-width="2"/><polyline points="22,6 12,13 2,6" stroke="currentColor" stroke-width="2" fill="none"/>',
    "server":   '<rect x="2" y="3" width="20" height="8" rx="1" stroke="currentColor" stroke-width="2"/><rect x="2" y="13" width="20" height="8" rx="1" stroke="currentColor" stroke-width="2"/><line x1="6" y1="7" x2="6.01" y2="7" stroke="currentColor" stroke-width="2"/><line x1="6" y1="17" x2="6.01" y2="17" stroke="currentColor" stroke-width="2"/>',
    "database": '<ellipse cx="12" cy="5" rx="9" ry="3" stroke="currentColor" stroke-width="2"/><path d="M21 12c0 1.66-4 3-9 3s-9-1.34-9-3" stroke="currentColor" stroke-width="2"/><path d="M3 5v14c0 1.66 4 3 9 3s9-1.34 9-3V5" stroke="currentColor" stroke-width="2"/>',
    "globe":    '<circle cx="12" cy="12" r="10" stroke="currentColor" stroke-width="2"/><line x1="2" y1="12" x2="22" y2="12" stroke="currentColor" stroke-width="2"/><path d="M12 2a15 15 0 010 20M12 2a15 15 0 000 20" stroke="currentColor" stroke-width="2" fill="none"/>',
    "terminal": '<polyline points="4 17 10 11 4 5" stroke="currentColor" stroke-width="2" fill="none"/><line x1="12" y1="19" x2="20" y2="19" stroke="currentColor" stroke-width="2"/>',
    "settings": '<circle cx="12" cy="12" r="3" stroke="currentColor" stroke-width="2"/><path d="M19.4 15a1.7 1.7 0 00.4 1.8l.1.1a2 2 0 11-2.8 2.8l-.1-.1a1.7 1.7 0 00-1.8-.4 1.7 1.7 0 00-1 1.5V21a2 2 0 11-4 0v-.1a1.7 1.7 0 00-1.1-1.5 1.7 1.7 0 00-1.8.4l-.1.1a2 2 0 11-2.8-2.8l.1-.1a1.7 1.7 0 00.4-1.8 1.7 1.7 0 00-1.5-1H3a2 2 0 110-4h.1a1.7 1.7 0 001.5-1.1 1.7 1.7 0 00-.4-1.8l-.1-.1a2 2 0 112.8-2.8l.1.1a1.7 1.7 0 001.8.4H9a1.7 1.7 0 001-1.5V3a2 2 0 114 0v.1a1.7 1.7 0 001 1.5 1.7 1.7 0 001.8-.4l.1-.1a2 2 0 112.8 2.8l-.1.1a1.7 1.7 0 00-.4 1.8V9a1.7 1.7 0 001.5 1H21a2 2 0 110 4h-.1a1.7 1.7 0 00-1.5 1z" stroke="currentColor" stroke-width="2" fill="none"/>',
    "users":    '<path d="M16 21v-2a4 4 0 00-4-4H6a4 4 0 00-4 4v2" stroke="currentColor" stroke-width="2" fill="none"/><circle cx="9" cy="7" r="4" stroke="currentColor" stroke-width="2"/><path d="M22 21v-2a4 4 0 00-3-3.87M16 3.13a4 4 0 010 7.75" stroke="currentColor" stroke-width="2" fill="none"/>',
    "bell":     '<path d="M18 8A6 6 0 006 8c0 7-3 9-3 9h18s-3-2-3-9" stroke="currentColor" stroke-width="2" fill="none"/><path d="M13.73 21a2 2 0 01-3.46 0" stroke="currentColor" stroke-width="2" fill="none"/>',
    "zap":      '<polygon points="13 2 3 14 12 14 11 22 21 10 12 10 13 2" stroke="currentColor" stroke-width="2" fill="none" stroke-linejoin="round"/>',
    "check":    '<polyline points="20 6 9 17 4 12" stroke="currentColor" stroke-width="2.5" fill="none" stroke-linecap="round" stroke-linejoin="round"/>',
    "minus":    '<line x1="5" y1="12" x2="19" y2="12" stroke="currentColor" stroke-width="2.5" stroke-linecap="round"/>',
    "arrow":    '<path d="M5 12h14M13 5l7 7-7 7" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>',
    "chevron":  '<polyline points="6 9 12 15 18 9" stroke="currentColor" stroke-width="2" fill="none" stroke-linecap="round" stroke-linejoin="round"/>',
}

def icon_svg(name, size=22):
    body = ICON_LIB.get(name, ICON_LIB["server"])
    return f'<svg width="{size}" height="{size}" viewBox="0 0 24 24" fill="none" aria-hidden="true">{body}</svg>'

# === Builders de blocs HTML =================================================

def build_features(features):
    html = []
    for i, f in enumerate(features, start=1):
        delay = f"delay-{min(i, 3)}"
        html.append(f"""        <article class="service-card reveal {delay}">
          <div class="icon-circle">{icon_svg(f.get('icon', 'server'))}</div>
          <div class="num">{i:02d}</div>
          <h3>{f['title']}</h3>
          <p>{f['desc']}</p>
          <a href="#cta" class="arrow-link">En savoir plus
            {icon_svg('arrow', 14)}
          </a>
        </article>""")
    return "\n".join(html)

def build_infra_features(features):
    html = []
    for i, f in enumerate(features, start=1):
        delay = f"delay-{min(i, 3)}"
        html.append(f"""        <div class="infra-feature reveal {delay}">
          <div class="icon-circle">{icon_svg(f.get('icon', 'server'), 20)}</div>
          <h3>{f['title']}</h3>
          <p>{f['desc']}</p>
        </div>""")
    return "\n".join(html)

def build_stats(stats):
    html = []
    for i, s in enumerate(stats, start=1):
        delay = f"delay-{min(i, 3)}"
        decimals = s.get('decimals', 0)
        html.append(f"""        <div class="stat-block reveal {delay}">
          <div class="stat-value"><span data-count="{s['num']}" data-decimals="{decimals}">0</span><span class="unit">{s.get('unit', '')}</span></div>
          <div class="stat-label">{s['label']}</div>
        </div>""")
    return "\n".join(html)

def build_pricing(tiers):
    html = []
    for i, t in enumerate(tiers, start=1):
        delay = f"delay-{min(i, 3)}"
        featured = " featured" if t.get('featured') else ""
        btn_class = "btn-primary" if t.get('featured') else "btn-outline"
        feats = []
        for f in t.get('features', []):
            feats.append(f'    <li>{icon_svg("check", 16)} {f}</li>')
        for f in t.get('muted', []):
            feats.append(f'    <li class="muted">{icon_svg("minus", 16)} {f}</li>')
        feats_html = "\n".join(feats)
        amount_str = t['amount']
        period = t.get('period', ' / mois')
        amount_block = f'<div class="price-amount">{amount_str}<span class="currency">€</span><span class="period">{period}</span></div>'
        if amount_str == '0' or amount_str.lower() == 'gratuit':
            amount_block = f'<div class="price-amount">Gratuit</div>'
        html.append(f"""        <div class="price-card{featured} reveal {delay}">
          <span class="price-tier">{t['name']}</span>
          {amount_block}
          <p class="price-desc">{t['desc']}</p>
          <ul class="price-features">
{feats_html}
          </ul>
          <a href="#cta" class="btn {btn_class}">{t.get('cta', 'Choisir')}</a>
        </div>""")
    return "\n".join(html)

def build_faq(items):
    html = []
    for it in items:
        html.append(f"""        <details class="faq-item reveal">
          <summary class="faq-question">
            {it['q']}
            <svg class="chev" viewBox="0 0 24 24" fill="none">{ICON_LIB['chevron']}</svg>
          </summary>
          <div class="faq-answer">{it['a']}</div>
        </details>""")
    return "\n".join(html)

# === Render principal =======================================================

def render_landing(cfg):
    tpl = (SKILL_ROOT / "templates/landing/index.html").read_text(encoding="utf-8")
    hero = cfg.get('hero', {})
    infra = cfg.get('infra', {})
    pricing = cfg.get('pricing', {})
    faq = cfg.get('faq', {})
    cta_band = cfg.get('cta_band', {})

    out = tpl
    subs = {
        "{{PAGE_TITLE}}":        cfg.get('page_title', cfg.get('brand_name', 'Kopo')),
        "{{META_DESC}}":         cfg.get('meta_desc', ''),
        "{{BRAND_NAME}}":        cfg.get('brand_name', 'Kopo'),
        "{{NAV_CTA}}":           cfg.get('nav_cta', 'Nous contacter'),
        "{{HERO_EYEBROW}}":      hero.get('eyebrow', 'Infrastructure souveraine · Brest, France'),
        "{{HERO_TITLE_HTML}}":   hero.get('title_html', 'Un service Kopo.'),
        "{{HERO_SUB}}":          hero.get('sub', ''),
        "{{HERO_CTA_PRIMARY}}":  hero.get('cta_primary', 'Commencer'),
        "{{HERO_CTA_SECONDARY}}":hero.get('cta_secondary', 'En savoir plus'),
        "{{MANIFESTO_HTML}}":    cfg.get('manifesto_html', ''),
        "{{FEATURES_TITLE}}":    cfg.get('features_title', 'Tout ce dont vous avez besoin.'),
        "{{FEATURES_CARDS}}":    build_features(cfg.get('features', [])),
        "{{INFRA_TITLE}}":       infra.get('title', 'Conçue et opérée en interne.'),
        "{{INFRA_LEAD}}":        infra.get('lead', ''),
        "{{INFRA_FEATURES}}":    build_infra_features(infra.get('features', [])),
        "{{STATS_BLOCKS}}":      build_stats(cfg.get('stats', [])),
        "{{PRICING_TITLE}}":     pricing.get('title', 'Choisissez votre formule.'),
        "{{PRICING_CARDS}}":     build_pricing(pricing.get('tiers', [])),
        "{{FAQ_TITLE}}":         faq.get('title', 'Questions fréquentes.'),
        "{{FAQ_ITEMS}}":         build_faq(faq.get('items', [])),
        "{{CTA_TITLE}}":         cta_band.get('title', 'Prêt à commencer ?'),
        "{{CTA_SUB}}":           cta_band.get('sub', ''),
        "{{CTA_BUTTON}}":        cta_band.get('button', 'Nous contacter'),
        "{{CONTACT_EMAIL}}":     cfg.get('contact_email', 'contact@kopo.systems'),
        "{{FOOTER_TAGLINE}}":    cfg.get('footer_tagline', ''),
        "{{YEAR}}":              str(cfg.get('year', 2026)),
    }
    for k, v in subs.items():
        out = out.replace(k, str(v))
    return out

def render_internal(cfg):
    tpl = (SKILL_ROOT / "templates/internal/index.html").read_text(encoding="utf-8")
    out = tpl
    # Build nav links
    nav_items = cfg.get('nav_links', [])
    nav_html = "\n".join(
        f'<li><a href="{n["href"]}"{" class=\"active\"" if n.get("active") else ""}>{n["label"]}</a></li>'
        for n in nav_items
    )
    nav_mobile_html = "\n".join(
        f'<li><a href="{n["href"]}">{n["label"]}</a></li>' for n in nav_items
    )
    # Breadcrumb
    bc = cfg.get('breadcrumb', [])
    bc_html = ""
    if bc:
        parts = []
        for i, item in enumerate(bc):
            is_last = (i == len(bc) - 1)
            if is_last:
                parts.append(f'<span class="current">{item["label"]}</span>')
            else:
                href = item.get("href", "#")
                parts.append(f'<a href="{href}">{item["label"]}</a>')
                parts.append('<span class="sep">/</span>')
        bc_html = "".join(parts)
    # Content sections
    sections_html = []
    for s in cfg.get('sections', []):
        alt = ' class="section-alt"' if s.get('alt') else ''
        sec_id = s.get('id', '')
        sections_html.append(f"""<section id="{sec_id}"{alt}>
  <div class="container" style="padding: 4rem 0;">
    <span class="section-eyebrow">{s.get('label', '')}</span>
    <h2 style="font-size:1.75rem; font-weight:700; letter-spacing:-0.02em;">{s.get('title', '')}</h2>
    <div class="cirrus-bar"></div>
    {s.get('body_html', '')}
  </div>
</section>""")
    sections_full = "\n".join(sections_html)
    # Footer columns
    fc_html = ""
    for col in cfg.get('footer_columns', []):
        links_html = "\n".join(f'<li><a href="{l["href"]}">{l["label"]}</a></li>' for l in col.get('links', []))
        fc_html += f"<div><h4>{col['heading']}</h4><ul>{links_html}</ul></div>\n"

    subs = {
        "{{PAGE_TITLE}}":     cfg.get('page_title', 'Kopo'),
        "{{META_DESC}}":      cfg.get('meta_desc', ''),
        "{{BRAND_NAME}}":     cfg.get('brand_name', 'Kopo'),
        "{{NAV_LINKS}}":      nav_html,
        "{{NAV_LINKS_MOBILE}}": nav_mobile_html,
        "{{NAV_CTA}}":        cfg.get('nav_cta', 'Contact'),
        "{{NAV_CTA_HREF}}":   cfg.get('nav_cta_href', '#'),
        "{{BREADCRUMB}}":     bc_html,
        "{{HERO_TITLE}}":     cfg.get('hero_title', ''),
        "{{HERO_SUB}}":       cfg.get('hero_sub', ''),
        "{{CONTENT_SECTIONS}}": sections_full,
        "{{FOOTER_TAGLINE}}": cfg.get('footer_tagline', ''),
        "{{FOOTER_COLUMNS}}": fc_html,
        "{{YEAR}}":           str(cfg.get('year', 2026)),
    }
    for k, v in subs.items():
        out = out.replace(k, str(v))
    return out

def render_app(cfg):
    tpl = (SKILL_ROOT / "templates/app/index.html").read_text(encoding="utf-8")
    out = tpl
    # Nav
    nav_items = cfg.get('nav_links', [])
    nav_html = "\n".join(
        f'<li><a href="{n["href"]}"{" class=\"active\"" if n.get("active") else ""}>{n["label"]}</a></li>'
        for n in nav_items
    )
    nav_mobile_html = "\n".join(
        f'<li><a href="{n["href"]}">{n["label"]}</a></li>' for n in nav_items
    )
    # Hero block (OPTIONNEL — par défaut pas de hero, le page-title-row suffit
    # pour une page d'app interne sobre)
    hero_block = ""
    if cfg.get('hero'):
        h = cfg['hero']
        hero_block = f"""<section class="kopo-hero-halo" style="margin: -2.5rem calc(-1 * var(--container-px)) 2rem; padding-left: var(--container-px); padding-right: var(--container-px);">
  <h1>{h.get('title', '')}</h1>
  <div class="cirrus-bar"></div>
  <p class="lead">{h.get('sub', '')}</p>
</section>"""
    # Page subtitle (sous le h1 du page-title-row, optionnel)
    subtitle_html = ""
    if cfg.get('page_subtitle'):
        subtitle_html = f'<p style="margin-top:0.75rem; color:var(--nimbus-soft); max-width:60ch; font-size:0.95rem;">{cfg["page_subtitle"]}</p>'
    # Toolbar actions
    ta_html = ""
    for a in cfg.get('toolbar_actions', []):
        cls = "btn-primary" if a.get('primary') else "btn-outline"
        ta_html += f'<a href="{a.get("href", "#")}" class="btn {cls}">{a["label"]}</a>\n'
    # KPI block
    kpi_block = ""
    kpis = cfg.get('kpis', [])
    if kpis:
        cards = []
        for k in kpis:
            delta_html = ""
            if 'delta' in k:
                d = k['delta']
                cls = d.get('dir', 'flat')
                arrow = '↑' if cls == 'up' else ('↓' if cls == 'down' else '→')
                delta_html = f'<div class="kpi-delta {cls}">{arrow} {d["text"]}</div>'
            cards.append(f"""  <div class="kpi-card">
    <div class="kpi-label">{k['label']}</div>
    <div class="kpi-value">{k['value']}<span class="unit">{k.get('unit', '')}</span></div>
    {delta_html}
  </div>""")
        kpi_block = '<div class="kpi-grid" style="margin-bottom: 2rem;">\n' + "\n".join(cards) + "\n</div>"
    # Filter block
    filter_block = ""
    if cfg.get('filters'):
        items = []
        for f in cfg['filters']:
            if f['type'] == 'select':
                opts = "\n".join(f'<option value="{o.get("value", o["label"])}">{o["label"]}</option>' for o in f['options'])
                items.append(f'<div><label for="{f["id"]}">{f["label"]}</label><select id="{f["id"]}">{opts}</select></div>')
            else:
                placeholder = f.get('placeholder', '')
                items.append(f'<div><label for="{f["id"]}">{f["label"]}</label><input id="{f["id"]}" type="{f["type"]}" placeholder="{placeholder}" /></div>')
        filter_block = '<div class="filter-bar" style="margin-bottom: 1.5rem;">\n' + "\n".join(items) + "\n</div>"
    # Main content : pass through as raw HTML so caller has full control
    main_content = cfg.get('main_content_html', '')

    subs = {
        "{{PAGE_TITLE}}":     cfg.get('page_title', 'Kopo App'),
        "{{META_DESC}}":      cfg.get('meta_desc', ''),
        "{{APP_NAME}}":       cfg.get('app_name', 'Kopo'),
        "{{NAV_LINKS}}":      nav_html,
        "{{NAV_LINKS_MOBILE}}": nav_mobile_html,
        "{{NAV_CTA}}":        cfg.get('nav_cta', 'Compte'),
        "{{NAV_CTA_HREF}}":   cfg.get('nav_cta_href', '#'),
        "{{USER_LABEL}}":     cfg.get('user_label', 'Service interne'),
        "{{HERO_BLOCK}}":     hero_block,
        "{{PAGE_HEADING}}":   cfg.get('page_heading', ''),
        "{{PAGE_SUBTITLE}}":  subtitle_html,
        "{{TOOLBAR_ACTIONS}}": ta_html,
        "{{KPI_BLOCK}}":      kpi_block,
        "{{FILTER_BLOCK}}":   filter_block,
        "{{MAIN_CONTENT}}":   main_content,
        "{{YEAR}}":           str(cfg.get('year', 2026)),
    }
    for k, v in subs.items():
        out = out.replace(k, str(v))
    return out

def render_legal(cfg):
    tpl = (SKILL_ROOT / "templates/legal/index.html").read_text(encoding="utf-8")
    out = tpl
    subs = {
        "{{PAGE_TITLE}}":     cfg.get('page_title', 'Mentions légales · Kopo'),
        "{{META_DESC}}":      cfg.get('meta_desc', ''),
        "{{BRAND_NAME}}":     cfg.get('brand_name', 'Kopo'),
        "{{LEGAL_TITLE}}":    cfg.get('legal_title', 'Mentions légales'),
        "{{LEGAL_META}}":     cfg.get('legal_meta', ''),
        "{{LEGAL_BODY}}":     cfg.get('legal_body', ''),
        "{{FOOTER_TAGLINE}}": cfg.get('footer_tagline', ''),
        "{{YEAR}}":           str(cfg.get('year', 2026)),
    }
    for k, v in subs.items():
        out = out.replace(k, str(v))
    return out

# === Scaffolding du dossier ================================================

def copy_assets(out_dir: Path):
    """Copy CSS, JS, assets, logos, illustrations, fonts into the output."""
    for sub in ("css", "js"):
        dest = out_dir / sub
        dest.mkdir(parents=True, exist_ok=True)
        for f in (SKILL_ROOT / sub).iterdir():
            shutil.copy2(f, dest / f.name)
    # assets/
    for sub in ("assets/logos", "assets/illustrations", "assets/fonts"):
        dest = out_dir / sub
        dest.mkdir(parents=True, exist_ok=True)
        src = SKILL_ROOT / sub
        if src.exists():
            for f in src.iterdir():
                shutil.copy2(f, dest / f.name)

def scaffold(cfg, out_dir: Path):
    out_dir.mkdir(parents=True, exist_ok=True)
    copy_assets(out_dir)
    template = cfg.get('template', 'landing')
    if template == 'landing':
        html = render_landing(cfg)
        (out_dir / "index.html").write_text(html, encoding="utf-8")
    elif template == 'internal':
        html = render_internal(cfg)
        (out_dir / cfg.get('filename', 'index.html')).write_text(html, encoding="utf-8")
    elif template == 'app':
        html = render_app(cfg)
        (out_dir / cfg.get('filename', 'index.html')).write_text(html, encoding="utf-8")
    elif template == 'legal':
        html = render_legal(cfg)
        fname = cfg.get('filename', 'mentions.html')
        (out_dir / fname).write_text(html, encoding="utf-8")
    else:
        raise SystemExit(f"Unknown template: {template}")
    return out_dir

def main():
    ap = argparse.ArgumentParser(description="Kopo Website Scaffolder")
    ap.add_argument("--config", help="Path to JSON config file")
    ap.add_argument("--out", required=True, help="Output directory")
    args = ap.parse_args()
    if not args.config:
        ap.error("--config is required")
    cfg = json.loads(Path(args.config).read_text(encoding="utf-8"))
    out = scaffold(cfg, Path(args.out))
    print(f"OK · Site Kopo généré dans {out.resolve()}")

if __name__ == "__main__":
    main()
