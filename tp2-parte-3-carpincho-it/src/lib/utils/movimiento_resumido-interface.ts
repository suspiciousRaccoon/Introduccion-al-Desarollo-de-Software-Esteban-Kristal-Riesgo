import type { Movimiento as MovimientoBase } from './movimiento.interface.ts';
import type { PokemonResumido } from './pokemon.interface.ts';

export interface Movimiento extends MovimientoBase {
	pokemon_por_nivel: PokemonResumido[];
	pokemon_por_huevo: PokemonResumido[];
	pokemon_por_maquina: PokemonResumido[];
}
