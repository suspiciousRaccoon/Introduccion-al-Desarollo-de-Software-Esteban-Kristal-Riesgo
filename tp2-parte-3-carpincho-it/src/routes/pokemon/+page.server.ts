import { BASE_URL, PAGINATION_SIZE } from '$lib/utils/constants.js';
import { get_page, set_page } from '$lib/utils/fetch.js';
import type { Pokemon } from '$lib/utils/pokemon.interface.js';
import { error, redirect, type Actions } from '@sveltejs/kit';
import type { PageServerLoad, RequestEvent } from '../$types.js';

export const load: PageServerLoad = async ({ url, fetch }) => {
	let apiUrl = new URL(BASE_URL + '/pokemon');
	const page = parseInt(get_page(url));
	apiUrl = set_page(apiUrl, url);

	const tipo = url.searchParams.get('tipo');
	const generaciones = url.searchParams.get('generaciones');
	const nombreParcial = url.searchParams.get('nombre_parcial');

	if (tipo) {
		apiUrl.searchParams.set('tipo', tipo);
	}
	if (generaciones) {
		apiUrl.searchParams.set('generaciones', generaciones);
	}
	if (nombreParcial) {
		apiUrl.searchParams.set('nombre_parcial', nombreParcial);
	}

	const response = await fetch(apiUrl);
	if (!response.ok) {
		error(response.status, `Response status: ${response.status}`);
	}

	const data: Pokemon[] = await response.json();
	const hasMore = data.length === PAGINATION_SIZE;
	const formInfo = { nombreParcial, generaciones: generaciones ?? 0, tipo: tipo ?? 0 };
	return {
		pokemons: data,
		currentPage: page,
		pageSize: PAGINATION_SIZE,
		hasMore: hasMore,
		formInfo: formInfo
	};
};

export const actions = {
	filter: async ({ request, url }) => {
		const data = await request.formData();
		const tipo = data.get('tipo');
		const generaciones = data.get('generaciones');
		const nombreParcial = data.get('nombreParcial');

		if (tipo && tipo !== '0') {
			url.searchParams.set('tipo', tipo.toString());
		}
		if (generaciones && generaciones !== '0') {
			url.searchParams.set('generaciones', generaciones.toString());
		}
		if (nombreParcial) {
			url.searchParams.set('nombre_parcial', nombreParcial.toString());
		}
		console.log(url.href);
		console.log(nombreParcial);

		redirect(303, url);
	},
	clear: async function (_event: RequestEvent) {
		redirect(303, '/pokemon');
	}
} satisfies Actions;
