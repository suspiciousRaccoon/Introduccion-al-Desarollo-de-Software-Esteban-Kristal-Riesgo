import { PAGINATION_SIZE } from './constants.js';

// returns the page inside the url query param or 0 if not found
export function get_page(url: URL): string {
	return url.searchParams.get('page') || '0';
}

export function set_page(apiUrl: URL, svelteUrl: URL): URL {
	const page = svelteUrl.searchParams.get('page') || '0';

	const pageSize = PAGINATION_SIZE;
	const offset = parseInt(page) * pageSize;
	apiUrl.searchParams.set('limit', pageSize.toString());
	apiUrl.searchParams.set('offset', offset.toString());

	return apiUrl;
}
