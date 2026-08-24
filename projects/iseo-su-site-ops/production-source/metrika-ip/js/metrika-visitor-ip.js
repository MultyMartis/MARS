/**
 * ISEO-SU Metrika visitor IP param addon (fail-open, non-blocking).
 * Sends ym(COUNTER, 'params', { ipaddress: <server IP> }) once per page load.
 * Does not initialize Metrika, overwrite window.ym, or alter counter options.
 */
(function () {
  "use strict";

  if (window.__ISEO_METRIKA_VISITOR_IP_DONE) {
    return;
  }
  window.__ISEO_METRIKA_VISITOR_IP_DONE = true;

  var COUNTER_ID = 54287016;
  var ENDPOINT = "/metrika-visitor-ip.php";
  var YM_WAIT_MS = 200;
  var YM_WAIT_MAX = 25;

  function sendParams(ip) {
    if (typeof ym !== "function") {
      return false;
    }
    try {
      ym(COUNTER_ID, "params", { ipaddress: ip });
      return true;
    } catch (_e) {
      return false;
    }
  }

  function waitForYmThenSend(ip, left) {
    if (sendParams(ip)) {
      return;
    }
    if (left <= 0) {
      return;
    }
    setTimeout(function () {
      waitForYmThenSend(ip, left - 1);
    }, YM_WAIT_MS);
  }

  function onData(data) {
    if (!data || data.enabled !== true) {
      return;
    }
    var ip = data.ipaddress;
    if (typeof ip !== "string" || !ip) {
      return;
    }
    waitForYmThenSend(ip, YM_WAIT_MAX);
  }

  try {
    if (typeof fetch !== "function") {
      return;
    }
    fetch(ENDPOINT, {
      method: "GET",
      credentials: "same-origin",
      cache: "no-store",
      headers: { Accept: "application/json" },
    })
      .then(function (res) {
        if (!res || res.status === 204 || !res.ok) {
          return null;
        }
        return res.json();
      })
      .then(function (data) {
        onData(data);
      })
      .catch(function () {
        /* fail-open: page / Metrika continue unchanged */
      });
  } catch (_e) {
    /* fail-open */
  }
})();
