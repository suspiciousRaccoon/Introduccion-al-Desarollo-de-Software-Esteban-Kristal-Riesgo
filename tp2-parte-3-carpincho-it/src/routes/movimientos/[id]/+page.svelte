<script lang="ts">
	import '$lib/styles/movimientos.css';
	export let data;
</script>

<a class="element hoverable" href="/movimientos">⬅ Volver </a>
<h1>{data.movimiento.nombre}</h1>

<div class="ul-div vflex">
	<div class="ul-div">
		<p class="element">Tipo: {data.movimiento.tipo.nombre}</p>
		<p class="element">Potencia: {data.movimiento.potencia}</p>
		<p class="element">Precisión: {data.movimiento.precision}</p>
	</div>

	<p class="element">Efecto: {data.movimiento.efecto}</p>
	<p class="element">PP: {data.movimiento.puntos_de_poder}</p>
	<p class="element">Generacion: {data.movimiento.generacion.nombre}</p>
</div>

<h2>Aprendido por nivel</h2>
<div class="ul-div">
	{#each data.movimiento.pokemon_por_nivel as p}
		<a class="hoverable" href="/pokemon/{p.id}">
			{p.nombre}
		</a>
	{/each}
</div>

<h2>Aprendido por huevo</h2>
<div class="ul-div">
	{#each data.movimiento.pokemon_por_huevo as p}
		<a class="hoverable" href="/pokemon/{p.id}">
			{p.nombre}
		</a>
	{/each}
</div>

<h2>Aprendido por máquina</h2>
<div class="ul-div">
	{#each data.movimiento.pokemon_por_maquina as p}
		<a class="hoverable" href="/pokemon/{p.id}">
			{p.nombre}
		</a>
	{/each}
</div>
