const ROOT = document.documentElement;
let darkMode = localStorage.getItem('darkMode');

if (darkMode) {
	darkmode = darkMode.toString();
} else {
	darkMode = matchMedia('(prefers-color-scheme: dark)').matches.toString();
	localStorage.setItem('darkMode', darkMode);
}

setDMDataTheme(ROOT);

function setDMDataTheme() {
	if (darkMode !== null) {
		ROOT.style.colorScheme = darkMode === 'true' ? 'dark' : 'light';
	}
}
