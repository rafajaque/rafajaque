"""Generate self-contained SVG banners. Python standard library only."""
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
THEMES = {
    'dark': ('#071426', '#102B4D', '#ECF6FF', '#B3CDE5', '#67D9FA', '#214669'),
    'light': ('#EDF6FF', '#D7EAFE', '#102C4F', '#365B7D', '#006D91', '#B6D4EE'),
}

for theme, (bg, panel, text, muted, accent, line) in THEMES.items():
    svg = f'''<svg xmlns="http://www.w3.org/2000/svg" width="1120" height="350" viewBox="0 0 1120 350" role="img" aria-labelledby="title desc">
<title id="title">Rafael Jaque · Programador Analista</title>
<desc id="desc">Android, datos y sistemas. San Fernando, Chile. Encabezado azul con una terminal de código decorativa.</desc>
<defs>
  <linearGradient id="bg"><stop stop-color="{bg}"/><stop offset="1" stop-color="{panel}"/></linearGradient>
  <pattern id="grid" width="28" height="28" patternUnits="userSpaceOnUse"><path d="M28 0H0V28" fill="none" stroke="{line}" stroke-width=".6" opacity=".3"/></pattern>
  <clipPath id="frame"><rect width="1120" height="350" rx="22"/></clipPath>
</defs>
<style>
  .cursor {{animation: blink 1.6s steps(1) infinite}}
  @keyframes blink {{50%{{opacity:0}}}}
  @media (prefers-reduced-motion:reduce) {{.cursor{{animation:none}}}}
</style>
<g clip-path="url(#frame)">
  <rect width="1120" height="350" fill="url(#bg)"/>
  <rect width="1120" height="350" fill="url(#grid)"/>
  <circle cx="1095" cy="20" r="220" fill="none" stroke="{line}"/>
  <circle cx="1095" cy="20" r="260" fill="none" stroke="{line}" opacity=".45"/>
  <rect x="0" y="0" width="6" height="350" fill="{accent}"/>
  <g font-family="Segoe UI,Arial,sans-serif">
    <text x="48" y="57" font-size="13" letter-spacing="3" fill="{accent}">SOFTWARE / DATOS / PERSONAS</text>
    <text x="45" y="126" font-size="58" font-weight="700" letter-spacing="-2" fill="{text}">Rafael Jaque<tspan fill="{accent}">.</tspan></text>
    <text x="48" y="169" font-size="25" fill="{muted}">Programador Analista</text>
    <text x="48" y="212" font-size="17" fill="{muted}">Aplicaciones útiles. Sistemas que conectan.</text>
    <g fill="none" stroke="{line}"><rect x="48" y="238" width="103" height="33" rx="16"/><rect x="162" y="238" width="87" height="33" rx="16"/><rect x="260" y="238" width="109" height="33" rx="16"/></g>
    <g font-size="13" fill="{accent}" text-anchor="middle"><text x="99" y="260">ANDROID</text><text x="205" y="260">DATOS</text><text x="314" y="260">SISTEMAS</text></g>
    <text x="48" y="316" font-size="13" fill="{muted}">SAN FERNANDO, CHILE <tspan dx="14" fill="{accent}">↗ @rafajaque</tspan></text>
  </g>
  <rect x="663" y="62" width="409" height="239" rx="13" fill="{bg}" stroke="{line}"/>
  <path d="M663 100H1072" stroke="{line}"/>
  <g fill="{accent}"><circle cx="684" cy="81" r="4"/><circle cx="700" cy="81" r="4" opacity=".6"/><circle cx="716" cy="81" r="4" opacity=".3"/></g>
  <g font-family="Consolas,monospace" font-size="14">
    <text x="738" y="86" fill="{muted}">perfil.yaml</text>
    <text x="687" y="133" fill="{accent}">rafael:</text>
    <g fill="{muted}"><text x="704" y="165">mobile: <tspan fill="{text}">[Java, Kotlin]</tspan></text>
    <text x="704" y="192">data:   <tspan fill="{text}">[Python, SQL]</tspan></text>
    <text x="704" y="219">backend: <tspan fill="{text}">Firebase</tspan></text>
    <text x="704" y="258">focus: <tspan fill="{accent}">mejora continua</tspan></text></g>
    <rect class="cursor" x="982" y="246" width="8" height="15" fill="{accent}"/>
  </g>
</g></svg>'''
    (ROOT / 'assets' / f'banner-{theme}.svg').write_text(svg, encoding='utf-8')

print('Generated dark and light banners.')
