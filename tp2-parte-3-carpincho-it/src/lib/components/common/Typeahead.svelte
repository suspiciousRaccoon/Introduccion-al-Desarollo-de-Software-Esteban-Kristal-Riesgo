<script>
	import '$lib/styles/typeahead.css';
	import { onDestroy, createEventDispatcher } from 'svelte';

	const dispatch = createEventDispatcher();

	let { placeholder, endpoint, minQueryLength = 2, debounceTime = 300, queryKey } = $props();

	let query = $state('');
	let results = $state([]);
	let showDropdown = $state(false);
	let timeout;

	function onInput() {
		clearTimeout(timeout);
		if (query.length < minQueryLength) {
			results = [];
			showDropdown = false;
			return;
		}
		timeout = setTimeout(fetchResults, debounceTime);
	}

	async function fetchResults() {
		let url = new URL(endpoint);
		let params = { [queryKey]: query };

		url.search = new URLSearchParams(params).toString();

		const response = await fetch(url, {
			method: 'GET',
			headers: { 'Content-Type': 'application/json' }
		});
		if (!response.ok) {
			error(response.status, response);
		}

		results = await response.json();
		showDropdown = results.length > 0;
	}

	function selectResult(result) {
		query = '';
		showDropdown = false;
		dispatch('select', { result });
	}

	function handleBlur() {
		setTimeout(() => (showDropdown = false), 150);
	}

	onDestroy(() => clearTimeout(timeout));
</script>

<div class="typeahead-container">
	<input
		class="typeahead-input"
		type="text"
		bind:value={query}
		oninput={onInput}
		onblur={handleBlur}
		{placeholder}
		autocomplete="off"
	/>

	{#if showDropdown}
		<div class="dropdown">
			{#each results as result}
				<div
					class="dropdown-item"
					role="button"
					tabindex="0"
					onmousedown={() => selectResult(result)}
				>
					{result.nombre}, {result.apellido}
				</div>
			{/each}
		</div>
	{/if}
</div>
