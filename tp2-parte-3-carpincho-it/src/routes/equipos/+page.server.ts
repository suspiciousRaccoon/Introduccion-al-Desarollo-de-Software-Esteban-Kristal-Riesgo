import { BASE_URL } from '$lib/utils/constants.js';
import type { EquipoResumido } from '$lib/utils/equipo.interface.js';
import { error } from '@sveltejs/kit';

export async function load() {
	let url = new URL(BASE_URL + '/equipos/');
	const response = await fetch(url);
	if (!response.ok) {
		error(response.status, `Response status: ${response.status}`);
	}

	let equipos: EquipoResumido[] = await response.json();

	return {
		equipos
	};
}

export const actions = {
	create: async ({ cookies, request }) => {
		const data = await request.formData();

		let url = new URL(BASE_URL + '/equipos/');

		const nombre = data.get('nombre');
		const id_gen = Number(data.get('generaciones'));

		if (!nombre) {
			error(422, 'Debes poner un nombre para el equipo.');
		} else if (!id_gen) {
			error(422, 'Debes poner una generacion para el equipo.');
		}

		const response = await fetch(url, {
			method: 'POST',
			headers: { 'Content-Type': 'application/json' },
			body: JSON.stringify({
				nombre: nombre,
				id_generacion: id_gen
			})
		});

		if (!response.ok) {
			error(response.status, `Response status: ${response.status}`);
		}
	}
};
