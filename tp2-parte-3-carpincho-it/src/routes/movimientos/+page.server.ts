import { BASE_URL, PAGINATION_SIZE } from '$lib/utils/constants.js';
import { get_page, set_page } from '$lib/utils/fetch.js';
import type { Movimiento } from '$lib/utils/movimiento.interface.ts';
import { error, redirect } from '@sveltejs/kit';
import type { Actions, RequestEvent, ServerLoad } from '@sveltejs/kit';

export const load: ServerLoad = async ({ url, fetch }) => {
	let apiUrl = new URL(BASE_URL + '/movimientos');
	const page = parseInt(get_page(url));
	apiUrl = set_page(apiUrl, url);

	const tipo = url.searchParams.get('tipo');
	const nombreParcial = url.searchParams.get('nombre_parcial');

	if (tipo && tipo !== '0') {
		apiUrl.searchParams.set('tipo', tipo);
	}
	if (nombreParcial) {
		apiUrl.searchParams.set('nombre_parcial', nombreParcial);
	}

	const response = await fetch(apiUrl);
	if (!response.ok) {
		error(response.status, `Error fetching movimientos`);
	}

	const data: Movimiento[] = await response.json();
	const hasMore = data.length === PAGINATION_SIZE;
	const formInfo = { nombreParcial, tipo: tipo ?? 0 };

	return {
		movimientos: data,
		currentPage: page,
		pageSize: PAGINATION_SIZE,
		hasMore,
		formInfo
	};
};

export const actions = {
	filter: async ({ request, url }) => {
		const data = await request.formData();
		const tipo = data.get('tipo');
		const nombreParcial = data.get('nombreParcial');

		if (tipo && tipo !== '0') {
			url.searchParams.set('tipo', tipo.toString());
		}
		if (nombreParcial) {
			url.searchParams.set('nombre_parcial', nombreParcial.toString());
		}

		return redirect(303, url);
	}
} satisfies Actions;
