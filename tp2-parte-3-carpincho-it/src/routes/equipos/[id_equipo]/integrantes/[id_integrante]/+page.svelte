<script>
	import IntegranteCard from '$lib/components/equipos/IntegranteCard.svelte';
	import '$lib/styles/equipos.css';
	export let data;

	let movs = Array(4);
	let idx = 0;
	data.integrante.movimientos.forEach((mov) => {
		movs[idx] = mov.id;
		idx += 1;
	});
</script>

<div class="element">
	<div class="vflex">
		<img
			class="pokemon-img"
			src={data.integrante.pokemon.imagen}
			alt="Imagen de {data.integrante.apodo}"
		/>
		<form class="vflex" action="?/updateIntegrante" method="POST">
			<input type="hidden" name="equipo_id" value={data.equipo.id} />
			<input type="hidden" name="integrante_id" value={data.integrante.id} />
			<input
				class="hoverable"
				type="text"
				name="apodo"
				placeholder="Apodo"
				value={data.integrante.apodo}
			/>
			<span>
				<select class="hoverable" name="mov1" id="mov1" value={movs[0]}>
					<option value="0">Movimiento 1 (ninguno)</option>
					{#each data.movimientosValidos as movimientos}
						{#each movimientos as mov}
							<option value={mov.id}>{mov.nombre}</option>
						{/each}
					{/each}
				</select>

				<select class="hoverable" name="mov2" id="mov2" value={movs[1]}>
					<option value="0">Movimiento 2 (ninguno)</option>
					{#each data.movimientosValidos as movimientos}
						{#each movimientos as mov}
							<option value={mov.id}>{mov.nombre}</option>
						{/each}
					{/each}
				</select>

				<select class="hoverable" name="mov3" id="mov3" value={movs[2]}>
					<option value="0">Movimiento 3 (ninguno)</option>
					{#each data.movimientosValidos as movimientos}
						{#each movimientos as mov}
							<option value={mov.id}>{mov.nombre}</option>
						{/each}
					{/each}
				</select>

				<select class="hoverable" name="mov4" id="mov4" value={movs[3]}>
					<option value="0">Movimiento 4 (ninguno)</option>
					{#each data.movimientosValidos as movimientos}
						{#each movimientos as mov}
							<option value={mov.id}>{mov.nombre}</option>
						{/each}
					{/each}
				</select>
			</span>

			<button class="green" type="submit">Guardar Cambios</button>
		</form>
	</div>
</div>
