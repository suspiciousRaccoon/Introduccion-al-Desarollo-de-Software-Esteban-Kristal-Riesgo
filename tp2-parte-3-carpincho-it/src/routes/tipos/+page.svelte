<script>
	export let data;
</script>

<h1>Tipos Pokemon</h1>

<div class="ul-div vflex">
	{#each data.tipo as tipos}
		<a class="hoverable element" href={`/pokemon?tipo=${tipos.id}`}>
			{tipos.nombre}
		</a>
	{/each}
</div>
