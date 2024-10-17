#/bin/bash
directorio="imagen"

hash_obj="e5ed313192776744b9b93b1320b5e268"

for archivo in "$directorio"/*; do
	hash_act=$(md5sum "$archivo" | awk '{print $1}')
	if [ "$hash_act" == "$hash_obj" ]; then
		echo "El archivo es: $archivo"
	fi
done
