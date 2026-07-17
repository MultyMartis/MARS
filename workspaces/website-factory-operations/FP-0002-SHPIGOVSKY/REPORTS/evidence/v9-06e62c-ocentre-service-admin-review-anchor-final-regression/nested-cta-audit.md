BEFORE (E62C pre-change template): who-we-treat.php called shpigovsky_get_about_guest_cta_band() with default wrap_section=true, rendering nested <section class="program-cta-band-section"> inside #who-we-treat <section>.
AFTER: wrap_section forced false → <div class="program-cta-band"> inside #who-we-treat. Guest CTA later on page retains wrap_section=true as top-level section.
