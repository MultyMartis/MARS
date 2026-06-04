import { chromium, devices } from "playwright";
import { join, dirname } from "path";
import { fileURLToPath } from "url";

const __dirname = dirname(fileURLToPath(import.meta.url));
const QUERY = "грузотакси краснодар";
const LR = "35";

async function main() {
  const browser = await chromium.launch({ headless: true });
  const context = await browser.newContext({
    ...devices["iPhone 13"],
    locale: "ru-RU",
  });
  const page = await context.newPage();
  await page.goto(
    `https://yandex.ru/search/touch/?text=${encodeURIComponent(QUERY)}&lr=${LR}`,
    { waitUntil: "networkidle", timeout: 60000 }
  );
  await page.waitForTimeout(3000);

  await page.screenshot({
    path: join(__dirname, "serp-top-ads.png"),
    fullPage: false,
  });

  await page.evaluate(() => window.scrollBy(0, 900));
  await page.waitForTimeout(1000);
  await page.screenshot({
    path: join(__dirname, "serp-organic-block.png"),
    fullPage: false,
  });

  await page.evaluate(() => window.scrollBy(0, 1200));
  await page.waitForTimeout(1000);
  await page.screenshot({
    path: join(__dirname, "serp-maps-organic.png"),
    fullPage: false,
  });

  await browser.close();
  console.log("section screenshots saved");
}

main();
