<script>
	import '$lib/styles/equipos.css';
	import '$lib/styles/addons.css';
	import EquipoCard from '$lib/components/equipos/EquipoCard.svelte';
	import { enhance } from '$app/forms';
	import Modal from '../../lib/components/common/Modal.svelte';
	import GeneracionFormSelect from '../../lib/components/pokemon/GeneracionFormSelect.svelte';

	let showModalCreate = $state(false);
	let { data } = $props();
</script>

<h1>Equipos</h1>
<div class="spaced-contents max-width">
	<div class="spaced-contents">
		<button onclick={() => (showModalCreate = true)}>Crear Equipo</button>

		<Modal bind:showModal={showModalCreate}>
			{#snippet header()}
				<h2>Crear Equipo</h2>
			{/snippet}

			<form method="POST" action="?/create">
				<input name="nombre" type="text" placeholder="Nombre" minlength="1" />
				<GeneracionFormSelect generacion_id="0" } />
				<button type="submit">
					<img class="dm-invert img-icon" src="vector/mas.svg" alt="Crear" />
				</button>
			</form>
		</Modal>
	</div>

	<div class="equipo-holder">
		{#each data.equipos as equipo}
			<EquipoCard {equipo} />
		{/each}
	</div>
</div>
