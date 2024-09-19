#!/bin/bash

# Set up working environment
cd "$(dirname "$0")" || exit 1
CWD=$(pwd)
VERSION="2024.9.20"
PRGNAM="orthodox_web-media"
BUILD_DIR="orthodox_build"

# Enable strict error handling
set -e
trap "rm -rf '$CWD/$BUILD_DIR'; echo 'Installation interrupted. Cleaned up temporary files.'; exit 1" INT TERM ERR

# Create working directory
mkdir -p "$CWD/$BUILD_DIR"
cd "$CWD/$BUILD_DIR" || exit 1
echo "Created $BUILD_DIR"

# Download source
echo "Downloading $PRGNAM-$VERSION.tar.gz"
wget -qc https://github.com/rizitis/"$PRGNAM"/archive/refs/tags/"$VERSION".tar.gz

# Unpack source
echo "Extracting source code"
tar -xvzf "$VERSION".tar.gz

# Navigate to source directory
cd "$PRGNAM"-"$VERSION" || exit 1

# List media players
totem="totem_orthodox"
mpv="mpv_orthodox"
vlc="vlc_orthodox"

# Prompt the user for media player choice
echo "Choose your preferred media player:"
echo "1. VLC"
echo "2. MPV"
echo "3. Totem"

# Read and validate user input
while true; do
  read -p "Enter your choice (1-3): " choice
  case $choice in
    1) player="$vlc" ;;
    2) player="$mpv" ;;
    3) player="$totem" ;;
    *) echo "Invalid choice. Please enter 1, 2, or 3." ;;
  esac
  [[ $choice -ge 1 && $choice -le 3 ]] && break
done

# Install the selected player
echo "Installing $player..."
sudo cat ./opt/"$player".py > /opt/"$player".py
sudo cat ./usr/share/applications/"$player".desktop > /usr/share/applications/"$player".desktop
sudo cp -r ./usr/share/"$PRGNAM" /usr/share/

# Clean up working directory
echo "Cleaning up working directory..."
cd "$CWD" || exit 1
rm -rf "$BUILD_DIR"
echo "Installation completed successfully."


cat << "EOF"


   ____     ______     ________   __    __     ____     ______       ____
  / __ \   (   __ \   (___  ___) (  \  /  )   / __ \   (_  __ \     / __ \
 / /  \ \   ) (__) )      ) )     \ (__) /   / /  \ \    ) ) \ \   / /  \ \
( ()  () ) (    __/      ( (       ) __ (   ( ()  () )  ( (   ) ) ( ()  () )
( ()  () )  ) \ \  _      ) )     ( (  ) )  ( ()  () )   ) )  ) ) ( ()  () )
 \ \__/ /  ( ( \ \_))    ( (       ) )( (    \ \__/ /   / /__/ /   \ \__/ /
  \____/    )_) \__/     /__\     /_/  \_\    \____/   (______/     \____/

 __     __                 ___       ___    _____   ______
(_ \   / _)               (  (       )  )  / ___/  (_   _ \
  \ \_/ /                  \  \  _  /  /  ( (__      ) (_) )  ________
   \   /                    \  \/ \/  /    ) __)     \   _/  (________)
   / _ \                     )   _   (    ( (        /  _ \
 _/ / \ \_   ___________     \  ( )  /     \ \___   _) (_) )
(__/   \__) |___________|     \_/ \_/       \____\ (______/

   __    __      _____   ______      _____     ____
   \ \  / /     / ___/  (_  __ \    (_   _)   (    )
   () \/ ()    ( (__      ) ) \ \     | |     / /\ \
   / _  _ \     ) __)    ( (   ) )    | |    ( (__) )
  / / \/ \ \   ( (        ) )  ) )    | |     )    (
 /_/      \_\   \ \___   / /__/ /    _| |__  /  /\  \
(/          \)   \____\ (______/    /_____( /__(  )__\

EOF
echo "ΖΕΙ ΚΥΡΙΟΣ Ο ΘΕΟΣ ΗΜΩΝ"
