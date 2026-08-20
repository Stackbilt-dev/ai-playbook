import fs from "node:fs/promises";
import path from "node:path";
import { execFile } from "node:child_process";
import { promisify } from "node:util";
import { fileURLToPath, pathToFileURL } from "node:url";

const execFileAsync = promisify(execFile);
const here = path.dirname(fileURLToPath(import.meta.url));
const outputRoot = path.join(here, "exports");
const candidates = [process.env.CHROME_PATH, "/usr/bin/google-chrome", "/usr/bin/chromium", "/usr/bin/chromium-browser"].filter(Boolean);
let chrome;
for (const candidate of candidates) { try { await fs.access(candidate); chrome = candidate; break; } catch {} }
if (!chrome) throw new Error("Chrome or Chromium was not found. Set CHROME_PATH to a browser executable.");

const source = path.join(outputRoot, "the-shape-of-judgment-linkedin.html");
const output = path.join(outputRoot, "the-shape-of-judgment-linkedin.pdf");
await execFileAsync(chrome, ["--headless=new", "--disable-gpu", "--no-sandbox", "--no-pdf-header-footer", "--run-all-compositor-stages-before-draw", `--print-to-pdf=${output}`, pathToFileURL(source).href]);
const stats = await fs.stat(output);
if (stats.size < 100_000) throw new Error(`LinkedIn PDF is unexpectedly small (${stats.size} bytes)`);
console.log(`Rendered LinkedIn PDF (${stats.size} bytes).`);
