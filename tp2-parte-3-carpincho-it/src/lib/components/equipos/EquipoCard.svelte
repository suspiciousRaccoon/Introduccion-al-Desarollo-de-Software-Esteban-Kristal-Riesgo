<script lang="ts">
	import '$lib/styles/equipoCard.css';
	import type { EquipoResumido } from '$lib/utils/equipo.interface';
	let { equipo }: { equipo: EquipoResumido } = $props();
</script>

<div class="element horizontal-container">
	<div class="primary-contents">
		<h3>{equipo.nombre}</h3>

		<div class="secondary-contents">
			<p>{equipo.generacion.nombre}</p>
			<div class="equipo-pokemon-container">
				{#each Array(equipo.cant_integrantes) as _}
					<img src="png/carpincho.png" alt="pokemon" />
				{/each}
			</div>
		</div>
	</div>

	<a class="red hoverable" href={'/equipos/' + equipo.id.toString()}>
		<img class="dm-invert img-icon" src="vector/arrow-right.svg" alt="Detalles" />
	</a>
</div>
