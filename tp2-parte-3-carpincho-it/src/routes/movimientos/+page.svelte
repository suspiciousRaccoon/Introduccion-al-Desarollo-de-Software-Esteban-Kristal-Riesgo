<script lang="ts">
	import '$lib/styles/movimientos.css';
	import Pagination from '$lib/components/common/Pagination.svelte';
	import TipoFormSelect from '$lib/components/pokemon/TipoFormSelect.svelte';
	export let data;
</script>

<h1>Movimientos</h1>
<form action="?/filter" method="GET">
	<input
		name="nombre_parcial"
		type="text"
		placeholder="Nombre Parcial"
		value={data.formInfo.nombreParcial}
	/>
	<TipoFormSelect tipo_id={data.formInfo.tipo} />
	<button class="element hoverable">
		<img class="dm-invert img-icon" src="/vector/buscar.svg" alt="Filtrar" />
	</button>
	<a class="element hoverable" href="/movimientos">
		<img class="dm-invert img-icon" src="/vector/x.svg" alt="Limpiar" />
	</a>
</form>

<div class="ul-div vflex max-width">
	{#each data.movimientos as m}
		<a class="element hoverable max-width" href={`/movimientos/${m.id}`}>
			<div>
				<h3>{m.nombre}</h3>
				<h4>{m.categoria} ({m.tipo.nombre})</h4>

				<p>Potencia: {m.potencia} | Precisión: {m.precision} | PP: {m.puntos_de_poder}</p>
				<p>Efecto: {m.efecto}</p>
			</div>
		</a>
	{/each}
</div>
<Pagination currentPage={data.currentPage} hasMore={data.hasMore} />
