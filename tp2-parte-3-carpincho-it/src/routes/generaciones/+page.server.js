import { error } from '@sveltejs/kit';
import { BASE_URL } from '../../lib/utils/constants.js';

export async function load({ params }) {
	let url = new URL(BASE_URL + '/generaciones');
	const response = await fetch(url);
	if (!response.ok) {
		error(response.status, 'Error fetching generations');
	}

	let generaciones = await response.json();
	return {
		generaciones
	};
}
