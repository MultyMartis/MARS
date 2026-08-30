# FriendHosting Build 01 rollback (pre-3X-UI checkpoint)
# Remote: /root/mars-backups/friendhosting-prebuild-20260829T174340Z.tgz
# SHA256: UNKNOWN
# Local: X:\AI MARS\local\infrastructure\FRIENDHOSTING-GERMANY\backups\friendhosting-prebuild-20260829T174340Z.tgz

Goal: return to Intake-01 clean pre-VPN baseline (no 3X-UI/Xray).

1. Preserve SSH :3333 at all times.
2. systemctl stop x-ui || true; systemctl disable x-ui || true
3. If withdrawing VPN only: remove UFW 8443 allow; keep 3333.
4. To restore pre-build host files from checkpoint:
   tar -C /root/mars-backups -xzf /root/mars-backups/friendhosting-prebuild-20260829T174340Z.tgz
   # Review etc-ssh before copying; do not blindly overwrite live sshd without session proof.
5. Optional full package rollback is NOT automatic — remove x-ui via official uninstall if installed:
   # bash <(curl -Ls https://raw.githubusercontent.com/mhsanaei/3x-ui/master/install.sh) uninstall   # ONLY if operator authorizes
6. Re-verify: ss -lntup shows :3333; :8443 free if VPN withdrawn; SSH login works.
