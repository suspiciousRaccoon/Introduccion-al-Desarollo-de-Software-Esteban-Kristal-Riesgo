#! /bin/bash

function find_filepath() {
  local file=$1

  local filepath=$(find . -name $1)
  echo $filepath
}

pokemon_gen_data="$(find_filepath "pokemon.csv")"
pokemon_abilities="$(find_filepath "pokemon_abilities.csv")"
pokemon_ability_names="$(find_filepath "ability_names.csv")"

while read name; do
  # doesn't validate that the pokemon name exists
  # breaks if used with a pokemon name not present in pokemon.csv

  height=$(($(grep -m 1 -w "$name" $pokemon_gen_data | cut -d "," -f4) * 10))
  weight=$(($(grep -m 1 -w "$name" $pokemon_gen_data | cut -d "," -f5) / 10))
  pokemon_id=$(grep -m 1 -w "$name" $pokemon_gen_data | cut -d "," -f1)
  ability_ids=()

  ignore_first_line=1
  while IFS=, read -r id ability_id _is_hidden _slot; do
    if [[ $ignore_first_line -eq 1 ]]; then
      ignore_first_line=0
      continue
    fi

    if [[ $id -eq $pokemon_id ]]; then
      ability_ids+=($ability_id)
    fi

  done <"$pokemon_abilities"

  echo "---------------------"
  echo "Pokemon: $name"
  echo "Altura: $height centimetros"
  echo "Peso: $weight kilos"
  echo ""
  echo "Habilidades"
  for ability_id in ${ability_ids[@]}; do
    echo " * $(grep "^$ability_id,7" $pokemon_ability_names | cut -d "," -f3)"
  done
  echo "---------------------"

done </dev/stdin
