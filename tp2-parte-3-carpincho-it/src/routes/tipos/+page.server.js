import { error } from '@sveltejs/kit';
import { BASE_URL } from '../../lib/utils/constants.js';

export async function load({ params }) {
	let url = new URL(BASE_URL + '/tipos');
	const response = await fetch(url);
	if (!response.ok) {
		error(response.status, 'Error fetching types');
	}

	let tipo = await response.json();
	return {
		tipo
	};
}
