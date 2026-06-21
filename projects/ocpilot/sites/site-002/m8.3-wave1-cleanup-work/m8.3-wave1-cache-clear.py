#!/usr/bin/env python3
"""BZPM M8.3 Wave 1 — clear OpenCart Twig cache on TEST."""
import ftplib

HOST = "polygonws.beget.tech"
FTP_USER = "polygonws_zpm"
FTP_PASS = "RT4uK7VKr&c"
CACHE_DIR = "system/storage/cache/template"


def clear_dir(ftp, cache_dir):
    cleared = []
    errors = []
    try:
        ftp.cwd(cache_dir)
        entries = []
        ftp.retrlines("LIST", entries.append)
        for line in entries:
            parts = line.split(None, 8)
            if len(parts) < 9:
                continue
            name = parts[8]
            if name in (".", "..", "index.html"):
                continue
            if line.startswith("d"):
                continue
            try:
                ftp.delete(name)
                cleared.append(f"{cache_dir}/{name}")
            except ftplib.error_perm as e:
                errors.append({"path": f"{cache_dir}/{name}", "error": str(e)})
    except Exception as e:
        errors.append({"path": cache_dir, "error": str(e)})
    return cleared, errors


def main():
    all_cleared = []
    all_errors = []
    for cache_dir in ("system/storage/cache", "system/storage/cache/template"):
        ftp = ftplib.FTP(HOST, timeout=120)
        ftp.login(FTP_USER, FTP_PASS)
        c, e = clear_dir(ftp, cache_dir)
        all_cleared.extend(c)
        all_errors.extend(e)
        ftp.quit()
    print({"cleared": len(all_cleared), "files": all_cleared[:20], "errors": all_errors})


if __name__ == "__main__":
    main()
