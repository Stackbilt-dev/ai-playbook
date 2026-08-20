import fs from "node:fs/promises";
import path from "node:path";
import { fileURLToPath } from "node:url";
import MarkdownIt from "markdown-it";

const here = path.dirname(fileURLToPath(import.meta.url));
const guideRoot = path.resolve(here, "..");
const outputRoot = path.join(here, "exports");
const source = await fs.readFile(path.join(guideRoot, "linkedin", "edition.md"), "utf8");
const release = JSON.parse(await fs.readFile(path.join(guideRoot, "release.json"), "utf8"));
const md = new MarkdownIt({ html: false, linkify: true, typographer: true });
const escape = (value) => value.replaceAll("&", "&amp;").replaceAll("<", "&lt;").replaceAll(">", "&gt;").replaceAll('"', "&quot;");

const pages = source.split(/\n<!-- page -->\n/g).map((page) => page.trim()).filter(Boolean);
const renderedPages = pages.map((page, index) => {
  const content = md.render(page).replace("<p>", '<p class="eyebrow">');
  const classes = ["page"];
  if (index === 0) classes.push("cover");
  if (index === pages.length - 1) classes.push("cta");
  return `<section id="page-${index + 1}" class="${classes.join(" ")}" aria-label="Page ${index + 1} of ${pages.length}"><div class="page-copy">${content}</div><footer><span>The Shape of Judgment</span><span>${String(index + 1).padStart(2, "0")} / ${pages.length}</span></footer></section>`;
}).join("\n");

const html = `<!doctype html>
<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">
<meta name="author" content="${escape(release.author)}"><meta name="description" content="A concise field guide to context, evidence, and governed decisions in AI systems.">
<title>${escape(release.title)} — LinkedIn document edition</title><style>
:root{color-scheme:dark;font-family:Inter,ui-sans-serif,system-ui,-apple-system,BlinkMacSystemFont,"Segoe UI",sans-serif;color:#f4f7fa;background:#05090d;--cyan:#53c8ff;--amber:#e7a74d}*{box-sizing:border-box}html,body{margin:0;min-height:100%;background:#05090d}body{display:flex;flex-direction:column;align-items:center;gap:28px;padding:28px 0}
.page{position:relative;width:8in;height:10in;overflow:hidden;padding:.72in .72in .62in;background:radial-gradient(circle at 92% 8%,rgba(31,145,190,.18),transparent 30%),linear-gradient(145deg,#0d1e29 0%,#07131d 54%,#05090d 100%);box-shadow:0 20px 55px rgba(0,0,0,.45);break-after:page;page-break-after:always}.page:target{position:fixed;z-index:20;top:0;left:50%;margin:0;transform:translateX(-50%);box-shadow:none}.page::before{content:"";position:absolute;top:.72in;left:.72in;width:.52in;height:.07in;background:var(--cyan)}.page::after{content:"";position:absolute;right:-1.1in;bottom:1.15in;width:3.1in;height:3.1in;border:1px solid rgba(83,200,255,.11);transform:rotate(45deg)}
.page-copy{position:relative;z-index:1;height:8.22in;display:flex;flex-direction:column;justify-content:center}.eyebrow{margin:0 0 .28in;color:var(--cyan);font-size:13px;line-height:1.2;font-weight:800;letter-spacing:.16em;text-transform:uppercase}h1{max-width:6.45in;margin:0 0 .27in;color:#fff;font-size:42px;line-height:1.06;letter-spacing:-.035em}p,li{color:#d5dee5;font-size:20px;line-height:1.39}p{margin:0 0 .18in}ul,ol{margin:.02in 0 .16in;padding-left:.3in}li{margin:0 0 .1in}strong{color:#fff}a{color:#70d2ff;font-weight:750;text-decoration-thickness:2px;text-underline-offset:3px;overflow-wrap:anywhere}blockquote{margin:.14in 0 .26in;padding:.18in .22in;border-left:.07in solid var(--amber);background:rgba(231,167,77,.09)}blockquote p{margin:0;color:#fff;font-size:24px;font-weight:650;line-height:1.3}pre{margin:.14in 0 .24in;padding:.2in .23in;border:1px solid rgba(112,210,255,.24);border-left:.07in solid var(--cyan);background:rgba(83,200,255,.07);white-space:pre-wrap}pre code{color:#f4f7fa;font-size:19px;line-height:1.45}
footer{position:absolute;z-index:2;left:.72in;right:.72in;bottom:.3in;display:flex;justify-content:space-between;padding-top:.12in;border-top:1px solid rgba(165,184,199,.32);color:#8fa1af;font-size:10px;font-weight:700;letter-spacing:.1em;text-transform:uppercase}.cover{background:#060a0e url("linkedin-cover-background.png") center/cover no-repeat}.cover::after{inset:0;width:auto;height:auto;border:0;transform:none;background:linear-gradient(180deg,rgba(4,12,19,.9) 0%,rgba(4,12,19,.28) 55%,rgba(4,12,19,.86) 100%)}.cover::before{z-index:2}.cover .page-copy{z-index:3;justify-content:flex-start;padding-top:.6in}.cover .eyebrow{visibility:hidden;margin-bottom:.22in}.cover h1{max-width:6.25in;margin-top:.08in;font-size:56px;line-height:1.03}.cover p{max-width:5.9in;font-size:22px}.cover p:nth-last-child(2){margin-top:auto;font-size:21px;font-weight:750}.cover p:last-child{color:#9db0bd;font-size:14px;font-weight:700;letter-spacing:.08em;text-transform:uppercase}.cover footer{z-index:3}.cta .page-copy{justify-content:center}.cta h1{font-size:49px}.cta a{display:inline-block;margin:.08in 0 .12in;font-size:21px}
@page{size:8in 10in;margin:0}@media print{html,body{display:block;padding:0;background:#05090d;print-color-adjust:exact;-webkit-print-color-adjust:exact}.page,.page:target{position:relative;left:auto;margin:0;transform:none;box-shadow:none}.page:last-child{break-after:auto;page-break-after:auto}}
</style></head><body>${renderedPages}</body></html>`;

await fs.mkdir(outputRoot, { recursive: true });
await fs.copyFile(path.join(here, "cover-background.png"), path.join(outputRoot, "linkedin-cover-background.png"));
await fs.writeFile(path.join(outputRoot, "the-shape-of-judgment-linkedin.html"), html);
console.log(`Exported ${pages.length}-page LinkedIn edition.`);
