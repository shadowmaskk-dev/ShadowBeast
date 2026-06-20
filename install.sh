#!/data/data/com.termux/files/usr/bin/bash

echo "[ShadowBeast] Installing..."

# Ensure python exists
pkg install python -y

# Optional: upgrade pip
pip install --upgrade pip

# Install dependencies if requirements exist
if [ -f requirements.txt ]; then
    pip install -r requirements.txt
fi

# Create global command
cat > $PREFIX/bin/shadowbeast << 'EOF'
#!/data/data/com.termux/files/usr/bin/bash
cd "$HOME/shadowbeast-assistant" || exit
python main.py
EOF

chmod +x $PREFIX/bin/shadowbeast

echo "[ShadowBeast] Installation complete."
echo "Run: shadowbeast"
