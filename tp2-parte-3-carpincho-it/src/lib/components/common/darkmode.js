import { browser } from '$app/environment'; // required for deferred functions

if (browser) {
	// main webload pre-op, post-op
	const ROOT = document.documentElement; // gather global vars
	const buttonDarkMode = document.getElementById('button-toggle-dark-mode');
	let darkMode = localStorage.getItem('darkMode');

	buttonDarkMode.addEventListener('click', toggleDarkMode);

	console.log('dark mode: ' + darkMode);

	function setDMDataTheme() {
		if (darkMode !== null) {
			ROOT.style.colorScheme = darkMode === 'true' ? 'dark' : 'light';
		}
	}

	function toggleDarkMode() {
		darkMode = (!(localStorage.getItem('darkMode') === 'true')).toString();
		setDMDataTheme();
		localStorage.setItem('darkMode', darkMode);
		console.log('dark mode: ' + darkMode);
	}
}
