<script lang="ts">
	import Movimientos from '$lib/components/pokemon/Movimientos.svelte';
	import MovimientoResumido from '$lib/components/pokemon/Movimientos.svelte';
	import PokemonCard from '$lib/components/pokemon/pokemonCard.svelte';
	import PokemonTipo from '$lib/components/pokemon/pokemonTipo.svelte';
	import '$lib/styles/pokemon.css';

	let { data } = $props();
</script>

<a class="element hoverable" href="/pokemon">⬅ Volver </a>
<h1>{data.pokemon.nombre}</h1>

<img class="pokemon-img" src={data.pokemon.imagen} alt={data.pokemon.nombre + 'imagen'} />

<!-- stats -->
<div class="container element start">
	<div class="ul-div vflex">
		<p>Altura: {data.pokemon.altura}</p>
		<p>Peso: {data.pokemon.peso}</p>
	</div>
	<div class="ul-div vflex">
		<h4>Habilidades</h4>
		{#each data.pokemon.habilidades as habilidad}
			<p>{habilidad.nombre}</p>
		{/each}
	</div>
	<div class="ul-div vflex">
		<h4>Estadisticas</h4>
		<p>Ataque: {data.pokemon.estadisticas.ataque}</p>
		<p>Defensa: {data.pokemon.estadisticas.defensa}</p>
		<p>Ataque Especial: {data.pokemon.estadisticas.ataque_especial}</p>
		<p>Defensa Especial: {data.pokemon.estadisticas.defensa_especial}</p>
		<p>Puntos de Golpe: {data.pokemon.estadisticas.puntos_de_golpe}</p>
		<p>Velocidad: {data.pokemon.estadisticas.velocidad}</p>
	</div>
	<div class="container start">
		{#each data.pokemon.tipos as tipo}
			<PokemonTipo nombre={tipo.nombre} id={tipo.id} debilidades={tipo.debilidades} />
		{/each}
	</div>
</div>

<!-- evoluciones -->
{#if data.pokemon.evoluciones.length > 0}
	<div>
		<h3>Evolucion/es</h3>
		<div class="pokemon-grid">
			{#each data.pokemon.evoluciones as evolucion}
				<PokemonCard id={evolucion.id} nombre={evolucion.nombre} imagen={evolucion.imagen} />
			{/each}
		</div>
	</div>
{/if}

<!-- Movimientos -->
<div class="container-mov center-items">
	{#if data.pokemon.movimientos_huevo.length > 0}
		<div class="vflex center-items">
			<h3>Movimientos Huevo</h3>
			<Movimientos movimientos={data.pokemon.movimientos_huevo} />
		</div>
	{/if}

	{#if data.pokemon.movimientos_nivel.length > 0}
		<div class="vflex center-items">
			<h3>Movimientos Nivel</h3>
			<Movimientos movimientos={data.pokemon.movimientos_nivel} />
		</div>
	{/if}

	{#if data.pokemon.movimientos_maquina.length > 0}
		<div class="vflex center-items">
			<h3>Movimientos Maquina</h3>
			<Movimientos movimientos={data.pokemon.movimientos_maquina} />
		</div>
	{/if}
</div>

<style>
	.container {
		display: flex;
		gap: 1rem;
	}
	.container-mov {
		display: flex;
		flex-wrap: wrap;
		gap: 1rem;
		max-width: 100%;
		overflow-x: auto;
	}
</style>
