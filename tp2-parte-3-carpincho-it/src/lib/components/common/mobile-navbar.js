import { browser } from '$app/environment'; // required for deferred functions

if (browser) {
	// main webload pre-op, post-op
	const buttonMenu = document.getElementById('button-toggle-menu');
	let buttonImg = document.getElementById('button-toggle-menu-img');
	let header = document.getElementById('header');
	const IMGS = ['/vector/menu-closed.svg', '/vector/menu-open.svg'];

	buttonMenu.addEventListener('click', toggleMenu);

	function toggleMenu() {
		let status = header.getAttribute('collapsed') == 'true';
		buttonImg.setAttribute('src', IMGS[+status]);
		header.setAttribute('collapsed', !status);
	}
}
