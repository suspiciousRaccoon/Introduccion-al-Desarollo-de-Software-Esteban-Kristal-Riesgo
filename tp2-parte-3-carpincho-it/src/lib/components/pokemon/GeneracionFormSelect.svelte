<script lang="ts">
	interface Props {
		generacion_id?: string | number;
	}

	let { generacion_id = 0 }: Props = $props();
</script>

<select name="generaciones" value={String(generacion_id)}>
	<option value="0">Generacion</option>
	<option value="1">Generación I</option>
	<option value="2">Generación II</option>
	<option value="3">Generación III</option>
	<option value="4">Generación IV</option>
	<option value="5">Generación V</option>
	<option value="6">Generación VI</option>
	<option value="7">Generación VII</option>
	<option value="8">Generación VIII</option>
</select>
