import { error, redirect } from '@sveltejs/kit';
import { BASE_URL } from '$lib/utils/constants.js';

export async function load({ params }) {
	let equipoUrl = new URL(BASE_URL + `/equipos/${params.id_equipo}`);

	const responseE = await fetch(equipoUrl);

	if (!responseE.ok) {
		error(`Response status: ${responseE.status}`);
	}

	let equipo = await responseE.json();
	let integrantes = equipo.integrantes;
	let integrante;

	integrantes.forEach((subintegrante) => {
		if (subintegrante.id === Number(params.id_integrante)) {
			integrante = subintegrante;
		}
	});

	let pokemonID = integrante.pokemon.id;
	let pokemonUrl = new URL(BASE_URL + `/pokemon/${pokemonID}`);

	const responseP = await fetch(pokemonUrl);

	if (!responseP.ok) {
		error(`Response status: ${responseP.status}`);
	}

	let pokemon = await responseP.json();
	let movimientosValidos = [
		pokemon.movimientos_huevo,
		pokemon.movimientos_maquina,
		pokemon.movimientos_nivel
	];

	return {
		equipo,
		integrante,
		movimientosValidos
	};
}

export const actions = {
	updateIntegrante: async ({ request }) => {
		const data = await request.formData();
		let equipo_id = data.get('equipo_id');
		let integrante_id = data.get('integrante_id');
		let mov1 = data.get('mov1');
		let mov2 = data.get('mov2');
		let mov3 = data.get('mov3');
		let mov4 = data.get('mov4');
		let apodo = data.get('apodo');

		const movimientos = [];
		if (mov1 != 0) {
			movimientos.push(mov1);
		}
		if (mov2 != 0) {
			movimientos.push(mov2);
		}
		if (mov3 != 0) {
			movimientos.push(mov3);
		}
		if (mov4 != 0) {
			movimientos.push(mov4);
		}

		let url = new URL(`${BASE_URL}/equipos/${equipo_id}/integrantes/${integrante_id}/`);

		const response = await fetch(url, {
			method: 'PUT',
			headers: { 'Content-Type': 'application/json' },
			body: JSON.stringify({
				apodo: apodo,
				movimientos: movimientos
			})
		});

		if (!response.ok) {
			error(response.status, 'No se pudo agregar el Integrante.');
		}
		redirect(303, `/equipos/${equipo_id}`);
	}
};
