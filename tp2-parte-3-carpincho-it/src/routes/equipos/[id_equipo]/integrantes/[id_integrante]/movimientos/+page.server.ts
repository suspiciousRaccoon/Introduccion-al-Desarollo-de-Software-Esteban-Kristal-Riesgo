import { BASE_URL } from '$lib/utils/constants';
import { error, redirect, type ServerLoad, type Actions } from '@sveltejs/kit';
import type { Movimiento } from '$lib/utils/movimiento.interface';

export const load: ServerLoad = async ({ url, fetch, params }) => {
	const { id_equipo, id_integrante } = params;
	const nombreParcial = url.searchParams.get('nombre_parcial');

	const resIntegrante = await fetch(
		`${BASE_URL}/equipos/${id_equipo}/integrantes/${id_integrante}`
	);
	if (!resIntegrante.ok) throw error(resIntegrante.status, 'No se pudo cargar el integrante');
	const integrante = await resIntegrante.json();

	let movimientosUrl = new URL(`${BASE_URL}/pokemon/${integrante.pokemon.id}/movimientos`);
	if (nombreParcial) {
		movimientosUrl.searchParams.set('nombre_parcial', nombreParcial);
	}
	const resMovimientos = await fetch(movimientosUrl);
	if (!resMovimientos.ok)
		throw error(resMovimientos.status, 'No se pudieron cargar los movimientos');
	const movimientos: Movimiento[] = await resMovimientos.json();

	return {
		integrante,
		movimientos,
		formInfo: { nombreParcial }
	};
};

export const actions: Actions = {
	guardar: async ({ request, params }) => {
		const data = await request.formData();
		const mov_ids = data.getAll('movimientos').map((id) => Number(id));
		const { id_equipo, id_integrante } = params;

		if (mov_ids.length > 4) {
			throw error(400, 'No se pueden seleccionar más de 4 movimientos');
		}

		for (const id_movimiento of mov_ids) {
			const res = await fetch(
				`${BASE_URL}/equipos/${id_equipo}/integrantes/${id_integrante}/movimientos`,
				{
					method: 'POST',
					headers: { 'Content-Type': 'application/json' },
					body: JSON.stringify({ id_movimiento })
				}
			);

			if (!res.ok && res.status !== 409) {
				throw error(res.status, `Error agregando movimiento ${id_movimiento}`);
			}
		}

		throw redirect(303, `/equipos/${id_equipo}`);
	},

	filter: async ({ request, url }) => {
		const data = await request.formData();
		const nombreParcial = data.get('nombreParcial');

		if (nombreParcial) {
			url.searchParams.set('nombre_parcial', nombreParcial.toString());
		}

		throw redirect(303, url);
	}
};
