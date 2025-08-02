<!-- taken from https://svelte.dev/playground/modal?version=5.34.3 -->
<script>
	import '$lib/styles/modal.css';

	let { showModal = $bindable(), header, children } = $props();

	let dialog = $state(); // HTMLDialogElement

	$effect(() => {
		if (showModal) dialog.showModal();
	});
</script>

<!-- svelte-ignore a11y_click_events_have_key_events, a11y_no_noninteractive_element_interactions -->
<dialog
	bind:this={dialog}
	onclose={() => (showModal = false)}
	onclick={(e) => {
		if (e.target === dialog) dialog.close();
	}}
>
	<div class="vflex">
		{@render header?.()}
		<hr />
		{@render children?.()}
		<hr />
		<!-- svelte-ignore a11y_autofocus -->
		<button class="red center-items" autofocus onclick={() => dialog.close()}>
			<img class="img-icon dm-invert" src="/vector/x.svg" alt="x" />
		</button>
	</div>
</dialog>
