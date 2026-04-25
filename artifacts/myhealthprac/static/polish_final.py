import re

file_path = "/home/dzhalil/Рабочий стол/антигравити/nikamed/artifacts/myhealthprac/static/index.html"

with open(file_path, "r", encoding="utf-8") as f:
    content = f.read()

# 1. FIX FLOATING BUTTON DUPLICATION
# We replace the script block with a more robust one
old_fb_script = r'<script>\s*document\.addEventListener\("DOMContentLoaded", function\(\) \{.*?setInterval\(patchFB, 1000\);\s*\}\);\s*</script>'
new_fb_script = """
<script>
document.addEventListener("DOMContentLoaded", function() {
    function patchFB() {
        const btn = document.querySelector("#maitre-inline-button") || 
                    document.querySelector("#referralhero-inline-button-MF4a5f00ee26") || 
                    document.querySelector(".rh-launcher");
        if (btn && btn.dataset.fixed !== "true") {
            // Clean EVERYTHING inside the button to stop duplication
            btn.innerHTML = '';
            const span = document.createElement('span');
            span.style.fontWeight = '600';
            span.innerText = 'Прототип by e-comEXPERT';
            btn.appendChild(span);
            
            btn.dataset.fixed = "true";
            btn.style.backgroundColor = "#010101";
            btn.style.color = "white";
            btn.style.padding = "10px 20px";
            btn.style.borderRadius = "30px";
            btn.style.zIndex = "99999";
            btn.style.display = "flex";
            btn.style.alignItems = "center";
            btn.style.justifyContent = "center";
        }
    }
    setInterval(patchFB, 500);
});
</script>
"""
content = re.sub(old_fb_script, new_fb_script, content, flags=re.DOTALL)

# 2. TRANSLATE HERO BULLETS
content = content.replace("Real-Time Analysis", "30+ лет опыта")
content = content.replace("Fast, actionable insights without long wait times.", "Разработка и дистрибуция ортопедических изделий")
content = content.replace("Personalized Health Insights", "Собственные бренды")
content = content.replace("Tailored recommendations based on your unique biomarkers.", "ORLETT, VENOTEKS, ORTMANN, BAUERFEIND, KINERAPY")
content = content.replace("Holistic Health Monitoring", "Медицинская экспертиза")
content = content.replace("Combining physical, nutritional, and mental data for a complete picture.", "Рекомендации специалистов и клиник")

# 3. FIX GEOGRAPHY SECTION (Russiamap + Glass)
# Find the geography headline and wrap in glass container
geo_pattern = re.compile(r'<div class="headline_cta"><div text-split="" letters-slide-up="" class="m_txt m_side white ch_spec">(.*?)</div>', re.DOTALL)
def add_glass_geo(match):
    text = match.group(1)
    return f'<div class="headline_cta" style="margin-bottom: 40px;"><div class="matte-container" style="text-align: left; opacity: 1; transform: none; background: rgba(255,255,255,0.7); padding: 30px 40px; border-radius: 20px;"><div text-split="" letters-slide-up="" class="m_txt m_side white ch_spec" style="color: #010101 !important; margin: 0;">{text}</div></div>'

content = geo_pattern.sub(add_glass_geo, content)
content = content.replace("/images/681b84cfb2c626858778b8a1_a36f79db72f3cbcd266117dbe37e3429_unlicensed_stills_294380_sophia-sinclair-min.jpg", "/images/Russiamap.png")

with open(file_path, "w", encoding="utf-8") as f:
    f.write(content)

print("Polishing complete.")
