<script lang="ts">
	import '$lib/styles/pokemonCard.css';
	import type { PokemonTipo } from '$lib/utils/pokemon.interface';

	interface Props {
		id: number;
		nombre: string;
		imagen: string;
		tipos?: PokemonTipo[] | undefined;
	}
	let { id, nombre, imagen, tipos = undefined }: Props = $props();

	const nombreUpper = $derived(nombre.charAt(0).toUpperCase() + nombre.slice(1));
</script>

<a href={'/pokemon/' + String(id)} class="hoverable element pokemon-card">
	<h3>{nombreUpper}</h3>
	<img class="pokemon-img" src={imagen} alt={'imagen' + nombre} />

	<div>
		{#each tipos as tipo}
			<!-- https://github.com/partywhale/pokemon-type-icons -->
			<img class="img-icon" src="/vector/tipos/{tipo.nombre}.svg" alt={tipo.nombre} />
		{/each}
	</div>
</a>
