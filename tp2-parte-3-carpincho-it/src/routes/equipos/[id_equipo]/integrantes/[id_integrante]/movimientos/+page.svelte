<script lang="ts">
	import '$lib/styles/intmov.css';
	import Pagination from '$lib/components/common/Pagination.svelte';
	export let data;

	let seleccionados = new Set<number>();

	function toggle(id: number) {
		if (seleccionados.has(id)) {
			seleccionados.delete(id);
		} else {
			if (seleccionados.size < 4) {
				seleccionados.add(id);
			}
		}
	}
</script>

<h1>Seleccioná hasta 4 movimientos para {data.integrante.apodo}</h1>

<form method="POST" action="?/filter">
	<input
		name="nombreParcial"
		type="text"
		placeholder="Nombre Parcial"
		value={data.formInfo.nombreParcial}
	/>
	<button type="submit">Filtrar</button>
</form>

<form method="POST" action="?/guardar">
	<div class="ul-div vflex-gap">
		{#each data.movimientos as mov}
			<label class="element hoverable">
				<input
					type="checkbox"
					name="movimientos"
					value={mov.id}
					disabled={!seleccionados.has(mov.id) && seleccionados.size >= 4}
					on:change={() => toggle(mov.id)}
					checked={seleccionados.has(mov.id)}
				/>
				{mov.nombre} ({mov.tipo.nombre}) – {mov.categoria}
			</label>
		{/each}
	</div>

	{#each Array.from(seleccionados) as id}
		<input type="hidden" name="movimientos" value={id} />
	{/each}
	<button class="sticky" type="submit"> Guardar </button>
</form>
