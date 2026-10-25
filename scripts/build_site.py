#!/usr/bin/env python3
"""Build the two content-bearing static portfolio pages. No runtime dependencies."""
import json
from html import escape
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PUBLIC = ROOT
ORIGIN = 'https://www.egeogutucu.com'
ART = 'assets/coastal-layers.webp'
ICONS = {
    'arrow': '<svg viewBox="0 0 24 24" width="20" height="20" fill="none" aria-hidden="true"><path d="M5 12h14m-6-6 6 6-6 6" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"/></svg>',
    'external': '<svg viewBox="0 0 24 24" width="20" height="20" fill="none" aria-hidden="true"><path d="M7 17 17 7M7 7h10v10" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"/></svg>',
    'code': '<svg viewBox="0 0 120 120" fill="none" aria-hidden="true"><path d="m39 40-22 20 22 20m42-40 22 20-22 20M70 27 50 93" stroke="currentColor" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"/></svg>',
    'network': '<svg viewBox="0 0 120 120" fill="none" aria-hidden="true"><circle cx="60" cy="60" r="39" stroke="currentColor" stroke-width="2"/><ellipse cx="60" cy="60" rx="18" ry="39" stroke="currentColor" stroke-width="2"/><path d="M23 47h74M23 73h74M60 21v78" stroke="currentColor" stroke-width="2"/></svg>',
    'auth': '<svg viewBox="0 0 120 120" fill="none" aria-hidden="true"><rect x="28" y="49" width="64" height="49" rx="5" stroke="currentColor" stroke-width="2"/><path d="M41 49V34a19 19 0 0 1 38 0v15" stroke="currentColor" stroke-width="2"/><circle cx="60" cy="70" r="5" stroke="currentColor" stroke-width="2"/><path d="M60 75v9" stroke="currentColor" stroke-width="2"/></svg>',
}
COPY = {
 'tr': {
  'title': 'Ege Öğütücü | Python ve Backend Geliştirme Portföyü',
  'description': 'Ege Öğütücü’nün kişisel portföyü. Python, backend geliştirme ve siber güvenlik odağındaki projeleri, BTK Akademi sertifikaları ve iletişim bilgileri.',
  'nav': ['Hakkımda', 'Projeler', 'Sertifikalar', 'İletişim'], 'skip': 'İçeriğe geç', 'language': 'EN', 'language_label': 'View this website in English', 'language_href': 'EN.html',
  'contact_short': 'Birlikte konuşalım', 'menu': 'Menüyü aç', 'menu_close': 'Menüyü kapat',
  'availability': 'Staj fırsatlarına açığım', 'role': 'Python, backend ve bitmeyen bir merak.',
  'intro': 'Kodun arkasındaki mantığı anlamayı, küçük fikirleri çalışan projelere dönüştürmeyi seviyorum. Yazılım geliştiriyorum. Öğrenmeye devam ediyorum.',
  'projects_cta': 'Projelerimi keşfet', 'contact_cta': 'İletişime geç', 'github': 'GitHub profilim',
  'art_label': 'EGE KATMANLARI', 'art_caption': 'Merak. Üretim. Gelişim.', 'art_alt': 'Lacivert ve kil tonlarında, Ege kıyılarından esinlenen soyut katmanlı heykeller',
  'scroll': 'Aşağı kaydır', 'strip': 'ÇALIŞMA ALANIM',
  'about_kicker': 'BENİM HİKÂYEM', 'about_heading': 'Meraktan koda.\nHer gün bir adım daha.',
  'about_lead': 'Ben Ege. Ankara Medipol Üniversitesi’nde Arka-yüz yazılım geliştirme öğrencisiyim.',
  'about_body': 'Python ile backend geliştirme, API entegrasyonları ve otomasyon üzerine çalışıyorum. Linux üzerinde lab ortamında denemeler yapıyorum. Nmap, Bettercap ve Wireshark bilgim var; siber güvenlik alanında kendimi geliştirmeye devam ediyorum. Git ve GitHub ile çalışmalarımı düzenli tutuyor; öğrendiklerimi küçük, somut projelerde deniyorum.',
  'about_goal': 'Şimdi, gerçek görevler üstlenebileceğim, geri bildirimle gelişebileceğim ve bir ekiple birlikte üretebileceğim bir staj fırsatı arıyorum.',
  'values': [('Merakla öğrenmek', 'Nasıl çalıştığını anlamak, doğru soruları sormak ve yeni şeyler denemek.'), ('Düzenli üretmek', 'Fikirleri küçük adımlara bölmek, temiz bir proje yapısı ve okunabilir kodla ilerlemek.'), ('Birlikte gelişmek', 'Geri bildirime açık olmak, iletişim kurmak ve takımın bir parçası olarak katkı sunmak.')],
  'skills': 'Kullandığım ve öğrendiğim teknolojiler',
  'projects_kicker': 'KODDAN ÇIKANLAR', 'projects_heading': 'Öğrendiklerim,\nprojelere dönüşüyor.', 'projects_intro': 'GitHub’da paylaştığım çalışmalar. Küçük denemeler, yeni fikirler ve devam eden bir öğrenme süreci.',
  'project_type': ['PYTHON / ÖĞRENME', 'AĞ / KEŞİF', 'WEB / KİMLİK DOĞRULAMA'],
  'project_titles': ['Python Pratik Projeleri', 'Python VPN & Ağ İzleme', 'Supabase Auth REST API'],
  'project_desc': ['Şehir hava durumunu wttr.in üzerinden alan uygulama, Hacker News başlıklarını çeken web scraping çalışması ve dört işlem yapan CLI hesap makinesi. Öğrendiklerimi küçük uygulamalarla pekiştiriyorum.', 'IP bilgisi ve konumu, CSV loglama, isteğe bağlı Telegram bildirimleri ve ping/hız testi yardımcıları içeren bir Python çalışması. Odak noktası ağ izleme ve tanılama; VPN tüneli yöneten bir servis değil.', 'Express ve Supabase Auth ile kayıt, giriş, çıkış ve token yenileme akışları. Bearer token ile korunan profil okuma/güncelleme endpoint’leri ve RLS için SQL kurulumu. Kaynak kod projesidir; canlı servis demosu değildir.'],
  'project_link': 'Depoyu incele', 'project_note': 'Kaynak kod GitHub’da', 'all_projects': 'GitHub’daki tüm herkese açık çalışmalarım',
  'cert_kicker': 'ÖĞRENME İZLERİ', 'cert_heading': 'Bilgiyi büyütmek.\nAdım adım.', 'cert_intro': 'BTK Akademi’de tamamladığım eğitimler. Her sertifikanın özgün PDF belgesini açabilirsin.',
  'cert_titles': ['Ağ Temelleri', 'Siber Güvenliğe Giriş', 'Siber Güvenlikte Linux İşletim Sistemleri', 'Sıfırdan İleri Seviye Python Programlama'],
  'cert_dates': ['02 Ocak 2026', '31 Aralık 2025', '09 Ocak 2026', '30 Nisan 2026'], 'cert_action': 'Belgeyi aç', 'new_tab': 'yeni sekmede açılır',
  'contact_kicker': 'BİR SONRAKİ ADIM', 'contact_heading': 'Güzel işler,\nbir merhabayla başlar.', 'contact_intro': 'Bir staj fırsatı, proje fikri ya da sadece bir merhaba. Mesajını okumayı isterim.',
  'mail': 'E-posta gönder', 'copy': 'E-postayı kopyala', 'copied': 'E-posta adresi kopyalandı.', 'copy_fail': 'Kopyalanamadı. Adresi seçerek kopyalayabilirsin.',
  'footer': 'Merakla öğreniyor, özenle üretiyorum.', 'top': 'Başa dön', 'lang_name': 'Türkçe',
 },
 'en': {
  'title': 'Ege Ogutucu | Python & Backend Development Portfolio',
  'description': 'The personal portfolio of Ege Ogutucu. Explore Python, backend and cybersecurity learning projects, BTK Academy certificates, and contact information.',
  'nav': ['About', 'Projects', 'Certificates', 'Contact'], 'skip': 'Skip to content', 'language': 'TR', 'language_label': 'Bu siteyi Türkçe görüntüle', 'language_href': 'index.html',
  'contact_short': 'Let’s talk', 'menu': 'Open menu', 'menu_close': 'Close menu',
  'availability': 'Open to internship opportunities', 'role': 'Python, backend, and endless curiosity.',
  'intro': 'I enjoy understanding the logic behind code and turning small ideas into working projects. I build software. And I keep learning.',
  'projects_cta': 'Explore my projects', 'contact_cta': 'Get in touch', 'github': 'My GitHub profile',
  'art_label': 'AEGEAN LAYERS', 'art_caption': 'Curiosity. Making. Growth.', 'art_alt': 'Abstract layered navy and terracotta sculptures inspired by the Aegean coastline',
  'scroll': 'Scroll to explore', 'strip': 'MY FOCUS',
  'about_kicker': 'MY STORY', 'about_heading': 'From curiosity to code.\nOne step at a time.',
  'about_lead': 'I’m Ege, a Back-end Software Development student at Ankara Medipol University.',
  'about_body': 'I work on Python backend development, API integrations, and automation. I experiment in Linux lab environments. I have knowledge of Nmap, Bettercap, and Wireshark, and continue developing my skills in cybersecurity. I use Git and GitHub to organize my work, and put what I learn into practice through small, tangible projects.',
  'about_goal': 'I’m looking for an internship where I can take on real tasks, grow through feedback, and build things as part of a team.',
  'values': [('Stay curious', 'Understand how things work, ask useful questions, and try something new.'), ('Build with care', 'Break ideas into small steps, with a clean project structure and readable code.'), ('Grow together', 'Welcome feedback, communicate openly, and contribute as part of a team.')],
  'skills': 'Technologies I use and learn',
  'projects_kicker': 'IDEAS IN CODE', 'projects_heading': 'Turning what I learn\ninto things I build.', 'projects_intro': 'Work I share on GitHub. Small experiments, new ideas, and an ongoing learning process.',
  'project_type': ['PYTHON / LEARNING', 'NETWORKING / EXPLORATION', 'WEB / AUTHENTICATION'],
  'project_titles': ['Python Practice Projects', 'Python VPN & Network Monitoring', 'Supabase Auth REST API'],
  'project_desc': ['A city weather app using wttr.in, a Hacker News headline scraper, and a four-operation CLI calculator. Small applications that turn Python learning into practice.', 'A Python project with IP discovery and geolocation, CSV logging, optional Telegram alerts, and ping/speed-test helpers. Focused on network monitoring and diagnostics, not on managing VPN tunnels.', 'Register, login, logout, and token-refresh flows with Express and Supabase Auth. Bearer-token-protected profile read/update endpoints and SQL setup for RLS. A source code project, not a deployed service demo.'],
  'project_link': 'Explore repository', 'project_note': 'Source code on GitHub', 'all_projects': 'All my public work on GitHub',
  'cert_kicker': 'LEARNING MILESTONES', 'cert_heading': 'Growing my knowledge.\nStep by step.', 'cert_intro': 'Courses I completed at BTK Academy. Each certificate links to its original PDF document.',
  'cert_titles': ['Network Fundamentals', 'Introduction to Cybersecurity', 'Linux Operating Systems in Cybersecurity', 'Python Programming: From Beginner to Advanced'],
  'cert_dates': ['02 January 2026', '31 December 2025', '09 January 2026', '30 April 2026'], 'cert_action': 'View certificate', 'new_tab': 'opens in a new tab',
  'contact_kicker': 'THE NEXT STEP', 'contact_heading': 'Good things start\nwith a hello.', 'contact_intro': 'An internship opportunity, a project idea, or simply a hello. I’d love to hear from you.',
  'mail': 'Send an email', 'copy': 'Copy email address', 'copied': 'Email address copied.', 'copy_fail': 'Could not copy. You can select and copy the address.',
  'footer': 'Learning with curiosity. Building with care.', 'top': 'Back to top', 'lang_name': 'English',
 }
}


def lines(text):
    return '<br>'.join(escape(x) for x in text.split('\n'))


def build(lang):
    c = COPY[lang]
    arrow, ext = ICONS['arrow'], ICONS['external']
    page_url = ORIGIN + ('/' if lang == 'tr' else '/EN.html')
    sections = ['about', 'projects', 'certificates', 'contact']
    nav = ''.join(f'<a href="#{s}" data-section="{s}">{escape(label)}</a>' for s, label in zip(sections, c['nav']))
    values = ''.join(f'<div class="value-item"><span class="value-index">0{i}</span><h3>{escape(title)}</h3><p>{escape(body)}</p></div>' for i,(title,body) in enumerate(c['values'],1))
    projects = []
    for i,(repo,icon,tags) in enumerate([('python-projects','code',['Python','Requests','BeautifulSoup']),('Python-vpn','network',['Python','CSV','Telegram API']),('supabase-auth-api','auth',['Node.js','Express','Supabase','REST API'])]):
        projects.append(f'''<article class="project-card reveal">
          <div class="project-visual visual-{['python','network','auth'][i]}"><span class="project-number">0{i+1} /</span><div class="project-symbol">{ICONS[icon]}</div><span class="project-status">{escape(repo)}</span></div>
          <div class="project-body"><p class="project-type">{c['project_type'][i]}</p><h3 class="project-title">{c['project_titles'][i]}</h3><p class="project-description">{c['project_desc'][i]}</p><div class="tags">{''.join(f'<span>{escape(t)}</span>' for t in tags)}</div><a class="project-link" href="https://github.com/Egeogutucu26/{repo}" target="_blank" rel="noopener noreferrer" aria-label="{escape(c['project_titles'][i] + ': ' + c['project_link'] + ', ' + c['new_tab'])}">{c['project_link']} {ext}</a></div>
        </article>''')
    certificates = []
    for i,(file,date) in enumerate([('ag-temelleri.pdf','2026-01-02'),('siber-linux.pdf','2025-12-31'),('siber-guvenlik-giris.pdf','2026-01-09'),('python-siber.pdf','2026-04-30')]):
        certificates.append(f'''<article class="certificate-row"><span class="certificate-number">0{i+1}</span><div class="certificate-title"><h3>{c['cert_titles'][i]}</h3><p class="certificate-provider">BTK {'Akademi' if lang=='tr' else 'Academy'}</p></div><time class="certificate-date" datetime="{date}">{c['cert_dates'][i]}</time><a class="certificate-link" href="{file}" target="_blank" rel="noopener noreferrer" aria-label="{escape(c['cert_titles'][i] + ': ' + c['cert_action'] + ', ' + c['new_tab'])}">{c['cert_action']} {ext}</a></article>''')
    schema = {'@context':'https://schema.org','@type':'Person','name':'Ege Öğütücü','url':ORIGIN+'/', 'sameAs':['https://github.com/Egeogutucu26','https://www.linkedin.com/in/ege-%C3%B6%C4%9F%C3%BCt%C3%BCc%C3%BC-393560169'], 'description':c['about_lead']}
    html = f'''<!doctype html>
<html lang="{lang}">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>{escape(c['title'])}</title>
  <meta name="description" content="{escape(c['description'])}">
  <meta name="keywords" content="Ege Öğütücü, Python, backend, portfolio, cybersecurity">
  <meta name="theme-color" content="#12304A">
  <link rel="canonical" href="{page_url}">
  <link rel="alternate" hreflang="tr" href="{ORIGIN}/">
  <link rel="alternate" hreflang="en" href="{ORIGIN}/EN.html">
  <link rel="alternate" hreflang="x-default" href="{ORIGIN}/">
  <meta property="og:type" content="website">
  <meta property="og:title" content="{escape(c['title'])}">
  <meta property="og:description" content="{escape(c['description'])}">
  <meta property="og:url" content="{page_url}">
  <meta property="og:site_name" content="Ege Öğütücü">
  <meta property="og:locale" content="{'tr_TR' if lang=='tr' else 'en_US'}">
  <meta property="og:image" content="{ORIGIN}/assets/social-card.png">
  <meta property="og:image:width" content="1200">
  <meta property="og:image:height" content="630">
  <meta name="twitter:card" content="summary_large_image">
  <meta name="twitter:title" content="{escape(c['title'])}">
  <meta name="twitter:description" content="{escape(c['description'])}">
  <meta name="twitter:image" content="{ORIGIN}/assets/social-card.png">
  <link rel="icon" href="favicon.ico" sizes="any">
  <link rel="icon" href="favicon-32x32.png" type="image/png">
  <link rel="apple-touch-icon" href="apple-touch-icon.png">
  <link rel="manifest" href="site.webmanifest">
  <link rel="preload" href="assets/manrope-800.woff2" as="font" type="font/woff2" crossorigin>
  <link rel="stylesheet" href="style.css?v=ege-layers-1">
  <script type="application/ld+json">{json.dumps(schema,ensure_ascii=False)}</script>
  <script src="site.js?v=ege-layers-1" defer></script>
</head>
<body id="top">
  <a class="skip-link" href="#main">{c['skip']}</a>
  <header class="site-header">
    <div class="container header-inner">
      <a class="brand" href="#top" aria-label="Ege Öğütücü"><span class="brand-mark" aria-hidden="true">e<span>.</span></span><span class="brand-name">Ege Öğütücü</span></a>
      <nav class="desktop-nav" aria-label="{'Ana menü' if lang=='tr' else 'Main navigation'}">{nav}</nav>
      <div class="header-actions"><a class="language-link" href="{c['language_href']}" hreflang="{'en' if lang=='tr' else 'tr'}" lang="{'en' if lang=='tr' else 'tr'}" aria-label="{c['language_label']}">{c['language']}</a><a class="nav-contact" href="#contact">{c['contact_short']} {ext}</a><button class="menu-toggle" type="button" aria-expanded="false" aria-controls="mobile-nav" aria-label="{c['menu']}" data-open-label="{c['menu']}" data-close-label="{c['menu_close']}"><span></span><span></span></button></div>
    </div>
    <nav class="mobile-nav container" id="mobile-nav" aria-label="{'Mobil menü' if lang=='tr' else 'Mobile navigation'}" data-open="false">{nav}</nav>
  </header>
  <main id="main">
    <section class="hero" aria-labelledby="hero-title">
      <div class="container hero-inner">
        <div class="hero-copy">
          <p class="eyebrow"><span class="status-dot" aria-hidden="true"></span>{c['availability']}</p>
          <h1 class="hero-name" id="hero-title"><span>Ege</span><span>Öğütücü<span class="clay">.</span></span></h1>
          <h2 class="hero-role">{c['role']}</h2>
          <p class="hero-description">{c['intro']}</p>
          <div class="hero-actions"><a class="button button-primary" href="#projects">{c['projects_cta']} {arrow}</a><a class="button button-outline" href="#contact">{c['contact_cta']}</a></div>
          <a class="hero-social" href="https://github.com/Egeogutucu26" target="_blank" rel="noopener noreferrer">{c['github']} {ext}</a>
        </div>
        <div class="hero-art"><img class="hero-art-image" src="{ART}" width="800" height="1000" alt="{c['art_alt']}" fetchpriority="high"><div class="art-label"><span>{c['art_label']}</span><span>{c['art_caption']}</span></div></div>
      </div>
      <div class="container hero-note"><span>PYTHON / BACKEND / CYBERSECURITY</span><a class="scroll-link" href="#about">{c['scroll']} <span aria-hidden="true">↓</span></a></div>
    </section>
    <div class="tech-strip"><div class="container tech-strip-inner"><span class="strip-label">{c['strip']}</span><div class="tech-items"><span>Python</span><span>API &amp; JSON</span><span>Git / GitHub</span><span>Linux</span></div></div></div>
    <section class="section about-section" id="about" aria-labelledby="about-title">
      <div class="container">
        <div class="about-layout"><div><p class="section-kicker"><span class="section-number">01 /</span> {c['about_kicker']}</p><h2 id="about-title">{lines(c['about_heading'])}</h2></div><div class="about-copy"><p class="about-lead">{c['about_lead']}</p><p>{c['about_body']}</p><p>{c['about_goal']}</p></div></div>
        <div class="about-values">{values}</div>
        <div class="skills-line"><p>{c['skills']}</p><div class="tags"><span>Python</span><span>API / JSON</span><span>Git &amp; GitHub</span><span>Linux</span><span>HTML / CSS ({'temel' if lang=='tr' else 'basics'})</span></div></div>
      </div>
    </section>
    <section class="section projects-section" id="projects" aria-labelledby="projects-title">
      <div class="container"><div class="section-heading"><div><p class="section-kicker"><span class="section-number">02 /</span> {c['projects_kicker']}</p><h2 id="projects-title">{lines(c['projects_heading'])}</h2></div><p class="section-intro">{c['projects_intro']}</p></div><div class="project-list">{''.join(projects)}</div><a class="project-link all-projects" href="https://github.com/Egeogutucu26?tab=repositories" target="_blank" rel="noopener noreferrer">{c['all_projects']} {ext}</a></div>
    </section>
    <section class="section certificates-section" id="certificates" aria-labelledby="certificates-title">
      <div class="container"><div class="section-heading"><div><p class="section-kicker"><span class="section-number">03 /</span> {c['cert_kicker']}</p><h2 id="certificates-title">{lines(c['cert_heading'])}</h2></div><p class="section-intro">{c['cert_intro']}</p></div><div class="certificate-list">{''.join(certificates)}</div></div>
    </section>
    <section class="section contact-section" id="contact" aria-labelledby="contact-title">
      <div class="container"><div class="contact-layout"><div><p class="section-kicker contact-eyebrow"><span class="section-number">04 /</span> {c['contact_kicker']}</p><h2 class="contact-heading" id="contact-title">{lines(c['contact_heading'])}</h2><p class="contact-intro">{c['contact_intro']}</p></div><div><a class="contact-email" href="mailto:egeogutucu@gmail.com">egeogutucu<span>@gmail.com</span></a><div class="contact-actions"><a class="button button-primary" href="mailto:egeogutucu@gmail.com">{c['mail']} {arrow}</a><button class="copy-button" type="button" data-copy="egeogutucu@gmail.com" data-success="{c['copied']}" data-failure="{c['copy_fail']}">{c['copy']}</button></div><div class="contact-socials"><a href="https://github.com/Egeogutucu26" target="_blank" rel="noopener noreferrer">GitHub {ext}</a><a href="https://www.linkedin.com/in/ege-%C3%B6%C4%9F%C3%BCt%C3%BCc%C3%BC-393560169" target="_blank" rel="noopener noreferrer">LinkedIn {ext}</a></div></div></div></div>
    </section>
  </main>
  <footer class="site-footer"><div class="container footer-inner"><a class="footer-brand" href="#top">Ege Öğütücü<span class="clay">.</span></a><p class="footer-note">© <span id="year">2026</span> · {c['footer']}</p><a class="back-top" href="#top">{c['top']} ↑</a></div></footer>
  <div class="toast" id="toast" role="status" aria-live="polite" hidden></div>
</body>
</html>
'''
    (PUBLIC / ('index.html' if lang=='tr' else 'EN.html')).write_text(html,encoding='utf-8')


if __name__ == '__main__':
    PUBLIC.mkdir(exist_ok=True)
    for language in ['tr','en']:
        build(language)
    (PUBLIC/'manus-routes.json').write_text(json.dumps({'routes':[{'path':'/','title':'Ege Öğütücü'},{'path':'/index.html','title':'Ege Öğütücü — Türkçe'},{'path':'/EN.html','title':'Ege Ogutucu — English'}]},ensure_ascii=False)+'\n')
    (PUBLIC/'site.webmanifest').write_text(json.dumps({'name':'Ege Öğütücü — Kişisel Portföy','short_name':'Ege Öğütücü','start_url':'/','display':'browser','background_color':'#12304A','theme_color':'#12304A','icons':[{'src':'android-chrome-192x192.png','sizes':'192x192','type':'image/png'},{'src':'android-chrome-512x512.png','sizes':'512x512','type':'image/png'}]},ensure_ascii=False)+'\n')
    (PUBLIC/'robots.txt').write_text('User-agent: *\nAllow: /\nSitemap: '+ORIGIN+'/sitemap.xml\n')
    (PUBLIC/'sitemap.xml').write_text('<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9" xmlns:xhtml="http://www.w3.org/1999/xhtml"><url><loc>'+ORIGIN+'/</loc><xhtml:link rel="alternate" hreflang="en" href="'+ORIGIN+'/EN.html"/><xhtml:link rel="alternate" hreflang="tr" href="'+ORIGIN+'/"/></url><url><loc>'+ORIGIN+'/EN.html</loc><xhtml:link rel="alternate" hreflang="en" href="'+ORIGIN+'/EN.html"/><xhtml:link rel="alternate" hreflang="tr" href="'+ORIGIN+'/"/></url></urlset>\n')
    print('Built Turkish and English static pages.')
