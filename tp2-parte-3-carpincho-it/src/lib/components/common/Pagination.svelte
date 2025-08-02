<script lang="ts">
	import { goto } from '$app/navigation';
	import { page } from '$app/stores';
	import { PAGINATION_SIZE } from '../../utils/constants';

	let { currentPage = 0, pageSize = PAGINATION_SIZE, hasMore = true } = $props();
	function goToPage(newPage) {
		const url = new URL($page.url);
		url.searchParams.set('page', newPage.toString());
		goto(url.toString());
	}

	function nextPage() {
		goToPage(currentPage + 1);
	}

	function prevPage() {
		goToPage(currentPage - 1);
	}
</script>

<div class="pagination">
	{#if currentPage > 0}
		<button onclick={prevPage} class="pagination-btn"> ← Anterior </button>
	{/if}

	<span class="page-info">
		Página {currentPage + 1}
	</span>

	{#if hasMore}
		<button onclick={nextPage} class="pagination-btn"> Siguiente → </button>
	{/if}
</div>
