#!/bin/bash

# Definir variables
SRC="$HOME/Escritorio/Seguridad"
DEST="bruno.izaguspruebalabo@34.175.143.152:/var/tmp/Backups"
LINK_DEST="../$(date -d 'yesterday' +%d-%m-%Y)" # Copia de ayer
TODAY=$(date +%d-%m-%Y) # Fecha de hoy
BACKUP_DIR="$DEST/$TODAY"

echo "Fuente: $SRC"
echo "Destino: $BACKUP_DIR"
echo "Copia incremental basada en: $LINK_DEST"

# Comprobar si existe la copia de ayer para hacer una copia incremental
if [ -d "$LINK_DEST" ]; then
    echo "Copia incremental desde $LINK_DEST"
    rsync -av --link-dest="$LINK_DEST" "$SRC/" "$BACKUP_DIR/"
else
    echo "Copia completa"
    rsync -av "$SRC/" "$BACKUP_DIR/"
fi
