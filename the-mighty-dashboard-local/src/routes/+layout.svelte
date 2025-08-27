<script>
	import '../app.css';
	import { onMount } from 'svelte';
	import { page } from '$app/stores';
	
	// Importar componentes de navegación
	import Sidebar from '$lib/components/Sidebar.svelte';
	import Header from '$lib/components/Header.svelte';
	import HelpProvider from '$lib/components/HelpProvider.svelte';
	
	// Estado de la aplicación
	let sidebarOpen = true;
	let currentProject = null;
	let projects = [];
	
	// Función para alternar sidebar
	function toggleSidebar() {
		sidebarOpen = !sidebarOpen;
	}
	
	// Cargar datos iniciales
	onMount(async () => {
		try {
			// Aquí se conectará con las APIs de Tauri para cargar proyectos
			console.log('Dashboard Local iniciado');
		} catch (error) {
			console.error('Error cargando datos iniciales:', error);
		}
	});
</script>

<HelpProvider>
	<div class="flex h-screen bg-gray-50 dark:bg-gray-900">
		<!-- Sidebar -->
		<Sidebar bind:open={sidebarOpen} {currentProject} {projects} />
		
		<!-- Contenido principal -->
		<div class="flex-1 flex flex-col overflow-hidden">
			<!-- Header -->
			<Header {toggleSidebar} {sidebarOpen} {currentProject} />
			
			<!-- Área de contenido -->
			<main class="flex-1 overflow-x-hidden overflow-y-auto bg-gray-50 dark:bg-gray-900 p-6">
				<div class="max-w-7xl mx-auto">
					<slot />
				</div>
			</main>
		</div>
	</div>
</HelpProvider>

<style>
	/* Estilos adicionales si son necesarios */
</style>
