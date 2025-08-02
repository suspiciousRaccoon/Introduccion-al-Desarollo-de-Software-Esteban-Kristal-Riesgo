export interface Tipo {
	id: number;
	nombre: string;
}

export interface Generacion {
	id: number;
	nombre: string;
}

export interface Movimiento {
	id: number;
	nombre: string;
	categoria: string;
	potencia: number | null;
	precision: number | null;
	puntos_de_poder: number;
	efecto: string;
	tipo: Tipo;
	generacion: Generacion;
}
