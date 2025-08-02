import type { Generacion, MovimientoResumido, PokemonResumido } from './pokemon.interface.js';

export interface Integrante {
	id: number;
	apodo: string;
	pokemon: PokemonResumido;
	movimientos: MovimientoResumido[];
}

export interface Equipo {
	id: number;
	nombre: string;
	generacion: Generacion;
	integrantes: Integrante[];
}

export interface EquipoResumido {
	id: number;
	nombre: string;
	generacion: Generacion;
	cant_integrantes: number;
}
