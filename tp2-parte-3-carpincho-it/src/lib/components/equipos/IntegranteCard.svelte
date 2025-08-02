<script>
	let { integrante, equipo } = $props();
	import '$lib/styles/integranteCard.css';
</script>

<div class="element integrante-card">
	<div class="vflex-gap">
		<span class="inline">
			<h3>{integrante.apodo}</h3>
			{#each integrante.pokemon.tipos as tipo}
				<!-- https://github.com/partywhale/pokemon-type-icons -->
				<a class="circle-hoverable" href="/pokemon?tipo={tipo.id}">
					<img class="img-icon" src="/vector/tipos/{tipo.nombre}.svg" alt={tipo.nombre} />
				</a>
			{/each}
		</span>
		<a class="hoverable aframe" href="/pokemon/{integrante.pokemon.id}">
			<img
				class="pokemon-img"
				src={integrante.pokemon.imagen}
				alt="imagen de {integrante.pokemon.nombre}"
			/>
		</a>
	</div>

	<div class="movimiento-container">
		<h3>
			{#if integrante.movimientos.length > 0}
				Movimientos
			{:else}
				Sin Movimientos.
			{/if}
		</h3>

		<div>
			{#each integrante.movimientos as movimiento}
				<a class="hoverable" href="/movimientos/{movimiento.id}">
					{movimiento.nombre}
				</a>
			{/each}

			{#if integrante.movimientos.length < 4}
				<a
					class="hoverable button-plus button-agregar-movimiento"
					href={`/equipos/${equipo.id}/integrantes/${integrante.id}/movimientos`}
				>
					<img class="img-icon dm-invert" src="/vector/mas.svg" alt="+" />
				</a>
			{/if}
		</div>
	</div>

	<div class="options-integrante">
		<a class="hoverable bg max-height" href="/equipos/{equipo.id}/integrantes/{integrante.id}">
			<img class="img-icon dm-invert" src="/vector/edit.svg" alt="Editar" />
		</a>
		<form class="max-height" action="?/deleteIntegrante" method="POST">
			<input type="hidden" name="equipo_id" value={equipo.id} />
			<input type="hidden" name="integrante_id" value={integrante.id} />
			<button class="red" type="submit">
				<img class="img-icon dm-invert" src="/vector/x.svg" alt="Eliminar" />
			</button>
		</form>
	</div>
</div>
<!-- <select class="hoverable" name="mov4" id="mov4" value={movs[3]}>
                    <option value="0">Movimiento 4</option>
                    {#each data.movimientosValidos as movimientos}
                        {#each movimientos as mov}
                            <option value={mov.id}>{mov.nombre}</option>
                        {/each}
                    {/each}
                </select>
            </span> -->

<!-- <button class="green" type="submit">Guardar Cambios</button>
        </form> -->
