<script>
	import '$lib/styles/header.css';
	import '$lib/components/common/mobile-navbar.js';
</script>

<header id="header" collapsed="true">
	<div>
		<nav id="complete-nav">
			<a aria-label="Home" class="button-navbar" id="logo" href="/"></a>

			<nav id="partial-nav">
				<a class="button-navbar" href="/pokemon">
					<img src="/vector/pokemon.svg" alt="icon" />
					Pokemon
				</a>

				<a class="button-navbar" href="/equipos">
					<img src="/vector/equipo.svg" alt="icon" />
					Equipos
				</a>

				<a class="button-navbar" href="/movimientos">
					<img src="/vector/movimiento.svg" alt="icon" />
					Movimientos
				</a>

				<a class="button-navbar" href="/generaciones">
					<img src="/vector/generacion.svg" alt="icon" />
					Generaciones
				</a>

				<a class="button-navbar" href="/tipos">
					<img src="/vector/tipo.svg" alt="icon" />
					Tipos
				</a>
			</nav>

			<button id="button-toggle-dark-mode">
				<img src="/vector/dark-mode.svg" alt="Dark Mode" />
			</button>
		</nav>
		<button id="button-toggle-menu">
			<!-- depends on whether app is within navbar limits (mobile), and if open -->
			<img id="button-toggle-menu-img" src="/vector/menu-closed.svg" alt="Menu" />
		</button>
	</div>
</header>
