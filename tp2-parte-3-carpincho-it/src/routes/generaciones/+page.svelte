<script>
	export let data;
</script>

<h1>Generaciones</h1>

<div class="ul-div vflex scatter">
	{#each data.generaciones as generacion}
		<a class="hoverable element" href={`/pokemon?generaciones=${generacion.id}`}>
			{generacion.nombre}
		</a>
	{/each}
</div>
