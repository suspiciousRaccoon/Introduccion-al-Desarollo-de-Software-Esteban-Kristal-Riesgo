export interface Generacion {
	id: number;
	nombre: string;
}

export interface Evolucion {
	id: number;
	nombre: string;
	imagen: string;
}

export interface Tipo {
	id: number;
	nombre: string;
}

export interface PokemonTipo {
	id: number;
	nombre: string;
	debilidades: Tipo[];
}

export interface Habilidad {
	id: number;
	nombre: string;
}

export interface Estadistica {
	ataque: number;
	defensa: number;
	ataque_especial: number;
	defensa_especial: number;
	puntos_de_golpe: number;
	velocidad: number;
}

export interface MovimientoResumido {
	id: number;
	nombre: string;
	categoria: string;
	potencia: number;
	precision: number;
	puntos_de_poder: number;
	efecto: string;
	generacion: Generacion;
	tipo: Tipo;
}

export interface Pokemon {
	id: number;
	nombre: string;
	altura: number;
	peso: number;
	generaciones: Generacion[];
	tipos: PokemonTipo[];
	habilidades: Habilidad[];
	estadisticas: Estadistica;
	evoluciones: Evolucion[];
	movimientos_huevo: MovimientoResumido[];
	movimientos_maquina: MovimientoResumido[];
	movimientos_nivel: MovimientoResumido[];
	imagen: string;
}

export interface PokemonResumido {
	id: number;
	nombre: string;
	imagen: string;
}
