#!/data/data/com.termux/files/usr/bin/bash

echo "[ShadowBeast] Installing..."

Update package lists

pkg update -y

Install required packages

pkg install -y python git

Install Python dependencies

pip install -r requirements.txt

Save project location

PROJECT_DIR="$(pwd)"

Create 'shadowbeast' launcher

cat > "$PREFIX/bin/shadowbeast" << EOF
#!/data/data/com.termux/files/usr/bin/bash

cd "$PROJECT_DIR" || exit
python main.py "$@"
EOF

chmod +x "$PREFIX/bin/shadowbeast"

Create short 'sb' launcher

cat > "$PREFIX/bin/sb" << EOF
#!/data/data/com.termux/files/usr/bin/bash

cd "$PROJECT_DIR" || exit
python main.py "$@"
EOF

chmod +x "$PREFIX/bin/sb"

echo
echo "[ShadowBeast] Installation complete."
echo
echo "You can now run ShadowBeast from anywhere using:"
echo
echo "    shadowbeast"
echo "    sb"
echo
