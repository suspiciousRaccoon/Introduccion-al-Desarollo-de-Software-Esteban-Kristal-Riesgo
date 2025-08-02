<script lang="ts">
	import '$lib/styles/equipos.css';
	import IntegranteCard from '$lib/components/equipos/IntegranteCard.svelte';
	import { enhance } from '$app/forms';
	import Modal from '../../../lib/components/common/Modal.svelte';
	import GeneracionFormSelect from '../../../lib/components/pokemon/GeneracionFormSelect.svelte';
	import Typeahead from '$lib/components/common/Typeahead.svelte';
	import { BASE_URL } from '$lib/utils/constants';
	import type { PokemonResumido } from '$lib/utils/pokemon.interface';
	let showModalEdit = $state(false);
	let showModalDelete = $state(false);
	let showModalAgregarIntegrante = $state(false);

	let { data } = $props();
	// @ts-ignore: Unreachable code error
	let selectedPokemon: PokemonResumido = $state({});
</script>

<h1>{data.equipo.nombre}</h1>

<div class="spaced-contents">
	<button onclick={() => (showModalEdit = true)}>Editar Equipo</button>
	<button onclick={() => (showModalDelete = true)} class="red">Borrar Equipo</button>
	<Modal bind:showModal={showModalEdit}>
		{#snippet header()}
			<h2>Editar Equipo</h2>
		{/snippet}

		<form id="edit-equipo" method="POST">
			<input type="text" name="nombre" placeholder="Nombre" value={data.equipo.nombre} />
			<GeneracionFormSelect generacion_id={data.equipo.generacion.id} />

			<div>
				<button class="button-plus" formaction="?/editarEquipo"> Guardar Cambios </button>
			</div>
		</form>
	</Modal>

	<Modal bind:showModal={showModalDelete}>
		{#snippet header()}
			<h2>Borrar Equipo</h2>
		{/snippet}
		Esto también va a borrar a los integrantes del equipo
		<form id="del-equipo" action="?/deleteEquipo" method="POST">
			<input type="hidden" name="equipo_id" value={data.equipo.id} />
			<button class="red"> ELIMINAR EQUIPO </button>
		</form>
	</Modal>

	{#each data.equipo.integrantes as integrante}
		<IntegranteCard equipo={data.equipo} {integrante} />
	{/each}

	{#if data.equipo.integrantes.length < 6}
		<button class="button-plus" onclick={() => (showModalAgregarIntegrante = true)}>
			<img src="/vector/mas.svg" alt="+" height="50px" />
		</button>

		<Modal bind:showModal={showModalAgregarIntegrante}>
			{#snippet header()}
				<h2>Agregar Integrante</h2>
			{/snippet}

			<form id="plus-integrante" action="?/agregarIntegrante" method="POST">
				<Typeahead
					endpoint={BASE_URL + '/pokemon/'}
					placeholder="Buscar pokemon"
					queryKey="nombre_parcial"
					on:select={(event) => {
						selectedPokemon = event.detail.result; // result is a pokemon interface
					}}
				/>
				<input type="hidden" name="equipo_id" id="equipo_id" value={data.equipo.id} />
				<input type="hidden" name="id_pokemon" id="id_pokemon" value={selectedPokemon.id} />
				<input type="text" disabled name="pokemon_name" value={selectedPokemon.nombre} />
				<input type="text" name="apodo" id="apodo" placeholder="Apodo" />
				<button class="button-plus">
					<img src="/vector/mas.svg" alt="+" />
				</button>
			</form>
		</Modal>
	{/if}
</div>
