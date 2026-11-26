#!/bin/bash
# usage: mk.sh index22.html 21 37   (html, versionName, versionCode)
set -e
cd "$(dirname "$0")"
cp "$1" proj/assets/index.html
sed -i "s/versionCode: .*/versionCode: '$3'/; s/versionName: .*/versionName: '$2'/" proj/apktool.yml
rm -f X.apk un.apk; rm -rf sg
java -jar apktool.jar b proj -o X.apk >/dev/null 2>&1
python3 - <<PY
import zipfile
zi=zipfile.ZipFile('X.apk');zo=zipfile.ZipFile('un.apk','w',zipfile.ZIP_DEFLATED)
for i in zi.infolist():
    if i.filename.startswith('META-INF/'):continue
    zo.writestr(i,zi.read(i.filename),compress_type=i.compress_type)
zo.close()
PY
java -jar uber.jar -a un.apk --allowResign -o sg >/dev/null 2>&1
f=$(ls sg/*.apk|head -1); cp "$f" /home/claude/Baitul-Mamur-v$2.apk
java -jar uber.jar -y "$f" 2>&1 | grep -i "verified\|sha256" | head -3
cp /home/claude/Baitul-Mamur-v$2.apk /home/claude/masjid-backup/; cp "$1" /home/claude/masjid-backup/
mkdir -p /mnt/user-data/outputs/masjid-backup; cp /home/claude/Baitul-Mamur-v$2.apk "$1" /mnt/user-data/outputs/masjid-backup/
ls -la /home/claude/Baitul-Mamur-v$2.apk
