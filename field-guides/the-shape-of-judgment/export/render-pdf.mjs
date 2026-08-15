import fs from "node:fs/promises";
import path from "node:path";
import { execFile } from "node:child_process";
import { promisify } from "node:util";
import { fileURLToPath, pathToFileURL } from "node:url";
import { createHash } from "node:crypto";

const execFileAsync = promisify(execFile);
const here = path.dirname(fileURLToPath(import.meta.url));
const outputRoot = path.join(here, "exports");
const candidates = [process.env.CHROME_PATH, "/usr/bin/google-chrome", "/usr/bin/chromium", "/usr/bin/chromium-browser"].filter(Boolean);
let chrome;
for (const candidate of candidates) { try { await fs.access(candidate); chrome = candidate; break; } catch {} }
if (!chrome) throw new Error("Chrome or Chromium was not found. Set CHROME_PATH to a browser executable.");
const output = path.join(outputRoot, "the-shape-of-judgment.pdf");
await execFileAsync(chrome, ["--headless=new", "--disable-gpu", "--no-sandbox", "--no-pdf-header-footer", "--run-all-compositor-stages-before-draw", `--print-to-pdf=${output}`, pathToFileURL(path.join(outputRoot, "the-shape-of-judgment.html")).href]);
const stats = await fs.stat(output);
if (stats.size < 100_000) throw new Error(`PDF is unexpectedly small (${stats.size} bytes)`);
const manifestPath = path.join(outputRoot, "reviewer-manifest.json");
const manifest = JSON.parse(await fs.readFile(manifestPath, "utf8"));
const data = await fs.readFile(output);
manifest.artifacts["the-shape-of-judgment.pdf"] = {
  bytes: data.byteLength,
  sha256: createHash("sha256").update(data).digest("hex"),
};
await fs.writeFile(manifestPath, JSON.stringify(manifest, null, 2) + "\n");
console.log(`Rendered PDF (${stats.size} bytes)`);
