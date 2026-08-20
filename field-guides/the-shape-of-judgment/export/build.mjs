import { createHash } from "node:crypto";
import fs from "node:fs/promises";
import path from "node:path";
import { fileURLToPath } from "node:url";
import JSZip from "jszip";
import MarkdownIt from "markdown-it";

const here = path.dirname(fileURLToPath(import.meta.url));
const guideRoot = path.resolve(here, "..");
const outputRoot = path.join(here, "exports");
const coverSource = path.join(here, "cover-background.png");
const release = JSON.parse(await fs.readFile(path.join(guideRoot, "release.json"), "utf8"));
const md = new MarkdownIt({ html: false, linkify: true, typographer: true });
const hash = (data) => createHash("sha256").update(data).digest("hex");
const escape = (value) => value.replaceAll("&", "&amp;").replaceAll("<", "&lt;").replaceAll(">", "&gt;").replaceAll('"', "&quot;");
const slug = (value) => value.toLowerCase().replace(/[^a-z0-9]+/g, "-").replace(/^-|-$/g, "");

const filesIn = async (directory) => (await fs.readdir(path.join(guideRoot, directory)))
  .filter((file) => file.endsWith(".md"))
  .sort()
  .map((file) => path.join(directory, file));
const sourceFiles = [...await filesIn("chapters"), ...await filesIn("worksheets")];
const sectionId = (relative) => `${relative.startsWith("chapters/") ? "chapter" : "worksheet"}-${slug(path.basename(relative, ".md"))}`;
const titleFor = (relative) => path.basename(relative, ".md").replace(/^\d+-/, "").replace(/-/g, " ").replace(/\b\w/g, (c) => c.toUpperCase());
const convertLinks = (source) => source.replaceAll("../worksheets/decision-record.md", "#worksheet-decision-record").replaceAll("../worksheets/experiment-and-promotion-card.md", "#worksheet-experiment-and-promotion-card");

const sections = [];
for (const relative of sourceFiles) {
  const source = convertLinks(await fs.readFile(path.join(guideRoot, relative), "utf8"));
  sections.push({ relative, id: sectionId(relative), title: titleFor(relative), html: md.render(source) });
}
const parts = new Map([
  ["chapters/00-how-to-use-this-guide.md", ["part-i", "Part I", "Frame the Situation"]],
  ["chapters/04-claims-before-conclusions.md", ["part-ii", "Part II", "Make Judgment Inspectable"]],
  ["chapters/07-capability-is-not-authority.md", ["part-iii", "Part III", "Govern the Consequences"]],
  ["worksheets/decision-record.md", ["worksheets", "Worksheets", "Put the Discipline to Work"]],
]);
const tocItems = [];
const bodyItems = [];
for (const { relative, id, title, html: rendered } of sections) {
  if (parts.has(relative)) {
    const [partId, label, partTitle] = parts.get(relative);
    tocItems.push(`<li class="toc-part"><a href="#${partId}">${escape(label)} — ${escape(partTitle)}</a></li>`);
    bodyItems.push(`<section class="book-part" id="${partId}"><div><p>${escape(label)}</p><h1>${escape(partTitle)}</h1></div></section>`);
  }
  tocItems.push(`<li><a href="#${id}">${escape(title)}</a></li>`);
  bodyItems.push(`<section id="${id}" data-source="${escape(relative)}">${rendered}</section>`);
}
const toc = tocItems.join("\n");
const body = bodyItems.join("\n");
const html = `<!doctype html>
<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">
<meta name="author" content="${escape(release.author)}"><meta name="dcterms.date" content="${escape(release.publicationDate)}">
<link rel="canonical" href="${escape(release.canonicalUrl)}"><title>${escape(release.title)}</title>
<meta name="description" content="${escape(release.subtitle)}"><style>
:root{--navy:#07131d;--navy-2:#0d2635;--ink:#14212a;--muted:#526572;--line:#b8c7d1;--paper:#fbfaf7;--cyan:#53c8ff;--amber:#e7a74d;font-family:Georgia,"Times New Roman",serif;line-height:1.58;color:var(--ink);background:var(--paper)}
*{box-sizing:border-box}body{margin:0;background:var(--paper)}main{max-width:52rem;margin:0 auto;padding:2.5rem 1.4rem 5rem}
.cover{position:relative;width:min(100%,52rem);min-height:70vh;margin:0 auto;overflow:hidden;color:#f5f7fa;background:var(--navy) url("cover-background.png") center/cover no-repeat;font-family:Arial,Helvetica,sans-serif}
.cover::after{content:"";position:absolute;inset:0;background:linear-gradient(180deg,rgba(4,12,19,.88) 0%,rgba(4,12,19,.35) 52%,rgba(4,12,19,.82) 100%)}
.cover-copy{position:absolute;z-index:1;inset:0;display:flex;flex-direction:column;padding:9% 8% 7%}.cover-rule{width:4rem;height:.45rem;margin-bottom:2.3rem;background:var(--cyan)}
.cover-eyebrow{margin:0 0 1.4rem;color:#b9d4df;font-size:.86rem;font-weight:800;letter-spacing:.12em;text-transform:uppercase}
.cover h1{max-width:82%;margin:0;color:#f5f7fa;font:750 clamp(3.5rem,9vw,6.5rem)/1.01 Arial,Helvetica,sans-serif;letter-spacing:-.045em}
.cover-subtitle{max-width:76%;margin:2.5rem 0 0;color:#c3d3dc;font-size:clamp(1rem,2.15vw,1.65rem);line-height:1.42;letter-spacing:.045em;text-transform:uppercase}
.cover-author{margin:auto 0 1.4rem;font-size:clamp(1.25rem,2.7vw,1.9rem);font-weight:750}.cover-meta{display:flex;justify-content:space-between;gap:1rem;padding-top:1.4rem;border-top:1px solid rgba(160,186,201,.6);color:#c8d2da;font-size:clamp(.72rem,1.55vw,.95rem);font-weight:750;letter-spacing:.08em;text-transform:uppercase}.cover-meta span:last-child{color:var(--cyan);text-align:right}
.toc{padding:1rem 0 2rem;border-bottom:1px solid var(--line);break-after:page}.toc-kicker{margin:0;color:#1686b0;font:800 .75rem/1.2 Arial,sans-serif;letter-spacing:.12em;text-transform:uppercase}.toc h1{margin:.5rem 0 .35rem;font-size:2.25rem}.toc-dek{max-width:38rem;margin:0 0 1.5rem;color:var(--muted)}.toc ol{columns:2;column-gap:2.5rem;padding:0;list-style:none;counter-reset:toc}.toc li{margin:0 0 .42rem;break-inside:avoid}.toc li:not(.toc-part){position:relative;padding-left:1.45rem;counter-increment:toc}.toc li:not(.toc-part)::before{content:counter(toc) ".";position:absolute;left:0;color:var(--muted);font-size:.88em}.toc-part{margin-top:1rem!important;list-style:none;font:800 .76rem/1.35 Arial,sans-serif;letter-spacing:.055em;text-transform:uppercase}.toc-part a{color:var(--navy-2);text-decoration:none}
a{color:#086d99;text-decoration-thickness:.055em;text-underline-offset:.12em}h1,h2,h3{color:var(--navy);font-family:Arial,Helvetica,sans-serif;line-height:1.14;break-after:avoid}h1{margin:0 0 1.5rem;font-size:2.25rem;letter-spacing:-.025em}h2{margin:2.2rem 0 .7rem;padding-top:.25rem;color:#173f53;font-size:1.35rem}h3{margin:1.6rem 0 .5rem;font-size:1.05rem}p{margin:.65rem 0 1rem}section[data-source]{break-before:page}section[data-source]>h1:first-child{padding-top:.75rem;border-top:.38rem solid var(--cyan)}section[data-source]>h1:first-child+p{color:#384f5d;font-size:1.08rem;line-height:1.62}
.book-part{min-height:62vh;display:grid;place-items:center;padding:3rem;border-top:.5rem solid var(--cyan);background:linear-gradient(145deg,var(--navy),var(--navy-2));color:#f5f7fa;text-align:center;break-before:page}.book-part p{margin:0 0 1rem;color:var(--cyan);font:800 .8rem/1.2 Arial,sans-serif;letter-spacing:.15em;text-transform:uppercase}.book-part h1{max-width:34rem;margin:0;color:#f5f7fa;font-size:3rem}
code,pre{font-family:ui-monospace,SFMono-Regular,Consolas,monospace}code{padding:.08em .25em;border-radius:.18rem;background:#e8eef1}pre{overflow-wrap:anywhere;white-space:pre-wrap;margin:1.2rem 0;padding:1rem 1.1rem;border:1px solid #b6c9d3;border-left:.35rem solid #1686b0;background:#edf5f8;color:#102934;font-size:.9rem;line-height:1.5}pre code{padding:0;background:transparent}
blockquote{margin:1.3rem 0;padding:.8rem 1.1rem;border-left:.3rem solid var(--amber);background:#f8f1e7;color:#263943}blockquote p{margin:0}table{width:100%;margin:1.25rem 0;border-collapse:collapse;font-family:Arial,Helvetica,sans-serif;font-size:.86rem;line-height:1.42}th,td{padding:.55rem .62rem;border:1px solid #b8c5cc;text-align:left;vertical-align:top;overflow-wrap:anywhere}th{background:var(--navy-2);color:#f4f8fa;font-size:.78rem;letter-spacing:.02em}tbody tr:nth-child(even){background:#f0f4f5}hr{margin:2.5rem 0;border:0;border-top:1px solid var(--line)}ul,ol{padding-left:1.45rem}li{margin:.28rem 0}.source{color:var(--muted);font:.8rem Arial,sans-serif}
@media(max-width:42rem){main{padding-inline:1rem}.cover h1{max-width:100%}.cover-subtitle{max-width:95%}.toc ol{columns:1}.cover-meta{display:block}.cover-meta span{display:block;margin-top:.4rem}.cover-meta span:last-child{text-align:left}}
@page{size:A4;margin:18mm 18mm 20mm;@bottom-center{content:counter(page);color:#71808a;font:9pt Arial,sans-serif}}@page cover{size:A4;margin:0;@bottom-center{content:none}}
@media print{body{background:#fff}.cover{page:cover;width:210mm;height:297mm;min-height:0;margin:0;break-after:page}.cover h1{font-size:25mm}.cover-subtitle{font-size:5.6mm}.cover-author{font-size:7mm}.cover-meta{font-size:3.3mm}main{padding:0}.toc{break-after:page}.book-part{min-height:220mm}a{text-decoration-thickness:.5px}table{font-size:7.5pt}thead{display:table-header-group}pre,blockquote,tr{break-inside:avoid}h1,h2,h3{break-after:avoid-page}p{orphans:3;widows:3}}
</style></head><body><section class="cover" aria-label="Book cover"><div class="cover-copy"><div class="cover-rule"></div><p class="cover-eyebrow">${escape(release.publisher)} field notes</p><h1>${escape(release.title)}</h1><p class="cover-subtitle">${escape(release.subtitle)}</p><p class="cover-author">${escape(release.author)}</p><div class="cover-meta"><span>Public review edition</span><span>v${escape(release.version)} · August 2026</span></div></div></section><main><nav class="toc"><p class="toc-kicker">${escape(release.publisher)} field notes · v${escape(release.version)}</p><h1>Contents</h1><p class="toc-dek">${escape(release.subtitle)}</p><ol>${toc}</ol></nav>${body}</main></body></html>`;

await fs.rm(outputRoot, { recursive: true, force: true });
await fs.mkdir(outputRoot, { recursive: true });
await fs.writeFile(path.join(outputRoot, "the-shape-of-judgment.html"), html);
await fs.copyFile(coverSource, path.join(outputRoot, "cover-background.png"));
const zip = new JSZip();
zip.file("mimetype", "application/epub+zip", { compression: "STORE" });
zip.file("META-INF/container.xml", `<?xml version="1.0" encoding="UTF-8"?><container version="1.0" xmlns="urn:oasis:names:tc:opendocument:xmlns:container"><rootfiles><rootfile full-path="OEBPS/content.opf" media-type="application/oebps-package+xml"/></rootfiles></container>`);
zip.file("OEBPS/book.xhtml", html.replace("<!doctype html>", '<?xml version="1.0" encoding="UTF-8"?>').replace('<html lang="en">', '<html xmlns="http://www.w3.org/1999/xhtml" xml:lang="en" lang="en">'));
zip.file("OEBPS/cover-background.png", await fs.readFile(coverSource));
zip.file("OEBPS/content.opf", `<?xml version="1.0" encoding="UTF-8"?><package xmlns="http://www.idpf.org/2007/opf" unique-identifier="book-id" version="3.0"><metadata xmlns:dc="http://purl.org/dc/elements/1.1/"><dc:identifier id="book-id">${escape(release.canonicalUrl)}</dc:identifier><dc:title>${escape(release.title)}</dc:title><dc:creator>${escape(release.author)}</dc:creator><dc:date>${escape(release.publicationDate)}</dc:date><dc:publisher>${escape(release.publisher)}</dc:publisher><dc:rights>${escape(release.rights)}</dc:rights><meta property="dcterms:modified">${escape(release.publicationDate)}T00:00:00Z</meta></metadata><manifest><item id="book" href="book.xhtml" media-type="application/xhtml+xml" properties="nav"/><item id="cover-image" href="cover-background.png" media-type="image/png" properties="cover-image"/></manifest><spine><itemref idref="book"/></spine></package>`);
await fs.writeFile(path.join(outputRoot, "the-shape-of-judgment.epub"), await zip.generateAsync({ type: "nodebuffer", mimeType: "application/epub+zip" }));
const bundle = new JSZip();
bundle.file("the-shape-of-judgment.html", html);
bundle.file("cover-background.png", await fs.readFile(coverSource));
for (const relative of sourceFiles) bundle.file(relative, await fs.readFile(path.join(guideRoot, relative)));
await fs.writeFile(path.join(outputRoot, "the-shape-of-judgment-html.zip"), await bundle.generateAsync({ type: "nodebuffer" }));
const artifacts = {};
for (const name of ["cover-background.png", "the-shape-of-judgment.html", "the-shape-of-judgment.epub", "the-shape-of-judgment-html.zip"]) {
  const data = await fs.readFile(path.join(outputRoot, name));
  artifacts[name] = { bytes: data.byteLength, sha256: hash(data) };
}
await fs.writeFile(path.join(outputRoot, "reviewer-manifest.json"), JSON.stringify({ ...release, artifacts }, null, 2) + "\n");
console.log(`Built ${sourceFiles.length} source sections and ${Object.keys(artifacts).length} artifacts.`);
