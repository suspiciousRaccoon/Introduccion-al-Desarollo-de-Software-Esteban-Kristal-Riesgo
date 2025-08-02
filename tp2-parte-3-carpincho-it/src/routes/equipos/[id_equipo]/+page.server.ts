import { page } from '$app/state';
import { BASE_URL } from '$lib/utils/constants.js';
import type { Equipo } from '$lib/utils/equipo.interface.js';
import { error, redirect } from '@sveltejs/kit';
import type { Actions } from '../$types.js';

export async function load({ params }) {
	let equipoUrl = new URL(BASE_URL + `/equipos/${params.id_equipo}`);
	const response = await fetch(equipoUrl);

	if (!response.ok) {
		error(response.status, `Response status: ${response.status}`);
	}

	let equipo: Equipo = await response.json();
	return {
		equipo
	};
}

export const actions = {
	editarEquipo: async ({ request, fetch, params }) => {
		const data = await request.formData();
		const nombre = data.get('nombre');
		const generacion_id = data.get('generaciones'); // ugly param due to GeneracionSelectForm component
		const equipo_id = params.id_equipo;

		let apiUrl = new URL(BASE_URL + `/equipos/${equipo_id}`);

		const response = await fetch(apiUrl, {
			method: 'PUT',
			headers: { 'Content-Type': 'application/json' },
			body: JSON.stringify({
				nombre: nombre,
				id_generacion: generacion_id
			})
		});

		if (!response.ok) {
			error(response.status, response.statusText);
		}
		redirect(303, '/equipos/' + equipo_id);
	},

	deleteIntegrante: async ({ request }) => {
		const data = await request.formData();
		const equipo = data.get('equipo_id');
		const integrante = data.get('integrante_id');

		let url = new URL(BASE_URL + `/equipos/${equipo}/integrantes/${integrante}/`);

		const response = await fetch(url, {
			method: 'DELETE',
			headers: { 'Content-Type': 'application/json' }
		});

		if (!response.ok) {
			error(response.status, 'Algo falló');
		}
	},

	deleteEquipo: async ({ request }) => {
		const data = await request.formData();
		const equipo = data.get('equipo_id');

		let url = new URL(BASE_URL + `/equipos/${equipo}/`);

		const response = await fetch(url, {
			method: 'DELETE',
			headers: { 'Content-Type': 'application/json' }
		});

		if (!response.ok) {
			error(response.status, 'Algo falló');
		} else {
			redirect(303, '/equipos');
		}
	},

	agregarIntegrante: async ({ request, params }) => {
		const data = await request.formData();
		const equipo_id = params.id_equipo;
		let id_pokemon = data.get('id_pokemon');
		let apodo = data.get('apodo');

		if (!id_pokemon) {
			error(422, 'El Pokemon no es válido.');
		} else if (!apodo) {
			error(422, 'Tenés que ingresar un apodo válido.');
		}

		let url = new URL(BASE_URL + `/equipos/${equipo_id}/integrantes/`);

		const response = await fetch(url, {
			method: 'POST',
			headers: { 'Content-Type': 'application/json' },
			body: JSON.stringify({
				id_pokemon: id_pokemon,
				apodo: apodo
			})
		});

		if (!response.ok) {
			const errorData = await response.json();

			error(response.status, `No se pudo agregar el Integrante: ${errorData.detail}`);
		}
		redirect(303, `/equipos/${equipo_id}`);
	}
} satisfies Actions;
