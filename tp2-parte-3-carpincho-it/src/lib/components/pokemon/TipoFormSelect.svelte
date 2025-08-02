<script lang="ts">
	interface Props {
		tipo_id: number | string;
	}

	let { tipo_id }: Props = $props();
</script>

<select name="tipo" value={String(tipo_id)}>
	<option value="0">Tipo</option>
	<option value="1">Normal</option>
	<option value="2">Lucha</option>
	<option value="3">Volador</option>
	<option value="4">Veneno</option>
	<option value="5">Tierra</option>
	<option value="6">Roca</option>
	<option value="7">Bicho</option>
	<option value="8">Fantasma</option>
	<option value="9">Acero</option>
	<option value="10">Fuego</option>
	<option value="11">Agua</option>
	<option value="12">Planta</option>
	<option value="13">Eléctrico</option>
	<option value="14">Psíquico</option>
	<option value="15">Hielo</option>
	<option value="16">Dragón</option>
	<option value="17">Siniestro</option>
	<option value="18">Hada</option>
</select>
