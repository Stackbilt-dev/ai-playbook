import fs from "node:fs/promises";
import path from "node:path";
import { createHash } from "node:crypto";
import JSZip from "jszip";

const outputRoot = path.resolve(new URL(".", import.meta.url).pathname, "exports");
const release = JSON.parse(await fs.readFile(path.join(outputRoot, "..", "..", "release.json"), "utf8"));
const manifest = JSON.parse(await fs.readFile(path.join(outputRoot, "reviewer-manifest.json"), "utf8"));
const hash = (data) => createHash("sha256").update(data).digest("hex");
const assert = (condition, message) => { if (!condition) throw new Error(message); };
const html = await fs.readFile(path.join(outputRoot, "the-shape-of-judgment.html"), "utf8");
const linkedInHtml = await fs.readFile(path.join(outputRoot, "the-shape-of-judgment-linkedin.html"), "utf8");
assert(html.includes(`v${release.version}`), "HTML version metadata is stale");
assert(html.includes('class="cover"'), "Complete edition is missing its designed cover");
assert(html.includes("The Lead That Stopped"), "Revenue case is missing");
assert(html.includes("The Silent Loop"), "Silent Loop case is missing");
assert(html.includes("The Fluent Omission"), "Fluent Omission case is missing");
assert(!/href="(?!https?:)[^\"]+\.md"/.test(html), "Reader-facing Markdown link remains");
const linkedInPages = [...linkedInHtml.matchAll(/<section id="page-\d+" class="page(?: [^"]+)?"/g)];
assert(linkedInPages.length === 13, `LinkedIn edition has ${linkedInPages.length} pages instead of 13`);
assert(linkedInHtml.includes("Evaluation is not authorization"), "LinkedIn edition is missing the evaluation boundary");
for (const name of Object.keys(manifest.artifacts)) {
  const data = await fs.readFile(path.join(outputRoot, name));
  assert(data.byteLength === manifest.artifacts[name].bytes, `Artifact size mismatch: ${name}`);
  assert(hash(data) === manifest.artifacts[name].sha256, `Artifact hash mismatch: ${name}`);
}
const epub = await JSZip.loadAsync(await fs.readFile(path.join(outputRoot, "the-shape-of-judgment.epub")));
assert(epub.files["OEBPS/book.xhtml"], "EPUB is missing XHTML content");
assert(epub.files["OEBPS/content.opf"], "EPUB is missing package metadata");
assert(epub.files["OEBPS/cover-background.png"], "EPUB is missing cover artwork");
const pdf = await fs.readFile(path.join(outputRoot, "the-shape-of-judgment.pdf"));
assert(pdf.byteLength > 100_000, "PDF is unexpectedly small");
const linkedInPdf = await fs.readFile(path.join(outputRoot, "the-shape-of-judgment-linkedin.pdf"));
assert(linkedInPdf.byteLength > 100_000, "LinkedIn PDF is unexpectedly small");
console.log(JSON.stringify({ version: release.version, sourceSections: (html.match(/data-source=/g) ?? []).length, epubFiles: Object.keys(epub.files).length, pdfBytes: pdf.byteLength, linkedInPages: linkedInPages.length, linkedInPdfBytes: linkedInPdf.byteLength }, null, 2));
