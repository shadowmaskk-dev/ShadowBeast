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

Create launcher

cat > "$PREFIX/bin/shadowbeast" << EOF
#!/data/data/com.termux/files/usr/bin/bash

cd "$PROJECT_DIR"
python main.py "$@"
EOF

Make launcher executable

chmod +x "$PREFIX/bin/shadowbeast"

echo
echo "[ShadowBeast] Installation complete."
echo "You can now run ShadowBeast from anywhere using:"
echo
echo "    shadowbeast"
echo
