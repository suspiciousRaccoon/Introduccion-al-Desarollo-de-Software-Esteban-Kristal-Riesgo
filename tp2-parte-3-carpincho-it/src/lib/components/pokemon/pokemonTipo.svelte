<script lang="ts">
	import type { PokemonTipo } from '$lib/utils/pokemon.interface';

	let { nombre, id, debilidades }: PokemonTipo = $props();
</script>

<div class="ul-div vflex">
	<span class="inline">
		<a class="circle-hoverable" href="/pokemon?tipo={id}">
			<img class="img-icon" src="/vector/tipos/{nombre}.svg" alt={nombre} />
		</a>
		<h4>{nombre}</h4>
	</span>

	Debilidades:

	{#each debilidades as debilidad}
		<p>{debilidad.nombre}</p>
	{/each}
</div>
