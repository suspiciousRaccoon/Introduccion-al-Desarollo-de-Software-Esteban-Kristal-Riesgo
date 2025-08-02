#! /bin/bash

padron=$1
output_directory=$2

function find_filepath() {
  local file=$1

  local filepath=$(find . -name $1)
  echo $filepath
}

##### DATA FILEPATHS #####
pokemon_stats="$(find_filepath "pokemon_stats.csv")"
pokemon_types="$(find_filepath "pokemon_types.csv")"
pokemon_gen_data="$(find_filepath "pokemon.csv")"

#### FILTERS ####
pokemon_filter_type=$((($padron % 18) + 1))
pokemon_filter_stat=$((($padron % 100) + 350))

# Filter by type
pokemon_ids_with_type=()
ignore_first_line=1

while IFS=, read -r id type_id _slot; do
  if [[ $ignore_first_line -eq 1 ]]; then
    ignore_first_line=0
    continue
  fi

  if [[ $type_id -eq $pokemon_filter_type ]]; then
    pokemon_ids_with_type+=(${id})
  fi
done <"$pokemon_types"

# Filter by stat amount

pokemon_ids_with_min_stat=()

for pokemon_id in ${pokemon_ids_with_type[@]}; do 
  stats=$(grep "^$pokemon_id," $pokemon_stats | cut -d "," -f3)
  total=0
  
  for stat in ${stats[@]}; do
    total=$(($total+$stat))
  done

  if [[ $total -ge $pokemon_filter_stat ]]; then
    pokemon_ids_with_min_stat+=($pokemon_id)
  fi
done

# Names
ignore_first_line=1
pokemon_names=()
current_index=0

while IFS=, read -r id identifier _species_id _height _weight _base_experience _order _is_default; do
  if [[ $ignore_first_line -eq 1 ]]; then
    ignore_first_line=0
    continue
  fi

  if [[ $id -eq ${pokemon_ids_with_min_stat[current_index]} ]]; then
    pokemon_names+=($identifier)
    current_index=$(($current_index + 1))
  fi
done <"$pokemon_gen_data"

# OUTPUT
mkdir -p $output_directory
rm -f "$output_directory/resultado.txt"
touch "$output_directory/resultado.txt"

for name in ${pokemon_names[@]}; do
  echo $name >>"$output_directory/resultado.txt"
done
