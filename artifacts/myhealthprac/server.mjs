import express from "express";
import path from "node:path";
import { fileURLToPath } from "node:url";

const __dirname = path.dirname(fileURLToPath(import.meta.url));

const rawPort = process.env.PORT;
if (!rawPort) {
  throw new Error("PORT environment variable is required");
}
const port = Number(rawPort);
if (Number.isNaN(port) || port <= 0) {
  throw new Error(`Invalid PORT value: "${rawPort}"`);
}

const basePath = process.env.BASE_PATH || "/";
const staticDir = path.join(__dirname, "static");

const app = express();

app.disable("etag");
app.use((_req, res, next) => {
  if (process.env.NODE_ENV !== "production") {
    res.setHeader("Cache-Control", "no-store, max-age=0");
  }
  next();
});

const staticOptions = {
  extensions: ["html"],
  index: ["index.html"],
  fallthrough: true,
  setHeaders: (res, filePath) => {
    if (filePath.endsWith(".avif")) res.setHeader("Content-Type", "image/avif");
    if (filePath.endsWith(".js") && !filePath.endsWith(".min.js")) {
      res.setHeader("Content-Type", "application/javascript; charset=utf-8");
    }
  },
};

const mountPath = basePath === "/" ? "/" : basePath.replace(/\/$/, "");

if (mountPath === "/") {
  app.use(express.static(staticDir, staticOptions));
} else {
  app.use(mountPath, express.static(staticDir, staticOptions));
}

app.use((req, res) => {
  res.status(404).type("text/plain").send("Not Found");
});

app.listen(port, "0.0.0.0", () => {
  console.log(`Static site server listening on 0.0.0.0:${port} (base ${basePath})`);
});
