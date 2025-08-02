import { BASE_URL } from '$lib/utils/constants.js';
import type { Movimiento } from '$lib/utils/movimiento.interface.ts';
import { error, type ServerLoad } from '@sveltejs/kit';

export const load: ServerLoad = async ({ params, fetch }) => {
	const res = await fetch(`${BASE_URL}/movimientos/${params.id}`);
	if (!res.ok) {
		throw error(res.status, 'No se pudo obtener el movimiento');
	}

	const movimiento: Movimiento = await res.json();
	return { movimiento };
};
