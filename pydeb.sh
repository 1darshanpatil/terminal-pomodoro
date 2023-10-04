#!/bin/bash

# Check if the script argument is provided
if [ "$#" -ne 1 ]; then
    echo "Usage: ./package.sh <python_script_name>"
    exit 1
fi

PYTHON_SCRIPT=$1
PACKAGE_NAME=$(basename "$PYTHON_SCRIPT" .py)

# 1. Organize the Python script
mkdir -p "$PACKAGE_NAME/usr/local/bin"
cp "$PYTHON_SCRIPT" "$PACKAGE_NAME/usr/local/bin/$PACKAGE_NAME"

# Make sure the script is executable
chmod +x "$PACKAGE_NAME/usr/local/bin/$PACKAGE_NAME"

# Add an icon
mkdir -p "$PACKAGE_NAME/usr/share/icons/hicolor/512x512/apps"
cp pomodoro.png "$PACKAGE_NAME/usr/share/icons/hicolor/512x512/apps/${PACKAGE_NAME}.png"

# Create a .desktop file
mkdir -p "$PACKAGE_NAME/usr/share/applications"
cat <<EOL > "$PACKAGE_NAME/usr/share/applications/${PACKAGE_NAME}.desktop"
[Desktop Entry]
Version=1.0
Name=Pomodoro Timer
Exec=gnome-terminal -- python3 /usr/local/bin/$PACKAGE_NAME
Icon=${PACKAGE_NAME}
Terminal=true
Type=Application
Categories=Utility;
EOL


# 2. Create Debian directory and control file
mkdir -p "$PACKAGE_NAME/DEBIAN"

cat <<EOL > "$PACKAGE_NAME/DEBIAN/control"
Package: $PACKAGE_NAME
Version: 1.0
Section: base
Priority: optional
Architecture: all
Maintainer: Your Name <youremail@example.com>
Description: Package created from $PYTHON_SCRIPT
EOL

# 3. Build the Debian package
dpkg-deb --build "$PACKAGE_NAME"

# Optional: Cleanup
rm -r "$PACKAGE_NAME"

echo "Done! Your Debian package is named ${PACKAGE_NAME}.deb"

