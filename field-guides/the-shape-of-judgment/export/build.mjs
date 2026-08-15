import { createHash } from "node:crypto";
import fs from "node:fs/promises";
import path from "node:path";
import { fileURLToPath } from "node:url";
import JSZip from "jszip";
import MarkdownIt from "markdown-it";

const here = path.dirname(fileURLToPath(import.meta.url));
const guideRoot = path.resolve(here, "..");
const outputRoot = path.join(here, "exports");
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
const toc = sections.map(({ id, title }) => `<li><a href="#${id}">${escape(title)}</a></li>`).join("\n");
const body = sections.map(({ relative, id, html }) => `<section id="${id}" data-source="${escape(relative)}">${html}</section>`).join("\n");
const html = `<!doctype html>
<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">
<meta name="author" content="${escape(release.author)}"><meta name="dcterms.date" content="${escape(release.publicationDate)}">
<link rel="canonical" href="${escape(release.canonicalUrl)}"><title>${escape(release.title)}</title>
<meta name="description" content="${escape(release.subtitle)}"><style>
:root{font-family:Georgia,serif;line-height:1.58;color:#1b1d20;background:#fff}body{margin:0}main{max-width:52rem;margin:0 auto;padding:2rem 1.25rem 5rem}.cover{min-height:70vh;display:grid;place-items:center;padding:4rem 2rem;color:#f5f7fa;background:linear-gradient(145deg,#08121b,#12384b);text-align:center}.cover h1{max-width:42rem;font:700 clamp(3rem,9vw,6rem)/1.02 Arial,sans-serif;letter-spacing:-.04em;margin:0}.cover p{max-width:38rem;color:#b9d4df;font:1.15rem/1.45 Arial,sans-serif;text-transform:uppercase;letter-spacing:.06em}.meta{color:#53c8ff;font:bold .85rem Arial,sans-serif;letter-spacing:.1em;text-transform:uppercase}.toc{border-bottom:1px solid #8a929b;margin-bottom:3rem;padding-bottom:1.5rem}.toc ol{columns:2}.toc li{margin:.35rem 0}h1,h2,h3{line-height:1.2;color:#111;break-after:avoid}h1{font-size:2rem;margin-top:3rem}h2{font-size:1.4rem;margin-top:2rem}a{color:#075985}code,pre{font-family:ui-monospace,SFMono-Regular,Consolas,monospace}code{background:#eef1f4;padding:.1em .25em}pre{overflow-wrap:anywhere;white-space:pre-wrap;background:#f3f5f7;border:1px solid #c8ced4;padding:1rem}blockquote{border-left:.25rem solid #1686b0;margin-left:0;padding-left:1rem}table{border-collapse:collapse;width:100%;margin:1rem 0}th,td{border:1px solid #8a929b;padding:.5rem;text-align:left;vertical-align:top;overflow-wrap:anywhere}th{background:#eef1f4}section{break-before:page}section:first-of-type{break-before:auto}.source{font:0.8rem Arial,sans-serif;color:#52606d}@page{size:A4;margin:18mm}@media print{.cover{min-height:240mm;break-after:page}main{padding:0}.toc{break-after:page}a{text-decoration-thickness:.5px}table{font-size:.85em}pre,blockquote,tr{break-inside:avoid}h1,h2,h3{break-after:avoid-page}}
</style></head><body><header class="cover"><div><p class="meta">${escape(release.publisher)} field notes · v${escape(release.version)}</p><h1>${escape(release.title)}</h1><p>${escape(release.subtitle)}</p><p>${escape(release.author)}</p></div></header><main><nav class="toc"><h1>Contents</h1><ol>${toc}</ol></nav>${body}</main></body></html>`;

await fs.rm(outputRoot, { recursive: true, force: true });
await fs.mkdir(outputRoot, { recursive: true });
await fs.writeFile(path.join(outputRoot, "the-shape-of-judgment.html"), html);
const zip = new JSZip();
zip.file("mimetype", "application/epub+zip", { compression: "STORE" });
zip.file("META-INF/container.xml", `<?xml version="1.0" encoding="UTF-8"?><container version="1.0" xmlns="urn:oasis:names:tc:opendocument:xmlns:container"><rootfiles><rootfile full-path="OEBPS/content.opf" media-type="application/oebps-package+xml"/></rootfiles></container>`);
zip.file("OEBPS/book.xhtml", html.replace("<!doctype html>", '<?xml version="1.0" encoding="UTF-8"?>').replace('<html lang="en">', '<html xmlns="http://www.w3.org/1999/xhtml" xml:lang="en" lang="en">'));
zip.file("OEBPS/content.opf", `<?xml version="1.0" encoding="UTF-8"?><package xmlns="http://www.idpf.org/2007/opf" unique-identifier="book-id" version="3.0"><metadata xmlns:dc="http://purl.org/dc/elements/1.1/"><dc:identifier id="book-id">${escape(release.canonicalUrl)}</dc:identifier><dc:title>${escape(release.title)}</dc:title><dc:creator>${escape(release.author)}</dc:creator><dc:date>${escape(release.publicationDate)}</dc:date><dc:publisher>${escape(release.publisher)}</dc:publisher><dc:rights>${escape(release.rights)}</dc:rights><meta property="dcterms:modified">${escape(release.publicationDate)}T00:00:00Z</meta></metadata><manifest><item id="book" href="book.xhtml" media-type="application/xhtml+xml" properties="nav"/></manifest><spine><itemref idref="book"/></spine></package>`);
await fs.writeFile(path.join(outputRoot, "the-shape-of-judgment.epub"), await zip.generateAsync({ type: "nodebuffer", mimeType: "application/epub+zip" }));
const bundle = new JSZip();
bundle.file("the-shape-of-judgment.html", html);
for (const relative of sourceFiles) bundle.file(relative, await fs.readFile(path.join(guideRoot, relative)));
await fs.writeFile(path.join(outputRoot, "the-shape-of-judgment-html.zip"), await bundle.generateAsync({ type: "nodebuffer" }));
const artifacts = {};
for (const name of ["the-shape-of-judgment.html", "the-shape-of-judgment.epub", "the-shape-of-judgment-html.zip"]) {
  const data = await fs.readFile(path.join(outputRoot, name));
  artifacts[name] = { bytes: data.byteLength, sha256: hash(data) };
}
await fs.writeFile(path.join(outputRoot, "reviewer-manifest.json"), JSON.stringify({ ...release, artifacts }, null, 2) + "\n");
console.log(`Built ${sourceFiles.length} source sections and ${Object.keys(artifacts).length} artifacts.`);
