<script lang="ts">
	import { enhance } from '$app/forms';
	import Pagination from '$lib/components/common/Pagination.svelte';
	import GeneracionFormSelect from '$lib/components/pokemon/GeneracionFormSelect.svelte';
	import PokemonCard from '$lib/components/pokemon/pokemonCard.svelte';
	import TipoFormSelect from '$lib/components/pokemon/TipoFormSelect.svelte';
	import '$lib/styles/pokemon.css';

	let { data } = $props();
</script>

<h1>Pokemons</h1>
<form action="?/filter" method="POST" use:enhance>
	<input
		name="nombreParcial"
		type="text"
		placeholder="Nombre Parcial"
		value={data.formInfo.nombreParcial}
	/>
	<TipoFormSelect tipo_id={data.formInfo.tipo} />
	<GeneracionFormSelect generacion_id={data.formInfo.generaciones} />

	<button>Filtrar</button>
	<button formaction="?/clear">Clear</button>
</form>

<div class="pokemon-grid">
	{#each data.pokemons as pokemon}
		<PokemonCard
			id={pokemon.id}
			imagen={pokemon.imagen}
			nombre={pokemon.nombre}
			tipos={pokemon.tipos}
		/>
	{/each}
</div>
<Pagination currentPage={data.currentPage} hasMore={data.hasMore} />
