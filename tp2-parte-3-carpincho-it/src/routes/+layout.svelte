<script>
	import '$lib/styles/styles.css';
	import '$lib/styles/addons.css';
	import '$lib/components/common/darkmode.js';
	import Header from '$lib/components/common/Header.svelte';
	import Footer from '$lib/components/common/Footer.svelte';
</script>

<div class="app">
	<Header />

	<main>
		<slot />
	</main>

	<Footer />
</div>
