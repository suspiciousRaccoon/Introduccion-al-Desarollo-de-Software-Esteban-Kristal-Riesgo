<script lang="ts">
	import type { MovimientoResumido } from '$lib/utils/pokemon.interface';
	import '$lib/styles/movimientoTable.css';
	let { movimientos }: { movimientos: MovimientoResumido[] } = $props();
</script>

<table>
	<thead>
		<tr>
			<th>Nombre</th>
			<th>Tipo</th>
			<th>Categoria</th>
			<th>Potencia</th>
			<th>Precision</th>
			<th>Puntos de Poder</th>
			<th>Generacion</th>
			<th>Efecto</th>
		</tr>
	</thead>
	<tbody>
		{#each movimientos as movimiento}
			<tr>
				<td>
					<a class="center-items" href="/movimientos/{movimiento.id}">
						{movimiento.nombre}
						<img
							class="dm-invert img-icon"
							src="https://www.svgrepo.com/show/491630/external-link.svg"
							alt="link"
						/>
					</a>
				</td>
				<td>{movimiento.tipo.nombre}</td>
				<td>{movimiento.categoria}</td>
				<td>{movimiento.potencia}</td>
				<td>{movimiento.precision}</td>
				<td>{movimiento.puntos_de_poder}</td>
				<td>{movimiento.generacion.nombre}</td>
				<td>{movimiento.efecto}</td>
			</tr>
		{/each}
	</tbody>
</table>
