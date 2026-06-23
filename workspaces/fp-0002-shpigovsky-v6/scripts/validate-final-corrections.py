from pathlib import Path
import json

ROOT = Path(__file__).resolve().parents[1]
html = (ROOT / "dist/index.html").read_text(encoding="utf-8")
js = (ROOT / "dist/assets/js/main.js").read_text(encoding="utf-8")
scss = list((ROOT / "src/scss").glob("*.scss"))

checks = {
    "scss_files": len(scss),
    "email_fields": html.count('type="email"'),
    "name_fields": html.count('name="name"'),
    "phone_fields": html.count("data-phone-input"),
    "textarea_fields": html.count("home-final-form__textarea"),
    "consent_checkboxes": html.count("home-final-form__consent-input"),
    "submit_buttons": html.count("home-final-form__submit"),
    "yoga_images": html.count("article-yoga-therapy.webp"),
    "bos_images": html.count("article-bos-therapy.webp"),
    "swiper_inits": js.count("Swiper("),
    "fancybox_present": "fancybox" in js.lower(),
}

out = ROOT / "reviews/main-content/final-corrections/BUILD-VALIDATION.json"
out.write_text(json.dumps(checks, indent=2), encoding="utf-8")
print(json.dumps(checks, indent=2))
