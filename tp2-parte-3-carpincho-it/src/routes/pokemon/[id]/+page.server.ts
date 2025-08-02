import { BASE_URL } from '$lib/utils/constants.js';
import type { Pokemon } from '$lib/utils/pokemon.interface.js';
import { error } from '@sveltejs/kit';
import type { PageServerLoad } from './$types.js';

export const load: PageServerLoad = async ({ params, fetch }) => {
	const apiUrl = new URL(BASE_URL + '/pokemon/' + params.id);
	const response = await fetch(apiUrl);
	if (!response.ok) {
		error(response.status, `Response status: ${response.status}`);
	}

	const data: Pokemon = await response.json();

	return { pokemon: data };
};
