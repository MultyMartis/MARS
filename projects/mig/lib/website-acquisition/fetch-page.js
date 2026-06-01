"use strict";

const fs = require("fs");
const path = require("path");

const DEFAULT_USER_AGENT =
  "MIG-Website-Acquisition/0.1 (+https://mars.local; research-capture; no-crawl)";

function pickHeadersSubset(headers) {
  const allow = [
    "content-type",
    "content-length",
    "location",
    "server",
    "cache-control",
    "x-robots-tag",
  ];
  const out = {};
  if (!headers) {
    return out;
  }
  for (const key of allow) {
    const value = headers.get ? headers.get(key) : headers[key];
    if (value) {
      out[key] = value;
    }
  }
  return out;
}

function classifyHttpOutcome(status) {
  if (status >= 200 && status < 300) {
    return "success";
  }
  if (status === 403 || status === 429 || status === 451) {
    return "blocked";
  }
  if (status >= 500) {
    return "failed";
  }
  if (status >= 400) {
    return "failed";
  }
  return "failed";
}

async function fetchWithRedirects(url, options = {}) {
  const maxRedirects = options.maxRedirects ?? 5;
  const timeoutMs = options.timeoutMs ?? 30000;
  const redirectChain = [];
  let currentUrl = url;

  for (let hop = 0; hop <= maxRedirects; hop += 1) {
    const controller = new AbortController();
    const timer = setTimeout(() => controller.abort(), timeoutMs);
    const started = Date.now();

    try {
      const response = await fetch(currentUrl, {
        method: "GET",
        redirect: "manual",
        signal: controller.signal,
        headers: {
          "user-agent": options.userAgent || DEFAULT_USER_AGENT,
          accept: "text/html,application/xhtml+xml;q=0.9,*/*;q=0.8",
          "accept-language": "ru,en;q=0.8",
        },
      });
      clearTimeout(timer);

      const durationMs = Date.now() - started;
      const status = response.status;
      const headers = pickHeadersSubset(response.headers);
      const contentType = response.headers.get("content-type");

      if (status >= 300 && status < 400) {
        const location = response.headers.get("location");
        if (!location || hop >= maxRedirects) {
          return {
            ok: false,
            status: "failed",
            http_status: status,
            final_url: currentUrl,
            redirect_chain: redirectChain,
            headers,
            content_type: contentType,
            body: "",
            duration_ms: durationMs,
            error: location ? "redirect_limit_exceeded" : "redirect_missing_location",
          };
        }
        const nextUrl = new URL(location, currentUrl).href;
        redirectChain.push(currentUrl);
        currentUrl = nextUrl;
        continue;
      }

      const body = await response.text();
      const outcome = classifyHttpOutcome(status);

      return {
        ok: outcome === "success",
        status: outcome,
        http_status: status,
        final_url: currentUrl,
        redirect_chain: redirectChain,
        headers,
        content_type: contentType,
        body,
        duration_ms: durationMs,
        error: outcome === "success" ? null : `http_${status}`,
      };
    } catch (err) {
      clearTimeout(timer);
      const isTimeout = err.name === "AbortError";
      return {
        ok: false,
        status: isTimeout ? "timeout" : "failed",
        http_status: null,
        final_url: currentUrl,
        redirect_chain: redirectChain,
        headers: {},
        content_type: null,
        body: "",
        duration_ms: Date.now() - started,
        error: isTimeout ? "timeout" : err.message,
      };
    }
  }

  return {
    ok: false,
    status: "failed",
    http_status: null,
    final_url: currentUrl,
    redirect_chain: redirectChain,
    headers: {},
    content_type: null,
    body: "",
    duration_ms: 0,
    error: "redirect_limit_exceeded",
  };
}

/**
 * Fetch page — HTTP GET or fixture file for tests.
 * @param {string} url
 * @param {{ fixtureRoot?: string, fixtureMap?: Record<string,string>, timeoutMs?: number, maxRedirects?: number }} [options]
 */
async function fetchPage(url, options = {}) {
  if (options.fixtureMap) {
    const fixtureKey = options.fixtureMap[url] || options.fixtureMap["*"];
    if (fixtureKey) {
      const fixturePath = path.isAbsolute(fixtureKey)
        ? fixtureKey
        : path.join(options.fixtureRoot || "", fixtureKey);
      const body = fs.readFileSync(fixturePath, "utf8");
      return {
        ok: true,
        status: "success",
        http_status: 200,
        final_url: url,
        redirect_chain: [],
        headers: { "content-type": "text/html; charset=utf-8" },
        content_type: "text/html; charset=utf-8",
        body,
        duration_ms: 1,
        error: null,
        acquisition_method: "fixture",
      };
    }
  }

  const result = await fetchWithRedirects(url, options);
  return {
    ...result,
    acquisition_method: "http_get",
  };
}

module.exports = {
  fetchPage,
  fetchWithRedirects,
  classifyHttpOutcome,
  DEFAULT_USER_AGENT,
};
